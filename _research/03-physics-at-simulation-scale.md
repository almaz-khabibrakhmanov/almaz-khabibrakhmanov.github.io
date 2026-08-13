---
title: "3. From accurate physics to large-scale simulation"
collection: research
order: 3
summary: "Accuracy only matters if it runs. This is where the models above meet production simulations."
figures:
  - file: '3_so3lr.jpg'
    alt: 'vdW binding curves from the QDO potential'
    caption: 'Optional caption under that one'
  - file: '3_mbd-ml.jpg'
    alt: 'Schematic of two coupled quantum Drude oscillators: a positive pseudo-nucleus harmonically bound to a negative Drude particle, two such atoms separated by a distance R and coupled through the Coulomb interaction'
    caption: 'Two coupled quantum Drude oscillators. Correlated displacements of the Drude particles give the dispersion attraction.'
ongoing: >-
  Extending ML-based long-range methodologies reliably to a broader chemical space — that is an open challenge. Extending MBD-ML to work for materials and hybrid interfaces is one of my prospective research topics.
key_papers:
  - label: "SO3LR"
    url: "https://doi.org/10.1021/jacs.5c09558"
  - label: "MBD-ML"
    url: "https://doi.org/10.1103/pv86-l9h7"
---

Machine-learned force fields have largely solved short-range accuracy, but they
inherit a long-standing weakness at long range, where dispersion and
electrostatics live. Physically grounded, transferable models are the natural
fix — and they only need to be derived once.

The universal vdW potential from my QDO work serves exactly this role: it is the
long-range dispersion module inside **SO3LR**, which couples the SO3krates
neural network for semilocal interactions with universal pairwise terms for
short-range repulsion, electrostatics and dispersion, enabling stable
simulations of large biomolecular systems. In **MBD-ML**, machine learning
supplies the inputs that nonlocal many-body dispersion normally requires from an
electronic-structure code, freeing one of the most accurate available dispersion
treatments from that dependency.

Both are collaborative projects in which I contributed the dispersion and
long-range electrostatics components rather than leading the work — but they are the clearest
evidence that the models in the sections above survive contact with real
simulations.
