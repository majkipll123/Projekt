class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            # draw a line using the default color
            Line(points=(x1, y1, x2, y2, x3, y3))
            Color(1, 0, 0, .5, mode='rgba')
            Rectangle(pos=self.pos, size=self.size)
        with self.canvas.before:
            Color(1, 0, .4, mode='rgb')

