##tile to blend python import script 0.1

def newLine (x, y, z):
	print 'x=%d y=%d z=%d' %(x,y,z)

def printBlock (x, y, z):
	
	newBlock = 'bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, 
	location=(x, y, z), layers=(True, False, False, False, False, False, False, False, 
	False, False, False, False, False, False, False, False, False, False, False, False))'

	
file = open('level.map', 'r');

mapH = 40;
mapW = 40;
count = 0;

arrCubeData = [
	'bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, 
	location=(x, y, z), layers=(True, False, False, False, False, False, False, False, 
	False, False, False, False, False, False, False, False, False, False, False, False))',
	'bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, 
	location=(x, y, z), layers=(True, False, False, False, False, False, False, False, 
	False, False, False, False, False, False, False, False, False, False, False, False))',
	'bpy.ops.mesh.primitive_cube_add(radius=1, view_align=False, enter_editmode=False, 
	location=(x, y, z), layers=(True, False, False, False, False, False, False, False, 
	False, False, False, False, False, False, False, False, False, False, False, False))']

for line in file:
	arrLine = line.split(',')
	for cube in arrLine:
		if count == mapW - 1 :
			print "NEW LINE"
			newLine(10, 22, 33)
			count = 0
		print arrCubeData[int(cube)]
	count += 1
		
file.close

