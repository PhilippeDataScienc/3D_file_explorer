import pyvistaqt
import pyvista as pv
import numpy as np

# Chargez le fichier STL
mesh = pv.read('./3D_data/tubulure.stl')
viewup = [0, 1, 1]

p = pyvistaqt.BackgroundPlotter()
p.add_mesh(mesh)
p.show()
path = p.generate_orbital_path(factor=2.0, n_points=36, viewup=viewup, shift=0.2)
p.open_gif("orbital_trajectory_for_stl.gif")
p.orbit_on_path(path, write_frames=True, viewup=viewup, step=0.05)
p.close()