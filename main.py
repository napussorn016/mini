from pyscript import document, when #type:ignore

# ===== OOP =====
class Grade:
    def __init__(self, score):
        self.score = int(score)

    def calculate_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"

# ===== Event Button =====
@when("click", "#btn_calculate")
def calculate(event):

    score = document.getElementById("score").value

    if score == "":
        document.getElementById("output").innerText = "กรุณากรอกคะแนน"
        return

    grade = Grade(score)

    document.getElementById("output").innerText = \
        f"คะแนน {score} ได้เกรด {grade.calculate_grade()}"
