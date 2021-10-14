
## `sheetSparse`
Represent atomistic sheet geometries in a reduced basis using sparse approximation.

### Theory
All discrete objects are written in brackets, continuum objects are unadorned, the Lagrangian description of continuum mechanics is used throughout.

A flat sheet of graphene is considered to have pristine discrete coordinates `[P]` defined solely by the lattice vectors and atomic basis.

Given some deformed configuration of `[P]` called `[D]`, one can partition `[D]` into the pristine coordinates plus the evaluation of some continuum displacement field `S` at the points in `[P]`.

```
[D] = [P] + S([P]) 
```
noting that `S([P])` is a disrcete quantity.

We then seek to approximate the deformed configuration `[D]` by making use of some basis functions for the displacement field as a function of the undeformed state.

```
[D] = [P] + S([P]) \approx [D']_n = [P] + S'([P])
S([P]) \approx S'([P])
S' = w_1*b_1 + w_2*b_2 + ... + w_n*b_n
```

Here we represent the displacement field in the basis `B`, which contains an infinite number of functions `{b_0,b_1,...}`.

In practice, `n` is determined by the residual of our representation `S([P]) - S([P])'` being sufficiently small.

Bounds on `n` can also be derived by using the Nyquist-Shannon theorem while taking into account the cell size and number of atoms, etc, though this may depend somewhat on the chosen basis.

The problem of representing the displacement field in the basis may be formulated as a sparse approximation problem.
Namely, consider `x` to be the vector containing all `3N` atomic displacements (`S([P])`) from above, the `j`th column of `3N x n` matrix `B` to be `b_j(x)` the evaulation of the `j`th basis function at the pristine coordinates `[P]`, and `w` to the vector of length `n` containing the basis function weights. 
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

The applications of such a representation are likely to be more interesting than a memory savings though.
For example, having a good sparse representation of the layer lends itself well to continuum models, where the representation would be infinitely differentiable (so long as the basis functions are).
Further, expensive operations (like geometry optimization) could now be performed on the system in the reduced basis than the raw atomic coordinates.


### Implementation
**A note on mapping**

Given an `n`-D parallelepiped domain defined by the `n` columns of matrix `V`, one would like to map back to the unit `n`-cube, where basis functions are more easily defined.
Let `L` be the mapping from unit `n`-cube basis (the indentity) to the parallelepiped basis.
```
L I = V  --> L = V.
```
The inverse of `L` is then a linear map from the parallelepiped basis to the `n`-cube basis
```
L^{-1} V = I.
```
Imagine one has the basis function `g(v)` defined over coordinates in the unit `n`-cube and seeks the mapping of this function `f(x)` onto the parallelepiped coordinates `x`.
Then
```
f(x) = g(L^{-1} x).
```
Mechanically, this is done be reverting the parallelepiped coordinates to the unit `n`-cube with the inverse, then computing the basis function values.
However, since the final sparse representation should be in terms of coefficients of functions over parallelepiped coordinates, it is useful to consider an example of what said basis functions would look like.
Consider the real cosine basis functions in `n` dimensions as an example.
The general form of a function from this basis is
```
b(x) = PROD_{d=1}^{n} cos(2*pi*v_d*k_d)
     = PROD_{d=1}^{n} cos(2*pi*(L^{-1} x)_d*k_d)
     = PROD_{d=1}^{n} cos(2*pi*(L^{-1}[d,:] \cdot x)*k_d)
```

**Basis pursuit**: construct real space basis functions over the parallelepiped domain as atoms in dictionary, then proceed as usual with matching pursuit

## Resources
- [sparse representation of point cloud data with learned dictionaries](https://www.researchgate.net/publication/311668564_Cloud_Dictionary_Sparse_Coding_and_Modeling_for_Point_Clouds#pf2)

