import bpy

armature_path = "D:\PES\Capstone\Testing\Blender trials\Auto_Rigging\skeleton_a_pose.fbx"
mesh_path = "D:\PES\Capstone\Testing\Blender trials\Auto_Rigging\casual-adult-with-baffled-expression_256.obj"
output_blend_file_path = "D:\PES\Capstone\Testing\Blender trials\Auto_Rigging\Output1.blend"
output_fbx_file_path = "D:\PES\Capstone\Testing\Blender trials\Auto_Rigging\Output1.fbx"

# Create a new Blender file with all default objects removed
bpy.ops.wm.read_factory_settings(use_empty=True)

#import fbx
bpy.ops.import_scene.fbx(filepath=armature_path)

# Select the armature
armature = bpy.context.selected_objects[0]
bpy.context.view_layer.objects.active = armature
bpy.ops.object.posemode_toggle()

# Import the mesh
bpy.ops.import_scene.obj(filepath=mesh_path)

# Select the mesh
mesh = bpy.context.selected_objects[0]

# Switch back to Object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Select the armature again
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Parent the armature to the mesh
bpy.ops.object.parent_set(type='ARMATURE_AUTO')

# Switch back to Object mode
bpy.ops.object.mode_set(mode='OBJECT')

# Save as Blender file (.blend)
bpy.ops.wm.save_as_mainfile(filepath=output_blend_file_path)

# Switch back to Pose mode
bpy.ops.object.mode_set(mode='POSE')

# Save as FBX file (.fbx)
bpy.ops.export_scene.fbx(filepath=output_fbx_file_path, use_selection=True)

# Switch back to Object mode
bpy.ops.object.mode_set(mode='OBJECT')
