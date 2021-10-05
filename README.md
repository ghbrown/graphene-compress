
Domain specific compression of deformed atomistic sheet geometries.

### Theory
All discrete objects are written in brackets, continuum objects are unadorned.

A flat sheet of graphene is considered to have pristine discrete coordinates [F] defined solely by the lattice vectors and atomic basis.
[F] will be an implict part of the final representation as explained below.

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

By the Nyquist-Shannon sampling theorem, `n` may be strictly upper bounded by `2 sqrt(N)` where ``N` is the number of atoms.
Clear this is a compressed representation compared to `3N` for coordinate storage.

### Uses
Optimize in reduced basis.
