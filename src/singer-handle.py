# SPDX-FileCopyrightText: 2024 antlers <antlers@illucid.net>
# SPDX-License-Identifier: GPL-3.0-or-later

#\ A handle for my partner's Singer sewing machine.
#\ The original wooden handle wore through.
#\ Not sure how long the filament will last, tbh.

# %% Imports
from build123d import *
from ocp_vscode import *

# %% Viewer defaults
set_defaults(reset_camera=Camera.CENTER)

# %% Singer Handle
_acc = 0
def acc(n):
  global _acc
  _acc += n
  return _acc

thickness = 1.85

initialRadius    = 12.72 / 2 - 0.05
penInitialRadius = 12.72 / 2
minRadius        = 9.1 / 2
minOffset        = acc(12.15)
maxRadius        = 19 / 2
maxOffset        = acc(22)
finalRadius      = 13.33 / 2
finalOffset      = acc(12.75 + 1.75)

outer_edge = Spline(
    (initialRadius, 0),
    (penInitialRadius, 0.0125),
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

# Punch out stem
stem = extrude(Circle(initialRadius - 2 * thickness), finalOffset)

# Split in half
top = split(s, Plane.XZ, keep=Keep.TOP) - stem
bottom = split(s, Plane.XZ, keep=Keep.BOTTOM) - stem

l = Rot(90, 0, 0) * outer_edge
l1 = Spline(l @ 0.6, l @ 0.7, l @ 0.8)
l2 = Spline(l @ 0.2, l @ 0.3, l @ 0.4)

# Pegs
offset = 5.25
line = Line([(offset,0,0),(offset,0,finalOffset)])

pegs = [
  # Point, Radius, Height
  (               line @ 0.05,  1.5,  3.00),
  (Pos(0.4,0,0) * line @ 0.65,  1.7,  3.75),
  (Pos(1,0,0)   * line @ 0.775, 2,    4.75),
  (Pos(0.5,0,0) * line @ 0.9,   1.7,  4.00)
]

diff = 0.1
thin_points = [Location(p) * extrude(Circle(r-diff).rotate(Axis.X, -90), h-(2*diff)) for p,r,h in pegs]
thin_points += [p.mirror(Plane.ZY) for p in thin_points]
thin_points = [fillet(p.edges()[2], 0.5+diff) for p in thin_points]
top += thin_points

thick_points = [Location(p) * extrude(Circle(r).rotate(Axis.X, -90), h) for p,r,h in pegs]
thick_points += [p.mirror(Plane.ZY) for p in thick_points]
thick_points = [fillet(p.edges()[2], 0.5-diff) for p in thick_points]
bottom -= thick_points

boxes = Pos(0,-maxRadius - 2,maxOffset) * Box(15,5,30)
boxes = [boxes, boxes.mirror(Plane.XZ)]
top -= boxes
bottom -= boxes

reset_show()
show_object(top)
show_object(bottom)

# %% Exports
export_step(top, "../STEPs/singer-handle-top.step")
export_stl(top, "../STLs/singer-handle-top.stl")
export_step(bottom, "../STEPs/singer-handle-bottom.step")
export_stl(bottom, "../STLs/singer-handle-bottom.stl")
