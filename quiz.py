poll_data = {}

async def send_quiz(client, chat_id, q):
    poll = await client.send_poll(
        chat_id=chat_id,
        question=q["question"],
        options=q["options"],
        type="quiz",
        correct_option_id=q["answer"],
        explanation=q["explanation"],
        is_anonymous=False
    )

    poll_data[poll.poll.id] = q["answer"]
