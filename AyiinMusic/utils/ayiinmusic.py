from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from AyiinMusic import app
import config


def ayiin(func):
    async def wrapper(_, message: Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        ppk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        if not config.MUST_JOIN:  # Not compulsory
            return
        try:
            try:
                await app.get_chat_member(config.MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                if config.MUST_JOIN.isalpha():
                    link = "https://t.me/" + config.MUST_JOIN
                else:
                    chat_info = await app.get_chat(config.MUST_JOIN)
                    chat_info.invite_link
                try:
                    await message.reply(
                        f"Hai {ppk},\nSupaya Bisa Menggunakan Bot Kamu Harus Masuk Ke Grup Support bot Terlebih Dahulu!.Silahkan Klik Tombol Di Bawah Untuk Join Ke Grup support.",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("• Join Grup Bot •", url=link)]]
                        ),
                    )
                    await message.stop_propagation()
                except ChatWriteForbidden:
                    pass
        except ChatAdminRequired:
            await message.reply(
                f"Saya bukan admin di chat MUST_JOIN chat : {config.MUST_JOIN} !"
            )
        return await func(_, message)

    return wrapper
