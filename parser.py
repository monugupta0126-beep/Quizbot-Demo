def parse_questions(text):
    blocks = text.strip().split("\n\n")
    questions = []

    for block in blocks:
        lines = block.split("\n")

        q = lines[0]
        options = []
        correct = 0
        explanation = ""

        for i, line in enumerate(lines[1:5]):
            if "✅" in line:
                correct = i
                line = line.replace("✅", "")
            options.append(line.strip())

        for line in lines:
            if line.startswith("Ex:"):
                explanation = line.replace("Ex:", "").strip()

        questions.append({
            "question": q,
            "options": options,
            "answer": correct,
            "explanation": explanation
        })

    return questions
