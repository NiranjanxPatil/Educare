from manim import *

class CylinderVolume(Scene):
    def construct(self):
        self.camera.background_color = DARK_GRAY

        title = Tex("Cylinder Volume Calculation", color=YELLOW).scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        r_text = MathTex(r"r = 2").set_color(BLUE).scale(1.2)
        h_text = MathTex(r"h = 8").set_color(GREEN).scale(1.2)
        self.play(Write(r_text), Write(h_text))
        r_text.to_edge(UL)
        h_text.next_to(r_text, DOWN)
        self.wait(1)

        cylinder = Cylinder(radius=2, height=8, fill_opacity=0.7, fill_color=BLUE_C)
        self.play(Create(cylinder))
        self.wait(1)

        formula = MathTex(r"V = \pi r^2 h").set_color(YELLOW).scale(1.2)
        formula.next_to(h_text, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(1)

        substitution = MathTex(r"V = \pi (2)^2 (8)").set_color(GOLD).scale(1.2)
        substitution.next_to(formula, DOWN, buff=1)
        self.play(TransformMatchingTex(formula.copy(), substitution))
        self.wait(1)

        calculation = MathTex(r"V = 32\pi").set_color(PURPLE).scale(1.2)
        calculation.next_to(substitution, DOWN, buff=1)
        self.play(TransformMatchingTex(substitution.copy(), calculation))
        self.wait(1)


        approx = MathTex(r"V \approx 100.53").set_color(PINK).scale(1.2)
        approx.next_to(calculation, DOWN, buff=1)
        self.play(Write(approx))
        self.wait(2)

        self.play(FadeOut(r_text), FadeOut(h_text), FadeOut(formula), FadeOut(substitution), FadeOut(calculation), FadeOut(approx), FadeOut(cylinder))
        self.wait(1)


        final_answer = MathTex("V \\approx 100.53 \\text{ cubic units}", color=WHITE).scale(1.5)
        self.play(Write(final_answer))
        self.wait(3)