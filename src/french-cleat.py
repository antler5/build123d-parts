# SPDX-FileCopyrightText: 2024 antlers <antlers@illucid.net>
# SPDX-License-Identifier: GPL-3.0-only

# SPDX-FileCopyrightText: 2022 James Martin
# SPDX-License-Identifier: CC-BY-4.0

#\ Based on JWM85's [[https://www.thingiverse.com/thing:5430865][French Cleat Mounts]].
# %% Imports %%
import copy
import math
from build123d import *
from ocp_vscode import *

# %% Viewer defaults
set_defaults(reset_camera=Camera.CENTER)

# %% French Cleat

length = 152.4 # 6in
height = 20
thickness = 3.2
overlap = 5
num_toofs = 6
toofs_width = height / num_toofs
toofs_height = 0.65

cleat = Rectangle(
  thickness, height,
  align=(Align.CENTER,Align.MIN,Align.CENTER)
)
cleat += (
  Pos(thickness,height-overlap)
  * Rectangle(
      thickness, 0.80 * height,
      align=(Align.CENTER,Align.MIN,Align.CENTER))
)

cleat = fillet(cleat.vertices()[2], 2)
cleat = fillet(cleat.vertices()[4:6], 1.55)
cleat = fillet(cleat.vertices()[9], 2)
cleat = fillet(cleat.vertices()[11], 1)

# Toofs
toofs = []
gap = 1
toof_shape = Rot(0,0,90) * mirror(
  Trapezoid(toofs_width-gap, toofs_height,
            50,
            align=(Align.MIN,Align.MIN,Align.CENTER)),
  Plane.XZ)
for i in range(0,num_toofs):
  toofs += [Pos(-thickness/2,i*toofs_width+gap/2)
            * copy.copy(toof_shape)]
  
cleat -= toofs
cleat = extrude(cleat, length)

# Screws
offset = 7.5
# Template aligned on X/Y
screwholes_shape = (
  Plane.YZ.offset(thickness/2-0.33)
  * Pos(height/3.3)
  * CounterSinkHole(1.8,2.25,thickness,90)
)
# Instantiate across Z-positions
screwholes = Pos(0,0,offset) * copy.copy(screwholes_shape)
screwholes += Pos(0,0,length-offset) * copy.copy(screwholes_shape)
cleat -= screwholes

reset_show()
show_object(cleat)

# %% Exports
export_step(cleat, "STEPs/french-cleat.step")
export_stl(cleat, "STLs/french-cleat.stl")
