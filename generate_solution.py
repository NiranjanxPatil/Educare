from manim import *

class SquareArea(Scene):
    def construct(self):
        square = Square(side_length=2, color=BLUE)
        square.set_fill(BLUE, opacity=0.5)
        side_length = MathTex("2").next_to(square, UP, buff=0.2).scale(1.5).set_color(YELLOW)
        side_length_label = Tex("cm").next_to(side_length, RIGHT, buff=0.1).set_color(YELLOW)

        area_text = MathTex("Area = side \\times side").to_edge(UP).set_color(GREEN)
        area_equation = MathTex("Area = 2 \\times 2").next_to(area_text, DOWN, buff=1).set_color(GREEN)
        area_result = MathTex("Area = 4").next_to(area_equation, DOWN, buff=0.5).set_color(GREEN).scale(1.5)
        area_unit = Tex("cm$^2$").next_to(area_result, RIGHT, buff=0.1).set_color(GREEN)

        self.play(Create(square))
        self.play(Write(side_length), Write(side_length_label))
        self.wait(1)

        self.play(Write(area_text))
        self.wait(1)
        self.play(Write(area_equation))
        self.wait(1)
        self.play(Transform(area_equation, area_result))
        self.play(Write(area_unit))

        self.play(square.animate.scale(1.2).set_color(RED), rate_func=wiggle)
        self.wait(1)
        self.play(square.animate.scale(1/1.2).set_color(BLUE), rate_func=smooth)
        self.wait(1)

        self.play(Indicate(area_result), Indicate(area_unit))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])