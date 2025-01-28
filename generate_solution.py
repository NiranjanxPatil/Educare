from manim import *

class MathProblemSolution(Scene):
    def construct(self):
        background = BackgroundRectangle(fill_color=DARK_GRAY, fill_opacity=1)
        self.add(background)

        equation = MathTex("2 + 7 + 8 = ?").set_color(YELLOW).scale(2)
        self.play(Write(equation))
        self.wait(1)

        two = Circle(radius=0.5, color=BLUE).next_to(equation[0:1], DOWN, buff=0.5)
        seven = Circle(radius=0.5, color=GREEN).next_to(equation[3:4], DOWN, buff=0.5)
        eight = Circle(radius=0.5, color=RED).next_to(equation[6:7], DOWN, buff=0.5)

        self.play(Create(two),Create(seven),Create(eight))
        self.wait(1)

        two_text = Tex("2").set_color(BLUE).move_to(two.get_center())
        seven_text = Tex("7").set_color(GREEN).move_to(seven.get_center())
        eight_text = Tex("8").set_color(RED).move_to(eight.get_center())

        self.play(Transform(two, two_text), Transform(seven, seven_text), Transform(eight, eight_text))
        self.wait(1)

        two_seven = MathTex("2 + 7 = 9").set_color(GOLD).to_edge(UP)
        self.play(Write(two_seven))
        self.wait(1)


        nine = Circle(radius=0.5, color=GOLD).next_to(two_seven, DOWN, buff=0.5)
        nine_text = Tex("9").set_color(GOLD).move_to(nine.get_center())
        self.play(Create(nine))
        self.play(Transform(nine, nine_text))
        self.wait(1)

        nine_eight = MathTex("9 + 8 = 17").set_color(PURPLE).to_edge(UP)
        self.play(TransformMatchingTex(two_seven, nine_eight), FadeOut(nine_text))
        self.wait(1)

        seventeen = MathTex("17").set_color(PURPLE).scale(2).next_to(equation, RIGHT, buff=1)
        self.play(Write(seventeen))
        self.wait(1)

        final_equation = MathTex("2 + 7 + 8 = 17").set_color(WHITE).scale(2)
        self.play(TransformMatchingTex(equation, final_equation), FadeOut(two_seven))
        self.wait(2)