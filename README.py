import aiogram
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.filters.state import State, StatesGroup
import random
import asyncio
from aiogram.filters import Command

bot = Bot(token=' ')
dp = Dispatcher()

correct_answers = 0
incorrect_answers = 0

correct_answers = 0
incorrect_answers = 0


class Test(StatesGroup):
    first_question = State()

@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
    global correct_answers, incorrect_answers
    correct_answers = 0
    incorrect_answers = 0
    await message.reply("Привіт! Я готовий перевіряти твої знання математики. Готовий до першого питання?(введіть 'я готовий')")


    
@dp.message(lambda message: message.text.startswith("Я готов"))
async def generate_question(message: types.Message):
    # Генерация случайных чисел и оператора
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    # Формирование вопроса
    
    
    question_text = f"Який результат {num1} {operator} {num2}?"
    await message.reply(question_text)
    # Отримуємо відповідь користувача
        
@dp.message()
async def check_answer(message: types.Message):
    global correct_answers, incorrect_answers
    expression = message.text.split(" ")[3:]  # Отримуємо вираз, відкидаючи перші три слова
    user_answer = int(message.text.split(" ")[-1])  # Отримуємо відповідь користувача
    
    
    if len(expression) == 2:
        num1, operator, num2 = map(int, expression)
        correct_result = eval(f"{num1} {operator} {num2}")
        if user_answer == correct_result:
            correct_answers += 1
            await message.reply("Правильно!")
        else:
            incorrect_answers += 1
            await message.reply(f"Невірно. Правильна відповідь {correct_result}.")
        startus =+ 1

    
    
async def main():
    print("Starting bot...")
    print("Bot username: @{}".format((await bot.me())))
    await dp.start_polling(bot)

asyncio.run(main())
