import tkinter as tk
from tkinter import ttk


def check_answer(selected_option, button):
    global score, score_label
    if selected_option == questions[current_question]["answer"]:
        score += 1
        button.config(style="Correct.TButton")
    else:
        button.config(style="Incorrect.TButton")

    for btn in answer_buttons:
        btn.config(state="disabled")

    update_score_label()
    if current_question == len(questions) - 1:
        next_button.config(text="Finish", command=root.destroy)
    next_button.grid(row=6, column=0, pady=10)


def display_question():
    if current_question < len(questions):
        question_label.config(text=questions[current_question]["question"])
        for i, option in enumerate(questions[current_question]["options"]):
            answer_buttons[i].config(text=option, style="TButton", state="normal",
                                     command=lambda opt=option, btn=answer_buttons[i]: check_answer(opt, btn))
            answer_buttons[i].grid(row=2 + i, column=0, padx=20, pady=5)
        next_button.grid_remove()
    else:
        question_label.config(text="Quiz completed! Your score: " + str(score))


def update_score_label():
    score_label.config(text=f"Score: {score}/{len(questions)}")


def next_question():
    global current_question
    current_question += 1
    display_question()


root = tk.Tk()
root.title("Quiz Window")
root.geometry("600x400")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 12))
style.configure("Correct.TButton", bg="#009900")
style.configure("Incoreerrect.TButton", bg="#990000")

score_label = ttk.Label(root, text="")
score_label.grid(row=0, column=2, sticky="e")

question_label = ttk.Label(root, text="", wraplength=1, justify="center")
question_label.grid(row=1, column=0, pady=30)

answer_buttons = []
for i in range(3):
    button = ttk.Button(root, text="")
    answer_buttons.append(button)

next_button = ttk.Button(root, text="Next", command=next_question)

questions = [
    {
        "question": "Was passiert im ersten Kapitel von \"Die Physiker\" von Friedrich Dürrenmatt?",
        "options": [
            "Die Hauptfigur, Möbius, wird vorgestellt und zeigt Anzeichen von Geisteskrankheit.",
            "Die Physiker Möbius, Einstein und Newton diskutieren ihre Theorien.",
            "Eine Krankenschwester wird ermordet, und Inspektor Richard Voss ermittelt den Fall."
        ],
        "answer": "Eine Krankenschwester wird ermordet, und Inspektor Richard Voss ermittelt den Fall."
    },
    {
        "question": "Wer sind die Hauptfiguren im ersten Kapitel von \"Die Physiker\"?",
        "options": [
            "Möbius, Newton und Einstein",
            "Möbius, Beutler und Rose",
            "Möbius, Inspektor Voss und Fräulein Doktor Mathilde von Zahnd"
        ],
        "answer": "Möbius, Newton und Einstein"
    },
    {
        "question": "Wo spielt die Handlung im ersten Kapitel von \"Die Physiker\"?",
        "options": [
            "In einem Irrenhaus",
            "In einem Forschungsinstitut",
            "In einem Universitätslabor"
        ],
        "answer": "In einem Irrenhaus"
    },
    {
        "question": "Warum befinden sich die Physiker im Irrenhaus?",
        "options": [
            "Sie sind alle geisteskrank und werden behandelt.",
            "Sie nutzen das Irrenhaus als Tarnung, um ihre Forschungen vor der Öffentlichkeit zu verbergen.",
            "Sie wurden fälschlicherweise für verrückt erklärt und versuchen, ihre Unschuld zu beweisen."
        ],
        "answer": "Sie nutzen das Irrenhaus als Tarnung, um ihre Forschungen vor der Öffentlichkeit zu verbergen."
    }
]

current_question = 0
score = 0

display_question()
update_score_label()

root.mainloop()

if __name__ == '__main__':
    print()
