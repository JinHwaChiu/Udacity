import numpy as np
import pyglet
class ArmEnv(object):
    viewer = None
    def __init__(self):
        state_dim
        action_dim
        action_bound
    def step(self,action):
        pass
    def reset(self):
        pass
    def render(self):
        if viewr is None:
            viewer = Viewr()
        return viewer

class Viewer(pyglet.window.Window):
    bar_thc = 5
    def __init__(self):
        super(Viewer,self).__init__(width=400, height=400)
        pyglet.graphics.glClearColor(1,1,1,1)
        
    def render(self):
        
        pass
    def on_draw(self):
        
        pass
    def _update_arm(self):
        pass


#if __name__ == '__main__':
pyglet.app.run()