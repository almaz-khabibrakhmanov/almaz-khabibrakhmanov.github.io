# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.extra.rate_limiter import RateLimiter

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate.
# Nominatim's usage policy requires a meaningful User-Agent and max 1 request/second.
# RateLimiter enforces the 1 req/sec cap and retries transient 429/Timeout errors,
# avoiding "HTTP 429 Too Many Requests" when many talks are processed in a row.
nominatim = Nominatim(user_agent="almaz-khabibrakhmanov.github.io (talkmap script)")
geocoder = RateLimiter(
    nominatim.geocode,
    min_delay_seconds=1.1,        # safety margin above the 1/sec limit
    max_retries=2,
    error_wait_seconds=5.0,
    swallow_exceptions=False,
)
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Read fields
    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()

    # Popup description: use the dedicated 'map_description' frontmatter field when set,
    # otherwise fall back to a generated string. The fallback also guarantees uniqueness
    # so empty map_descriptions don't collide into a single dict key.
    description = (data.get('map_description') or '').strip()
    if not description:
        description = f"{title}<br />{venue}; {location}"

    # Geocode the venue first (more precise), fall back to the city-level location.
    # This separates multiple conferences held in the same city onto their real venues.
    query = f"{venue}, {location}"
    try:
        result = geocoder(query, timeout=TIMEOUT)
        if result is None:
            print(f"Venue '{query}' not found — falling back to city-level '{location}'")
            result = geocoder(location, timeout=TIMEOUT)
        location_dict[description] = result
        print(description, result)
    except ValueError as ex:
        print(f"Error: geocode failed on input {query} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {query} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {query} with message {ex}")

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
