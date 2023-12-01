import bpy

# Get the active object (the currently selected object)
active_object = bpy.context.active_object

# Check if the active object exists (not None)
if active_object and active_object.type == 'MESH':
    print("The active object is:", active_object.name)

    # Calculate the area of the model before cleaning
    original_area = sum(polygon.area for polygon in active_object.data.polygons)

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select the active object
    active_object.select_set(True)
    bpy.context.view_layer.objects.active = active_object

    # Enter Edit Mode
    bpy.ops.object.mode_set(mode='EDIT')

    # Select all geometry
    bpy.ops.mesh.select_all(action='SELECT')

    # Separate loose parts into individual objects
    bpy.ops.mesh.separate(type='LOOSE')

    # Exit Edit Mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Calculate the area of the portion cleaned
    cleaned_area = sum(polygon.area for polygon in active_object.data.polygons)

    # Metric
    print("Area of the model before cleaning:", original_area)
    print("Area of the connected portion:", cleaned_area)
    print("Area of disstorted portion:",original_area-cleaned_area)
    print("Ratio of connected to orginal",cleaned_area/original_area)

    # Remove the disconnected objects
    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.name != active_object.name:
            bpy.data.objects.remove(obj)

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
else:
    print("No valid active object selected.")
