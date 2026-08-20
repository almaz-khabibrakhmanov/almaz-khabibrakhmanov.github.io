---
layout: archive
title: "CV"
description: "Curriculum vitae of Almaz Khabibrakhmanov, postdoctoral researcher in theoretical chemical physics at the University of Luxembourg."
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
title_button:
  label: "Download CV (PDF)"
  url: /files/cv/Khabibrakhmanov_CV.pdf
---

{% include base_path %}

Professional Experience
------
* March 2025 -- present: <b>Postdoctoral Researcher</b>
  * University of Luxembourg, [TCP group](https://tcpunilu.com/)
  * Advisor: [Prof. Dr. Alexandre Tkatchenko](https://scholar.google.com/citations?user=o2t1Pv8AAAAJ&hl=en&oi=ao)
 
* March -- June 2022: <b>Visiting Graduate Researcher</b>
  * [Institute for Pure and Applied Mathematics](https://www.ipam.ucla.edu/programs/long-programs/advancing-quantum-mechanics-with-mathematics-and-statistics/), UCLA, Los Angeles
  * Advisor: Prof. Dr. Alexandre Tkatchenko

* January 2021 -- March 2025: <b>Doctoral Researcher</b>
  * University of Luxembourg, TCP group
  * Advisor: Prof. Dr. Alexandre Tkatchenko

* October 2019 -- November 2020: <b>Research Assistant</b>
  * NUST "MISiS", [Laboratory of Digital Materials Science](https://ldms.misis.ru/main_en), Moscow
  * Advisor: [Prof. Dr. Pavel Sorokin](https://scholar.google.com/citations?user=41ttua4AAAAJ&hl=en&oi=ao)

* September 2017 -- June 2020: <b>Research Assistant</b>
  * Technological Institute for Superhard and Novel Carbon Materials, Moscow
  * Advisor: Prof. Dr. Pavel Sorokin

Education
------
* 2025 -- **Ph.D. in Physics**, University of Luxembourg
  * Thesis: [Bridging Quantum Drude Oscillators and Electronic-Structure Theory for van der Waals Dispersion Interactions](https://tcpunilu.com/pages/assets/img/Theses/AKhabibrakhmanov2025.pdf)  
* 2020 -- **M.Sc. in Applied Mathematics & Physics**, Moscow Institute of Physics and Technology
  * Thesis: [Theoretical Study of Diamond-Like Carbon Nanostructures and Their Mechanical Stiffness](https://almaz-khabibrakhmanov.github.io/files/theses/AKhabibrakhmanov_MSc_Thesis_2020.pdf) (RU)
* 2018 -- **B.Sc. in Applied Mathematics & Physics**, Moscow Institute of Physics and Technology
  * Thesis: [Theoretical Investigation of the Atomic Structure and Mechanical Properties of Novel Dense sp<sup>3</sup>-Carbon Nanostructures](https://almaz-khabibrakhmanov.github.io/files/theses/AKhabibrakhmanov_BSc_Thesis_2018.pdf) (RU)

Skills & Software Experience
------
* Density Functional Theory: [FHI-aims](https://fhi-aims.org/), [VASP](https://vasp.at/), [SIESTA](https://siesta-project.org/siesta/)
* Quantum Chemistry: [PySCF](https://pyscf.org/), [Q-Chem](https://www.q-chem.com/), [ORCA](https://www.faccts.de/orca/), [MRCC](https://www.mrcc.hu/)
* Molecular Dynamics: [LAMMPS](https://www.lammps.org/)
* Visualization & Analysis: [OVITO](https://www.ovito.org/), [VESTA](https://jp-minerals.org/vesta/en/), [ChimeraX](https://www.cgl.ucsf.edu/chimerax/), [Jmol](https://jmol.sourceforge.net/)
* Coding: Python, Fortran, Bash, MATLAB, C++
* High-Performance Computing: MPI/OpenMP, Slurm
* Code Development & Modifications: [libMBD](https://github.com/libmbd/libmbd), FHI-aims, LAMMPS

Selected Publications
------
{% assign selected_pubs = site.publications | where: 'selected', true | sort: 'date' | reverse %}
<ul class="cv-sel-list">
{% for post in selected_pubs %}
  <li>{{ post.citation }}</li>
{% endfor %}
</ul>
<p class="cv-sel-fulllist"><a href="{{ base_path }}/publications/">See the full list of publications &rarr;</a></p>

Selected Conferences
------
{% assign selected_talks = site.talks | where: 'selected', true | sort: 'date' | reverse %}
<ul class="cv-sel-list">
{% for post in selected_talks %}
  <li>
    {% if post.conference_url %}<a class="cv-sel-title" href="{{ post.conference_url }}" target="_blank" rel="noopener">{{ post.title }}</a>{% else %}<span class="cv-sel-title">{{ post.title }}</span>{% endif %}<br>
    <span class="cv-sel-meta">{{ post.type }} &middot; {{ post.venue }}, {{ post.location }} &middot; {{ post.date | date: '%B %Y' }}</span>
  </li>
{% endfor %}
</ul>
<p class="cv-sel-fulllist"><a href="{{ base_path }}/talks/">See the full list of talks &amp; posters &rarr;</a></p>

Awards
------
<ul class="cv-sel-list">
  <li>
    {% comment %} The award text itself is the click target; it opens a self-contained
    <dialog> lightbox of the certificate photo. Same no-JS pattern as the Publications
    TOC images, so it survives the production HTML minifier. {% endcomment %}
    <a class="award-link" tabindex="0" onclick="this.nextElementSibling.showModal()">Best Poster Award at the NCAITMS conference, Warsaw (2025)</a>
    <dialog class="award-modal" onclick="this.close()">
      <img src="{{ base_path }}/files/portfolio/NCAITMS_best_poster.jpg" alt="Best Poster Award certificate, NCAITMS conference, Warsaw 2025">
    </dialog>
  </li>
  <li><i>Summa cum Laude</i> graduation from B.Sc. (2018) and M.Sc. (2020)</li>
  <li>Letter of acknowledgement for achievements in research, Russian Ministry of Science and Higher Education (2020)</li>
  <li>Increased Academic Scholarship for excellence in study (2017 &ndash; 2020)</li>
  <li>Alexander Abramov's Fund Scholarship for excellence in study (2015 &ndash; 2017)</li>
  <li>Prize winner of regional Olympiads in physics and chemistry (2012 &ndash; 2014)</li>
</ul>

Teaching & Service
------
* Reviewer for <i>The Journal of Chemical Physics</i> and <i>Journal of Chemical Theory and Computation</i> since 2023
{% assign teaching_items = site.teaching | sort: 'date' | reverse %}
<ul class="cv-sel-list">
{% for post in teaching_items %}
  <li>
    <a class="cv-sel-title" href="{{ base_path }}{{ post.url }}">{{ post.title }}</a><br>
    <span class="cv-sel-meta">{{ post.type }} &middot; {{ post.venue }}, {{ post.location }} &middot; {{ post.date | date: '%B %Y' }}</span>
  </li>
{% endfor %}
</ul>


