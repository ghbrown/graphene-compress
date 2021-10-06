
Domain specific compression of deformed atomistic sheet geometries using sparse approximation.

### Theory
All discrete objects are written in brackets, continuum objects are unadorned.

A flat sheet of graphene is considered to have pristine discrete coordinates `[F]` defined solely by the lattice vectors and atomic basis.
`[F]` will be an implict part of the final representation as explained below.

Given some deformed configuration `[D]`, one can partition `[D]` into the pristine coordinates plus the evaluation of some continuum displacement field `S` at the points in `[F]`.

```
[D] = [F] + S([F]) 
```
noting that `S([F])` is a disrcete quantity.

We then seek to approximate the deformed configuration `[D]` by making use of some basis functions for the displacement field,

```
[D] = [F] + S([F]) \approx [D']_n = [F] + S'([F])
S([F]) \approx S'([F])
S' = w_1*b_1 + w_2*b_2 + ... + w_n*b_n
```

Here we represent the displacement field in the basis B, which contains an infinite number of functions {b_0,b_1,...}.

In practice, `n` is determined by the residual of our representation `S([F]) - S([F])'` being sufficiently small.

Bounds on `n` can also be derived by using the Nyquist-Shannon theorem while taking into account the cell size and number of atoms, etc, though this may depend somewhat on the chosen basis.

The problem of representing the displacement field in the basis may be formulated as a sparse approximation problem.
Namely, consider `x` to be the vector containing all `3N` atomic coordinates (`[S]`) from above, the `j`th column of `3N x n` matrix `B` to be `b_j(x)` the evaulation of the `j`th basis function at `x`, and `w` to the vector of length `n` containing the basis function weights. 
One can then write the problem in sparse approximation form directly as
```
min ||a||_0  subject to  x = B w.
```

Since we don't expect a perfect reconstruction, one can allow some error in the representation, giving the formulation
```
min ||a||_0  subject to  ||x - B w||_2^2 <= tolerance^2.
```

This formulation suggests directly the use of classical algorithms for sparse approximation.


### Uses
In practice, one should be able to reconstruct atomic geometries by injecting pristine atomic coordinates into the sparse representation.
This would allow one to store only store bare minimum atomic cell information needed to construct the pristine atomic coordiantes, plus the basis coefficients.

The applications of such a representation are likely to be more intersting than a memory savings though.
For example, having a good sparse representation of the layer lends itself well to continuum models, where the representation would be infinitely differentiable (so long as the basis functions are).
Further, expensive operations (like geometry optimization) could now be performed on the system in the reduced basis than the raw atomic coordinates.


