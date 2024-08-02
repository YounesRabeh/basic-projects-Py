from manim import *

class VectorSum(Scene):
    def construct(self):
        # Create vectors
        v_arrow = Arrow(ORIGIN, RIGHT, color=BLUE)
        v_label = Mobject("v").next_to(v_arrow.get_end(), UP)

        w_arrow = Arrow(ORIGIN, UP, color=RED)
        w_label = Mobject("w").next_to(w_arrow.get_end(), RIGHT)

        # Position the second vector relative to the first one
        w_arrow.next_to(v_arrow, UP+RIGHT, buff=0)

        # Display vectors
        self.play(Create(v_arrow), Write(v_label))
        self.play(Create(w_arrow), Write(w_label))
        self.wait(1)

        # Draw the resultant vector
        s_arrow = Arrow(ORIGIN, UP+RIGHT, color=GREEN)
        s_label = Mobject("s").next_to(s_arrow.get_end(), UP+RIGHT)
        s_arrow.next_to(w_arrow, UP+RIGHT, buff=0)
        self.play(Create(s_arrow), Write(s_label))
        self.wait(2)

# To render the animation
if __name__ == "__main__":
    VectorSum().render()
