import bpy
import random

# variables used for "Scripting Perfectly Colliding Arrays of Spheres"
space = 3                        # edge of sphere to adjacent edge of sphere
radius = 1                       # radius of spheres
distance = space + 2 * radius    # center to center distance between spheres
height = 5                       # number of sphere layers in z-direction
depth = 4                        # number of sphere layers in y-direction
width = 4                        # number of sphere layers in x-direction (keep width value close to height value)
floor = -2 - radius              # z location of passive plane
area = depth * width * distance  # effective area of square plane

# add spheres in height, depth and width for loops
for z in range(height):
    for y in range(depth):
        for x in range(width):
            bpy.ops.mesh.primitive_uv_sphere_add(location = [x * distance, y * distance, z * distance])  # add primitive sphere
            # add the sphere objects to rigidbody physics 
            bpy.ops.rigidbody.object_add()                # Add selected objects as Rigid Bodies
            bpy.context.object.rigid_body.type = 'ACTIVE' # role of body (Moving)
            # shape the collision
            bpy.context.object.rigid_body.collision_shape = 'SPHERE'  # 'SHAPE'; of collisions; others: 'MESH', 'CONE',
            # add bounciness to object
            bpy.context.object.rigid_body.restitution = 1             # 'BOUNCINESS' - tendency to bounce (0 -> 1)
    
#  add plane under the array of spheres
bpy.ops.mesh.primitive_plane_add(location = [((width -1) * distance)/2, \
            ((depth -1) * distance)/2, floor], size = area)
            
# add the plane object to rigidbody physics
bpy.ops.rigidbody.object_add()                   # Add selected objects as Rigid Bodies
bpy.context.object.rigid_body.type = 'PASSIVE'   # role of body (Rigid)

# generate and return random color function
def get_random_color():
    ''' generate rgb using a list comprehension '''
    r, g, b = [random.random() for i in range(3)]
    return r, g, b, 1

#randomly color objects in dataset
for obj in bpy.data.objects:
    mat =  bpy.data.materials.new(name="Material_" + str(obj)) #set new material to variable
    obj.data.materials.append(mat)
    mat.diffuse_color = get_random_color()
# deselect all objects
bpy.ops.object.select_all(action = 'DESELECT')
