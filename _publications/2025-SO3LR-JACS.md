---
title: "Molecular Simulations with a Pretrained Neural Network and Universal Pairwise Force Fields"
collection: publications
category: manuscripts
permalink: /publication/2025-SO3LR-JACS
excerpt: 'This work introduces the SO3LR method that integrates the fast and stable SO3krates neural network for semilocal interactions with universal pairwise force fields designed for short-range repulsion, long-range electrostatics, and dispersion interactions. My contribution was designing and implementing these long-range modules based on my prior work on the universal vdW-QDO potentials. SO3LR is trained on a diverse PBE0+MBD dataset of 4 million neutral and charged molecular complexes, ensuring broad coverage of covalent and noncovalent interactions. SO3LR is applied to study units of four major biomolecule types, polypeptide folding, and nanosecond dynamics of larger systems such as a protein, a glycoprotein, and a lipid bilayer, all in explicit solvent, demonstrating reasonable to high accuracy.'
date: 2025-08-31
venue: 'The Journal of the American Chemical Society'
paperurl: 'https://doi.org/10.1021/jacs.5c09558'
pdfurl: 'http://almaz-khabibrakhmanov.github.io/files/papers/2025-SO3LR-JACS.pdf'
citation: 'A. Kabylda, J. T. Frank, S. Suárez-Dou, <b>A. Khabibrakhmanov</b>, L. M. Sandonas, O. T. Unke, S. Chmiela, K.-R.&nbspMüller, A. Tkatchenko, <a href="https://doi.org/10.1021/jacs.5c09558">Molecular Simulations with a Pretrained Neural Network and Universal Pairwise Force Fields</a>, <i>J.&nbspAm. Chem. Soc.</i> <b>147</b>(37), 33723–33734 (2025).'
toc_image: '2025-SO3LR-JACS.png'
supplementary: 'http://almaz-khabibrakhmanov.github.io/files/papers/2025-SO3LR-SM-JACS.pdf'
---
<b>Abstract:</b> Machine Learning Force Fields (MLFFs) promise to enable general molecular simulations that can simultaneously achieve efficiency, accuracy, transferability, and scalability for diverse molecules, materials, and hybrid interfaces. A key step toward this goal has been made with the GEMS approach to biomolecular dynamics [Unke <i>et al.</i>, Sci. Adv. <b>2024</b>, <i>10</i>, eadn4397]. This work introduces the SO3LR method that integrates the fast and stable SO3krates neural network for semilocal interactions with universal pairwise force fields designed for short-range repulsion, long-range electrostatics, and dispersion interactions. SO3LR is trained on a diverse set of 4 million neutral and charged molecular complexes computed at the PBE0+MBD level of quantum mechanics, ensuring broad coverage of covalent and noncovalent interactions. Our approach is characterized by computational and data efficiency, scalability to 200 thousand atoms on a single GPU, and reasonable to high accuracy across the chemical space of organic (bio)molecules. SO3LR is applied to study units of four major biomolecule types, polypeptide folding, and nanosecond dynamics of larger systems such as a protein, a glycoprotein, and a lipid bilayer, all in explicit solvent. Finally, we discuss future challenges toward truly general molecular simulations by combining MLFFs with traditional atomistic models.

