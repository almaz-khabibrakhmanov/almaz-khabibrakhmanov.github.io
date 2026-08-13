---
title: "2. Mutual connection of dispersion and the electron density"
collection: research
order: 2
summary: "Dispersion is usually bolted onto a calculation as a scalar energy correction. It is not scalar — it reshapes the electron density itself."
figures:
  - file: '2_mbd_esp.jpg'
    alt: 'vdW binding curves from the QDO potential'
    caption: 'Optional caption under that one'
  - file: '2_mbd_en_dens_DNA.jpg'
    alt: 'Schematic of two coupled quantum Drude oscillators: a positive pseudo-nucleus harmonically bound to a negative Drude particle, two such atoms separated by a distance R and coupled through the Coulomb interaction'
    caption: 'Two coupled quantum Drude oscillators. Correlated displacements of the Drude particles give the dispersion attraction.'
ongoing: >-
  A reduced-density-matrix formulation of the many-body dispersion (MBD) model,
  which recasts the dispersion energy as a **scalar field in real space** rather
  than a single number. The practical prize would be genuine spatial
  visualization of noncovalent interactions — seeing *where* dispersion energy
  sits.
key_papers:
  - label: "JACS 2025"
    url: "https://doi.org/10.1021/jacs.5c13706"
  - label: "Dataset (Zenodo)"
    url: "https://doi.org/10.5281/zenodo.18865966"
---

Density-functional approximations are usually judged on energies, and long-range
dispersion is added afterwards as a correction that leaves the density untouched.
I asked what that assumption costs.

Across more than 30 molecular and supramolecular systems, benchmarked against
carefully converged CCSD−HF reference density differences, dispersion turns out
to **polarize electron densities substantially**, shifting long-range
electrostatic potentials by up to 4 kcal/mol. That is a non-trivial coupling
between dispersion and electrostatics — two contributions that are routinely
treated as separable — and it has consequences for any density-derived quantity:
electrostatic potentials, density-based indicators, embedding schemes.

Establishing the effect required building reproducible protocols for
high-level reference densities, which I curated and published as an open dataset
rather than leaving on a cluster.
