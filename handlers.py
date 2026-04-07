from pyrogram import filters
from parser import parse_questions
from quiz import send_quiz, poll_data
from database import add_user, update_score, get_top

NEGATIVE = 0.25

def register(app):

    @app.on_message(filters.command("start"))
    async def start(client, message):
        add_user(message.from_user.id, message.from_user.first_name)
        await message.reply("🤖 Advanced Quiz Bot Ready!")

    @app.on_message(filters.command("quiz"))
    async def quiz_handler(client, message):
        text = message.text.replace("/quiz", "").strip()
        questions = parse_questions(text)

        for q in questions:
            await send_quiz(client, message.chat.id, q)

    @app.on_message(filters.command("leaderboard"))
    async def leaderboard(client, message):
        data = get_top()
        text = "🏆 Leaderboard\n\n"

        for i, u in enumerate(data, 1):
            text += f"{i}. {u['name']} → {round(u['score'],2)}\n"

        await message.reply(text)

    @app.on_poll_answer()
    async def handle_answer(client, poll_answer):
        user_id = poll_answer.user.id
        name = poll_answer.user.first_name
        selected = poll_answer.option_ids[0]

        add_user(user_id, name)

        poll_id = poll_answer.poll_id

        if poll_id in poll_data:
            correct = poll_data[poll_id]

            if selected == correct:
                update_score(user_id, True)
            else:
                update_score(user_id, False, NEGATIVE)
