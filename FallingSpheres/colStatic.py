import bpy
import random

# variables used for "Scripting Perfectly Colliding Arrays of Spheres"
space = 3                        # edge of sphere to adjacent edge of sphere
radius = 1                       # radius of spheres
distance = space + 2 * radius    # center to center distance between spheres
height = 3                       # number of sphere layers in z-direction
depth = 1                        # number of sphere layers in y-direction
width = 1                        # number of sphere layers in x-direction (keep width value close to height value)
floor = -2 - radius              # z location of passive plane
area = depth * width * distance  # effective area of square plane

# add spheres in a single column
for z in range(height):
    bpy.ops.mesh.primitive_uv_sphere_add(location = [0, 0, z * distance])  # add primitive sphere

#  add plane under the array of spheres
bpy.ops.mesh.primitive_plane_add(location = [((width -1) * distance)/2, \
            ((depth -1) * distance)/2, floor], size = area)

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
