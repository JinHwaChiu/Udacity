import numpy as np
import pyglet
class ArmEnv(object):
    viewer = None
    def __init__(self):
        pass
    def step(self,action):
        pass
    def reset(self):
        pass
    def render(self):
        if self.viewer is None:
            self.viewer = Viewer()
        self.viewer.render()

class Viewer(pyglet.window.Window):
    bar_thc = 5
    def __init__(self):
        super(Viewer,self).__init__(width=400,height=400,resizable=False,caption='Arm')
        pyglet.gl.glClearColor(1,1,1,1)
        self.batch = pyglet.graphics.Batch()
         # 添加蓝点
        self.point = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [50, 50,                # x1, y1
                     50, 100,               # x2, y2
                     100, 100,              # x3, y3
                     100, 50]),             # x4, y4
            ('c3B', (86, 109, 249) * 4))    # color

        # 添加一条手臂
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,              # 同上, 点信息
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (249, 86, 86) * 4,))    # color

    def render(self):
        self._update_arm()
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()
        
    def on_draw(self):
        self.clear()
        self.batch.draw()
    def _update_arm(self):
        pass

if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()