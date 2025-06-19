import bpy
import sys

# Get user inputs from the command line
input_args = sys.argv
rooms = int(input_args[input_args.index("--") + 1])  # e.g., number of rooms
floors = int(input_args[input_args.index("--") + 2])  # e.g., number of floors

# Clear existing objects
bpy.ops.wm.read_factory_settings(use_empty=True)

# Example: Generate a basic structure (add cubes for rooms/floors)
for floor in range(floors):
    for room in range(rooms):
        bpy.ops.mesh.primitive_cube_add(size=2, location=(room * 3, 0, floor * 3))

# Set the camera
bpy.ops.object.camera_add(location=(10, -10, 10))
camera = bpy.context.object
camera.rotation_euler = (1.1, 0, 0.7)
bpy.context.scene.camera = camera

# Set lighting
bpy.ops.object.light_add(type='SUN', location=(10, -10, 15))

# Render the image
output_path = sys.argv[input_args.index("--") + 3]  # Output file path
bpy.context.scene.render.filepath = output_path
bpy.ops.render.render(write_still=True)
