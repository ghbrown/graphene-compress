
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
S' = w_o*b_0 + w_1*b_1 + ... + w_n*b_n
```

Here we represent the displacement field in the basis B, which contains an infinite number of functions {b_0,b_1,...}.

In practice, the method used to compress `[D]` (really `[S]`) will select `n` by terminating the compression after `norm(S([F]) - S'([F])_n) < tolerance`.
Bounds on `n` can also be derived by using the Nyquist-Shannon theorem while taking into accound the cell size and number of atoms, etc.

The problem of representing the displacement field in the basis may be formulated as a sparse approximation problem.
Namely, consider `x` to be the vector containing all `3N` atomic coordinates (`[S]`) from above, the `j`th column of `3N x n` matrix `B` to be the evaulation of the `j`th basis function at `x`, and `w` to the vector of length `n` containing the basis function weights. 
One can then write the problem in sparse approximation form directly as
```
min ||a||_0  subject to  x = D w.
```

Since we don't expect a perfect reconstruction, one can allow some error in the representation, giving the formulation
```
min ||a||_0  subject to  ||x - D w||_2^2 <= tolerance^2.
```

This formulation suggests directly the use of classical algorithms for sparse approximation.


### Uses
In practice, one should also be able to reconstruct atomic geometries by injecting pristine atomic coordinates into the sparse representation.

Having such a sparse representation of the layer lends itself well to continuum models, where the representation would be infinitely differentiable (so long as the basis functions are).

Such a reduced basis could also allow more efficient operations on the system, like geometry optimization, which may now be performed in terms of reduced basis coefficients rather than the raw atomic coordinates.


