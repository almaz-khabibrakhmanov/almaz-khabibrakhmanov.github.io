---
title: "3. From accurate physics to large-scale simulation"
collection: research
order: 3
summary: "This is where the coarse-grained models above meet production simulations."
figures:
  - file: '3_so3lr.jpg'
    alt: ''
    caption: 'Overview of the SO3LR architecture. The long-range modules complement the neural network.'
  - file: '3_mbd-ml.jpg'
    alt: ''
    caption: 'Overview of the MBD-ML approach. The neural network predicts polarizability and dispersion coefficient ratios, serving as inputs to libMBD.'
ongoing: >-
  Making ML-based long-range methodologies transferable across chemical space is still an open challenge. Extending them to work reliably across broad classes of materials and hybrid interfaces is one of the directions I intend to pursue.
key_papers:
  - label: "SO3LR"
    url: "https://doi.org/10.1021/jacs.5c09558"
  - label: "MBD-ML"
    url: "https://doi.org/10.1103/pv86-l9h7"
---

Machine-learned force fields have largely solved short-range accuracy, but they
inherit a long-standing weakness at long range, where dispersion and
electrostatics dominate. Physically grounded, transferable models are the natural
fix — and they only need to be derived once.

The universal vdW potential from my QDO work serves exactly this role: it is the
long-range dispersion module inside **SO3LR**, which couples the SO3krates
neural network for semilocal interactions with universal pairwise terms for
short-range repulsion, electrostatics and dispersion, enabling stable
simulations of large and diverse biomolecular systems. In **MBD-ML**, machine learning
supplies the inputs that the nonlocal many-body dispersion (MBD-NL) formalism normally requires from an
electronic-structure code, freeing one of the most accurate available dispersion
treatments from that dependency.

Both are collaborative projects in which I contributed the long-range dispersion component 
and expertise in physics rather than leading the work — but they are the clearest
evidence that the models in the sections above survive contact with real
simulations.
