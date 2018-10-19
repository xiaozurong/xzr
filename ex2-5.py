import turtle as t
def drawTriangle(e,direct=120):
    t.seth(0)
    t.fd(e)
    t.left(direct)
    t.fd(e)
    t.left(direct)
    t.fd(e)
drawTriangle(200)
