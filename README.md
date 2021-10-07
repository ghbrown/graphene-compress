
## `sheetSparse`
Represent atomistic sheet geometries in a reduced basis using sparse approximation.

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


### Implementation
**Discrete Cosine Transform**: One possible way to extract the reduced the reduced basis representation is by transforming the displacement field into a rectangular array with "channels", which can then be likened to images, themselves amenable to standard image compression techniques.
For example the displacement between the pristine lattice and distorted lattices
```
                 (pristine)                         (distorted)
          .___________.___________.          .___________.___________.
         /   (b_3)   /   (b_4)   /          / (b_3)     /     (b_4) /
        /           /           /          /           /           /
       /  (a_3)    /  (a_4)    /          /    (a_3)  /  (a_4)    /
      /___________/___________/          /___________/___________/
     /   (b_1)   /   (b_2)   /          /   (b_1)   / (b_2)     /
    /           /           /          /           /           /
   /  (a_1)    /  (a_2)    /          /  (a_1)    /  (a_2)    /
  /___________/___________/          /___________/___________/
```
could be represented in the following rectangular arrays
```
         _                                        _
 S_x =  |  s_x_(a_1) s_x_(b_1) s_x_(a_2) s_x_(b_2) |
        |  s_x_(a_3) s_x_(b_3) s_x_(a_4) s_x_(b_4) |
         _                                        _
         _                                        _
 S_y =  |  s_y_(a_1) s_y_(b_1) s_y_(a_2) s_y_(b_2) |
        |  s_y_(a_3) s_y_(b_3) s_y_(a_4) s_y_(b_4) |
         _                                        _
         _                                        _
 S_z =  |  s_z_(a_1) s_z_(b_1) s_z_(a_2) s_z_(b_2) |
        |  s_z_(a_3) s_z_(b_3) s_z_(a_4) s_z_(b_4) |
         _                                        _
```
where each mode of the array corresponds to one basis vector, and the atomic basis is injected along a single mode.
In general, the array (for a single dimension) is then of shape `(n_lat_vec_1*atomic_basis_size, n_lat_vec_2, ..., n_lat_vec_m)` for a lattice in `m` dimensions, assuming the atomic basis has been injected along the first mode.

One can then appeal directly to methods like the discrete cosine transform, since the atomic information has been neatly packaged into the appropriate form.

**WILL THIS CAUSE ISSUES WHEN ATTEMPTING TO RECOVER THE REAL SPACE FUNCTION SINCE DCT ASSUMES UNIFORM SPACING???**

**REQUIRES ATOM LABELS/KNOWN ORDERING RELATIVE TO PRISTINE LATTICE**

**Basis pursuit**: retain real space structure, construct real space basis functions 

