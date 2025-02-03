from manim import *

class TwoPlusTwoPlusTen(Scene):
    def construct(self):
        background = Rectangle(width=14, height=8, fill_color=DARK_GREY, fill_opacity=1).to_edge(LEFT)
        self.add(background)

        two_plus_two = MathTex("2 + 2").set_color(YELLOW).scale(2).shift(2*UP + 2*LEFT)
        self.play(Write(two_plus_two))

        plus_ten = MathTex("+ 10").set_color(BLUE).scale(2).next_to(two_plus_two, RIGHT)
        self.play(Write(plus_ten))

        equals = MathTex("=").set_color(GREEN).scale(2).next_to(plus_ten, RIGHT)
        self.play(Write(equals))

        four = MathTex("4").set_color(YELLOW).scale(2).next_to(two_plus_two, RIGHT)
        self.play(TransformMatchingTex(two_plus_two, four))
        self.play(FadeOut(plus_ten))
        self.play(four.animate.next_to(equals,LEFT))


        four_plus_ten = MathTex("4 + 10").set_color(ORANGE).scale(2).next_to(equals,LEFT)
        self.play(TransformMatchingTex(four, four_plus_ten[0]))
        self.play(Write(four_plus_ten[1:]))

        fourteen = MathTex("14").set_color(PINK).scale(3).next_to(four_plus_ten,RIGHT)
        self.play(TransformMatchingTex(four_plus_ten, fourteen), run_time=1)


        circle = Circle(radius=1, color=PURPLE, fill_opacity=0.5).move_to(fourteen)
        self.play(Create(circle), run_time=0.5)
        self.play(circle.animate.scale(2), run_time=0.5)
        self.play(FadeOut(circle))
        self.wait(1)

        final_answer = Tex("Therefore, 2 + 2 + 10 = 14").set_color(WHITE).scale(1.5).to_edge(DOWN)
        self.play(Write(final_answer))
        self.wait(2)