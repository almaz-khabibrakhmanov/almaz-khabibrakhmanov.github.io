---
title: "MBD-ML: Many-Body Dispersion from Machine Learning for Molecules and Materials"
collection: publications
selected: true
category: manuscripts
permalink: /publication/2026-MBD-ML-PRXI
excerpt: 'Non-local many-body dispersion (MBD-NL) is one of the most accurate for describing long-range van der Waals interactions, yet its application has traditionally been limited to electronic-structure codes with native MBD-NL implementations, since it requires atomic polarizabilities and dispersion coefficients derived from the electron density. In the present work, we close this gap by introducing MBD-ML, a machine-learning model that predicts these quantities directly from atomic structure. As a result, MBD can be combined with virtually any atomistic method, including DFT, semi-empirical approaches, and machine-learning force fields, without requiring access to the underlying electron density.'
date: 2026-07-28
venue: 'PRX Intelligence'
paperurl: 'https://doi.org/10.1103/pv86-l9h7'
pdfurl: '../files/papers/2026-MBD-ML-PRXI.pdf'
citation: 'E. Moerman, A. Kabylda, <b>A. Khabibrakhmanov</b>, A. Tkatchenko, <a href="https://doi.org/10.1103/pv86-l9h7">MBD-ML: Many-Body Dispersion from Machine Learning for Molecules and Materials</a>, <i>PRX Intelligence</i> <b>1</b>, 013003 (2026).'
toc_image: '2026-MBD-ML-PRXI.png'
supplementary: '../files/papers/2026-MBD-ML-SM-PRXI.pdf'
---
<b>Abstract:</b> van der Waals (vdW) interactions are essential for describing molecules and materials, from drug design and catalysis to battery applications. These omnipresent interactions must also be accurately included in machine-learned (ML) force fields. The many-body dispersion (MBD) method stands out as one of the most accurate and transferable approaches to capture vdW interactions, requiring only atomic $C_6$ coefficients and polarizabilities as input. We present MBD-ML, a pretrained message-passing neural network that predicts these atomic properties directly from structures with demonstrated transferability across molecular systems and organic condensed phases. Through seamless integration with libMBD, our method enables the immediate calculation of MBD-inclusive total energies, forces, and stress tensors. By eliminating the need for intermediate electronic-structure calculations, MBD-ML offers a practical and streamlined tool that simplifies the incorporation of state-of-the-art vdW interactions into any electronic-structure code, as well as empirical and machine-learned force fields.

