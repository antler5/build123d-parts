# %%
from build123d import *
from ocp_vscode import *

_acc = 0
def acc(n):
  global _acc
  _acc += n
  return _acc

thickness = 1.85

initialRadius = 12.72 / 2
minRadius     = 9.1 / 2
minOffset     = acc(12.15)
maxRadius     = 19 / 2
maxOffset     = acc(22)
finalRadius   = 13.33 / 2
finalOffset   = acc(12.75)

outer_edge = Spline(
    (initialRadius, 0),
    (minRadius, minOffset),
    (maxRadius, maxOffset),
    (finalRadius, finalOffset),
)
s = outer_edge

# Close off ends
s += Line(s @ 1, (0, finalOffset))
s += Line(s @ 0, (0, 0))
s += Line((0, finalOffset), (0, 0))

# Revolve & Hollow out
s = Plane.XZ * make_face(s)
s = revolve(s, Axis.Z)
s -= offset(s, -thickness)

# # Punch ends back out
# s -= extrude(Circle(initialRadius + thickness), thickness)
# s -= Pos(0,0,finalOffset) * extrude(Circle(finalRadius + thickness), -thickness)

# Split in half
top = split(s, Plane.XZ, keep=Keep.TOP)
bottom = split(s, Plane.XZ, keep=Keep.BOTTOM)

l = Rot(90, 0, 0) * outer_edge
l1 = Spline(l @ 0.6, l @ 0.7, l @ 0.8)
l2 = Spline(l @ 0.2, l @ 0.3, l @ 0.4)

reset_show()
show_object(top)
# show_object(bottom)
# export_step(top, "top.step")
# export_step(bottom, "bottom.step")
# %%
