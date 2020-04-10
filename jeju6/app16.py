from questions import question

question_prompts = [
    "what color are apples?\n(a) red/green\n(b) purple\n(c) blue\n\n",
    "what color are bananas?\n(a) blue\n(b) black\n(c) yellow\n\n",
    "what color are strawberries?\n(a) red\n(b) green\n(c) brown\n\n",
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "a"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            scrore += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


