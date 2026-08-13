---
title: "1. Quantum Drude oscillators: a minimal model of electronic response"
collection: research
order: 1
summary: "How far can three numbers — a frequency, a mass and a charge — go in describing how atoms respond to each other?"
figures:
  - file: '1_qdo_jpcl.png'
    alt: 'Schematic of two coupled quantum Drude oscillators: a positive pseudo-nucleus harmonically bound to a negative Drude particle, two such atoms separated by a distance R and coupled through the Coulomb interaction'
    caption: 'Two coupled quantum Drude oscillators. Correlated displacements of the Drude particles give the dispersion attraction.'
  - file: '1_binding_curves.png'
    alt: 'vdW binding curves from the QDO potential'
    caption: 'Optional caption under that one'
ongoing: >-
  I am currently pushing the model into territory it was never built for:
  **covalent bonding**. At this stage it is a proof of concept, and its 
  value lies in mapping where the model works and where it genuinely breaks. 
  If successful, this points towards a single coarse-grained framework 
  covering covalent and noncovalent bonding alike.
key_papers:
  - label: "JCP 2025 (review)"
    url: "https://doi.org/10.1063/5.0281913"
  - label: "JCTC 2023"
    url: "https://doi.org/10.1021/acs.jctc.3c00797"
  - label: "JPCL 2023"
    url: "https://doi.org/10.1021/acs.jpclett.3c01221"
---

Most of my work rests on one idea: an atom's valence electron cloud can be
represented as a quantum harmonic oscillator — a quantum Drude oscillator (QDO)
— defined by just a frequency, a mass and a charge. The win is that
response and interaction properties then follow analytically, without an
electronic-structure calculation.

Two results make the model practical. In the **optimized QDO (OQDO)**
parametrization, all three parameters are fixed from only the static dipole
polarizability and the $$C_6$$ coefficient — giving accurate
polarization potentials and multipolar dispersion coefficients across the
periodic table. Building on that, I derived a **universal pairwise vdW
potential** whose functional form comes from the QDO model itself and which
again needs only $$\alpha_1$$ and $$C_6$$ per element. It has since been adopted
as the long-range module in machine-learned force-field frameworks including
[SO3LR](https://github.com/general-molecular-simulations/so3lr) and [FeNNol](https://github.com/FeNNol-tools/FeNNol).

I also led a community review synthesizing what QDO models can and cannot do,
written with colleagues across the field.
