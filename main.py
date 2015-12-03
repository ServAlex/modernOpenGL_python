import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    glut.glutSwapBuffers()

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

def keyboard( key, x, y ):
    if key == '\033':
        sys.exit( )

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
glut.glutCreateWindow('Hello world!')
glut.glutReshapeWindow(512,512)
glut.glutReshapeFunc(reshape)
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(keyboard)
glut.glutMainLoop()


program     = gl.glCreateProgram()
vertex      = gl.glCreateShader(gl.GL_VERTEX_SHADER)
fragment    = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)

vertex_code = """

"""

fragment_code = """

"""

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












