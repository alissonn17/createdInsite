import bge
from collections import OrderedDict

class scene(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self,args):
        print(bge.render.getWindowHeight())
        scene = bge.logic.getCurrentScene()

        #bge.render.enableMotionBlur(0.1)
        bge.render.showFramerate(True)
        #bge.render.setBackgroundColor([0,0,0,0])
        bge.render.setEyeSeparation(1)

    def update(self):
        pass