---
title: "2. The fundamental link between dispersion and the electron density"
collection: research
order: 2
summary: "Dispersion is widely regarded as an additive energy correction. However, in large systems it is not that simple — dispersion reshapes the electron density itself."
figures:
  - file: '2_mbd_esp.jpg'
    alt: 'Dispersion-induced electrostatic potential map'
    caption: 'Map of the dispersion-induced electrostatic potential for the buckyball catcher (in kcal/mol).'
  - file: '2_mbd_en_dens_DNA.jpg'
    alt: ''
    caption: 'The MBD energy density plotted in real space for the DNA-ellipticine complex.'
ongoing: >-
  I am also developing a reduced-density-matrix formulation of the many-body 
  dispersion (MBD) model, which recasts the dispersion energy as a 
  **scalar energy density field** rather than a single number. If it works, 
  dispersion stops being one number per system and becomes something you can 
  look at in space, seeing *where* the dispersion energy sits.
key_papers:
  - label: "JACS 2025"
    url: "https://doi.org/10.1021/jacs.5c13706"
  - label: "Dataset (Zenodo)"
    url: "https://doi.org/10.5281/zenodo.18865966"
---

Density-functional approximations are usually judged on energies, and long-range
dispersion is added afterwards as a correction that leaves the density untouched.
That is reasonable for small molecules, but not necessarily for large,
polarizable systems — exactly the question I studied.

Across more than 30 molecular and supramolecular systems, benchmarked against
carefully converged CCSD−HF reference density differences, dispersion turns out
to **polarize electron densities substantially**, shifting long-range
electrostatic potentials by up to 4 kcal/mol. That is a non-trivial coupling
between dispersion and electrostatics — two contributions that are routinely
treated as separable. This has consequences for any density-derived quantity,
from electrostatic potentials to density-based bonding indicators.

There is also an uncomfortable implication for the functionals themselves. In
the systems where polarization matters most, an exchange–correlation
approximation evaluates the energy at a slightly wrong density, and how much
that costs in supramolecular complexes and proteins is what I would eventually
like to find out. The hard part is disentangling the two contributions:
semilocal functionals already capture some dispersion at intermediate range, by
an amount that is difficult to pin down, and that overlap is normally hidden
inside an empirically fitted damping function.
