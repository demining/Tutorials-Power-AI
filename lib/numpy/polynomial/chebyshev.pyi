from typing import Any

from numpy import int_
from numpy.typing import NDArray
from numpy.polynomial._polybase import ABCPolyBase
from numpy.polynomial.polyutils import trimcoef

__all__: list[str]

chebtrim = trimcoef

def poly2cheb(pol): ...
def cheb2poly(c): ...

chebdomain: NDArray[int_]
chebzero: NDArray[int_]
chebone: NDArray[int_]
chebx: NDArray[int_]

def chebline(off, scl): ...
def chebfromroots(roots): ...
def chebadd(c1, c2): ...
def chebsub(c1, c2): ...
def chebmulx(c): ...
def chebmul(c1, c2): ...
def chebdiv(c1, c2): ...
def chebpow(c, pow, maxpower=...): ...
def chebder(c, m=..., scl=..., axis=...): ...
def chebint(c, m=..., k = ..., lbnd=..., scl=..., axis=...): ...
def chebval(x, c, tensor=...): ...
def chebval2d(x, y, c): ...
def chebgrid2d(x, y, c): ...
def chebval3d(x, y, z, c): ...
def chebgrid3d(x, y, z, c): ...
def chebvander(x, deg): ...
def chebvander2d(x, y, deg): ...
def chebvander3d(x, y, z, deg): ...
def chebfit(x, y, deg, rcond=..., full=..., w=...): ...
def chebcompanion(c): ...
def chebroots(c): ...
def chebinterpolate(func, deg, args = ...): ...
def chebgauss(deg): ...
def chebweight(x): ...
def chebpts1(npts): ...
def chebpts2(npts): ...

class Chebyshev(ABCPolyBase):
    @classmethod
    def interpolate(cls, func, deg, domain=..., args = ...): ...
    domain: Any
    window: Any
    basis_name: Any
