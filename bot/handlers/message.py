from aiogram.filters import Command, CommandStart

from gemini_service import generate_answer

from aiogram import Router, F


router = Router()
@router.message(CommandStart())
async def handle_start(message):
    await message.answer("Assalomu alaykum! Ai telegram chatbotga xush kelibsiz! \n"
                         "Bu chatbot orqali aidan o'zingizni qiziqtirgan savollar berishingiz mumkin, "
                         "suhbatlashishingiz mumkin!")
#help komandasi uchun!

@router.message(Command("help"))
async def handle_help(message):
    await message.answer("""AI Telegram Chatbot — Yordam

Assalomu alaykum! Men AI yordamchiman.
Siz bilan suhbatlashish va savollaringizga javob berish uchun yaratilganman.

Mening imkoniyatlarim:
- Istalgan mavzuda savol berish.
- Tarjima qilish.
- Dasturlash bo‘yicha yordam olish.

Komandalar:
- /start — Botni boshlash.
- /help — Yordam olish.

Eslatma: Hozircha bot faqat matnli xabarlarni qabul qiladi.""")


@router.message(F.text)
async def handle_message(message):
    user_id = message.from_user.id
    user_message = message.text
    try:
        answer = await generate_answer(user_id, user_message)
    except Exception as e:
        print(e)
        await message.answer("AI xizmatida vaqtinchalik muammo yuz berdi. Birozdan keyin qayta urinib ko‘ring.")
    else:
        await message.answer(answer)

@router.message(~F.text)
async def handle_non_message(message):
    await message.answer("Menga faqat matn yuboring!")


