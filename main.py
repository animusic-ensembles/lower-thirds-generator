from manim import *
import csv

def convert(x, y):
    x1 = (x - 960) / 135
    y1 = (540 - y) / 135
    return [x1, y1, 0]
def abs_convert(x):
    return x / 135

with open('setlist.csv', 'r', encoding='utf-8') as file:
    data = list(csv.reader(file))

class LowerThird(Scene):

    def construct(self):
        for line in data:
            self.next_section(line[0])
            self.generate(line[0], line[1])

    def generate(self, title_text, subtitle_text):
        line = Line(start=convert(100, 900), end=convert(100, 900))
        line.set_stroke(color=WHITE, width=10)
        line.generate_target()
        line.target.put_start_and_end_on(convert(100, 820), convert(100, 980))
        with register_font('fonts/Roboto-Regular.ttf'):
            title = Text(title_text, font="Roboto", height=abs_convert(60), fill_opacity=0).move_to(convert(-80, 900-30), aligned_edge=LEFT)

        with register_font('fonts/Roboto-Light.ttf'):
            subtitle = Text(subtitle_text, font="Roboto", height=abs_convert(40), fill_opacity=0).move_to(convert(-80, 900+40), aligned_edge=LEFT)
                
        overlay = Rectangle(color=BLACK, height=abs_convert(160), width=abs_convert(100)).move_to(convert(40, 900))
        overlay.set_fill(color=BLACK, opacity=1)

        title.generate_target()
        title.target.set_fill(opacity=1)
        title.target.move_to(convert(150, 900-30), aligned_edge=LEFT)
        subtitle.generate_target()
        subtitle.target.set_fill(opacity=1)
        subtitle.target.move_to(convert(150, 900+40), aligned_edge=LEFT)

        self.add(line)
        self.play(MoveToTarget(line))
        self.add(title)
        self.add(subtitle)
        self.add(overlay)
        self.play(MoveToTarget(title), MoveToTarget(subtitle))
        self.wait(2)

        title.generate_target()
        title.target.set_fill(opacity=0)
        title.target.move_to(convert(-80, 900-30), aligned_edge=LEFT)
        subtitle.generate_target()
        subtitle.target.set_fill(opacity=0)
        subtitle.target.move_to(convert(-80, 900+40), aligned_edge=LEFT)
        line.generate_target()
        line.target.put_start_and_end_on(convert(100, 900), convert(100, 900))
        self.play(MoveToTarget(title), MoveToTarget(subtitle))
        self.play(MoveToTarget(line))