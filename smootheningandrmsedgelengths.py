import bpy
import math

# Ensure you have an active object selected
active_object = bpy.context.active_object
if active_object is None:
    raise ValueError("No active object selected. Please select the object you want to smooth.")

# Function to calculate RMS of edge lengths
def calculate_rms_edge_lengths(object):
    edge_lengths = []
    for edge in object.data.edges:
        v1 = object.data.vertices[edge.vertices[0]]
        v2 = object.data.vertices[edge.vertices[1]]
        edge_length = (v1.co - v2.co).length
        edge_lengths.append(edge_length)
    return math.sqrt(sum(x**2 for x in edge_lengths) / len(edge_lengths))

# Calculate RMS of edge lengths before smoothing
before_rms = calculate_rms_edge_lengths(active_object)

# Switch to Edit Mode
bpy.ops.object.mode_set(mode='EDIT')

# Select all vertices
bpy.ops.mesh.select_all(action='SELECT')

# Apply the "Smooth" operation
bpy.ops.mesh.vertices_smooth(factor=1, repeat=10)

# Switch back to Object Mode
bpy.ops.object.mode_set(mode='OBJECT')

# Calculate RMS of edge lengths after smoothing
after_rms = calculate_rms_edge_lengths(active_object)

# Compute the change in RMS
score = after_rms / before_rms

# Print the scores
print(f"Smoothing complete for the active object: {active_object.name}")
print(f"RMS Edge Lengths Before Smoothing: {before_rms:.4f}")
print(f"RMS Edge Lengths After Smoothing: {after_rms:.4f}")
print(f"Smoothness Change (RMS After/Before): {score:.4f}")
