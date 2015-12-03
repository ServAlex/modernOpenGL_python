import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import numpy as np
from gloo import Program, VertexBuffer, IndexBuffer

def display():
    gl.glClearColor(1,1,1,1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    program.draw(gl.GL_TRIANGLE_STRIP)
    glut.glutSwapBuffers()

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == '\033':
        sys.exit( )

glut.glutInit(sys.argv)
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutCreateWindow('Hello world!')
glut.glutReshapeWindow(512,512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
#glut.glutTimerFunc(1000/60, timer, 60)		# takes fps parameter

program     = gl.glCreateProgram()
vertex      = gl.glCreateShader(gl.GL_VERTEX_SHADER)
fragment    = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)

vertex_code = """
	uniform float scale;
	attribute vec2 position;
	attribute vec4 color;
	varying vec4 v_color;

	void main()
	{
	    gl_Position = vec4(position*scale, 0.0, 1.0);
	    v_color = color;
	}
"""

fragment_code = """
	varying vec4 v_color;

	void main()
	{
	    gl_FragColor = v_color;
	}
"""


program = gloo.Program(vertex_code, fragment_code, count=4)
program['color']    = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
program['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]
program['scale']    = 1.0

glut.glutMainLoop()




'''
# setting shaders sources
gl.glShaderSource(vertex, vertex_code)
gl.glShaderSource(fragment, fragment_code)

# compiling shaders
gl.glCompileShader(vertex)
gl.glCompileShader(fragment)

gl.glAttachShader(program, vertex)
gl.glAttachShader(program, fragment)

gl.glLinkProgram(program)

gl.glDetachShader(program, vertex)
gl.glDetachShader(program, fragment)

gl.glUseProgram(program)

# Request a buffer slot from GPU
buffer = gl.glGenBuffers(1)

# Make this buffer the default one
gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)

# Upload data
gl.glBufferData(gl.GL_ARRAY_BUFFER, data.nbytes, data, gl.GL_DYNAMIC_DRAW)


# creating data srtucture
data = numpy.zeros(4, dtype = [ ("position", np.float32, 2),
                                ("color",    np.float32, 4)] )

# binding buffer to program
stride = data.strides[0]

offset = ctypes.c_void_p(0)
loc = gl.glGetAttribLocation(program, "position")
gl.glEnableVertexAttribArray(loc)
gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
gl.glVertexAttribPointer(loc, 3, gl.GL_FLOAT, False, stride, offset)

offset = ctypes.c_void_p(data.dtype["position"].itemsize)
loc = gl.glGetAttribLocation(program, "color")
gl.glEnableVertexAttribArray(loc)
gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
gl.glVertexAttribPointer(loc, 4, gl.GL_FLOAT, False, stride, offset)


# binding uniform
loc = gl.glGetUniformLocation(program, "scale")
gl.glUniform1f(loc, 1.0)


# setting data
data['color']    = [ (1,0,0,1), (0,1,0,1), (0,0,1,1), (1,1,0,1) ]
data['position'] = [ (-1,-1),   (-1,+1),   (+1,-1),   (+1,+1)   ]


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
    glut.glutSwapBuffers()
'''




