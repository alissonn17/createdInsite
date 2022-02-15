import bge
from collections import OrderedDict

from mathutils import Vector, noise
import random

class Terrain(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        mesh = self.object.meshes[0]
        
        #gera terreno
        
        for index in range(mesh.getVertexArrayLength(0)):
            vertex = mesh.getVertex(0, index)
            
            #pra varios objs do mundo
            pos = self.object.worldTransform * vertex.XYZ
            #pra um so obj
            #pos = vertex.XYZ
            
            vertex.z = noise.hetero_terrain(pos * 0.02, 1.0, 200.0, 8.0, 1.0) * 20.0
            
            if random.random() > 0.90:
                last = self.object.scene.addObject("prop")
                last.worldPosition = self.object.worldTransform * vertex.XYZ
            
        #atualiza iluminação
        for poly in mesh.polygons:
            v1 = mesh.getVertex(0, poly.v1).XYZ - mesh.getVertex(0, poly.v2).XYZ
            v2 = mesh.getVertex(0, poly.v3).XYZ - mesh.getVertex(0, poly.v2).XYZ
            
            for vertex in poly.vertices:
                vertex.normal = v2.cross(v1).normalized()
                
        self.object.reinstancePhysicsMesh()

    def update(self):
        pass
