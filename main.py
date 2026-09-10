import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Sticker
from APIKEY import API
import app.keyboards as kb
from random import choice
stikers = ["CAACAgIAAxkBAAMMakZLMOfcIBifKqPLd86HPDY3sXYAAvOhAAL0dwlKUy9Fzqldscs8BA","CAACAgIAAxkBAAMOakZLMoLGQs2FCWF1s9CjMDuCULkAAgGjAALG3ghKtR8nF9EtG-c8BA","CAACAgIAAxkBAAMQakZLNKCdlXfULmt2NOiAaoapJfwAAtinAAJqshBKJLJDeXPbq8g8BA","CAACAgIAAxkBAAMSakZLNO8LNvxUwVj2gVGmJcHlW-8AAnGcAALbmwhKSkDCMGOlyJ48BA","CAACAgIAAxkBAAMUakZLNfxgvWWJuxY29LlfwweiVfUAAkmYAAKN_wlKWeMcfp48MVk8BA","CAACAgIAAxkBAAMWakZLNYOLS6hhac6lnTszNorq_-MAAlm0AAKQUAhKWyaATqVoxNk8BA","CAACAgIAAxkBAAMYakZLNjI6JNR9BLROrHPzo7XbvpEAAsCYAAI_HQlKXtYWzkJXsLQ8BA","CAACAgIAAxkBAAMaakZLNrWBAmeXvGBGkzKzbo4_c10AAsWkAALArxBKEhLEYI9fPjk8BA","CAACAgIAAxkBAAMcakZLN7JiQfgvQH8aeeemoyFeOkwAAlGcAAJMNRFKYuEp0bc1Oek8BA","CAACAgIAAxkBAAMeakZLN4pUaMNAYLQcMUeU9EpE8E8AAlueAAIL7BFKOm8-WFsFEWk8BA","CAACAgIAAxkBAAMgakZLONewU7-arofyTRa_EIH1oKwAAt2gAAJP2xFKqow74FuJjnI8BA","CAACAgIAAxkBAAMiakZLONznlChLrcq__UVY-fUn4s4AApWkAAKgtQhKUhqm4rkKMqM8BA","CAACAgIAAxkBAAMkakZLOZm8hB6-R9jvySA7rcUTAXMAAhKgAAJDkRFKDBo1TVrpMRw8BA","CAACAgIAAxkBAAMmakZLOeanmCMjSiR_NFP2NWFno9wAAkSeAAIutwhKffjI4hYB8Rk8BA","CAACAgIAAxkBAAMoakZLOfsK4bV2nzK7WzKconC_XyQAArKbAAIZGQhKbIve923WT8Q8BA","CAACAgIAAxkBAAMqakZLOouh0O8VcFmaHK8tFX902xoAAvmjAALp1ghK34AIyotJpvs8BA","CAACAgIAAxkBAAMsakZLOxWhaTcl89PNO9oOItlmdsMAAheZAAIQFAhKQ4ldM91WftA8BA","CAACAgIAAxkBAAMuakZLO2U_375hcZfXd-I8nANvdxYAAtCZAAKCvghKeQvN0ezMoNE8BA","CAACAgIAAxkBAAMwakZLPDcSZE-K4gHWR3pmz4ZfqxYAAmueAAJIeghKMjOWhyZfK1E8BA","CAACAgIAAxkBAAMyakZLPOrMPw69Impapq1SQMllzIAAAgSgAAIGdAlKPusvsuDf1uM8BA","CAACAgIAAxkBAAM0akZLPQuuOiUyzvAszsqgjHoFjbsAAtebAAI5pwhKv6aJOqOhszo8BA","CAACAgIAAxkBAAM2akZLPVijUy6FC945ZxXkEo_H070AAqCoAAK63QhKVBBB-Gf56jM8BA","CAACAgIAAxkBAAM4akZLPj4rkT2D4KBCbhEe2er3NBMAAo-gAAI1sAlKm80CugOngzY8BA","CAACAgIAAxkBAAM6akZLPrydac84nGjOcpTNGgpPrsgAAuiYAAK-1wlKRVC2LVjXRU08BA","CAACAgIAAxkBAAM8akZLP0z0_Tl2cLUV3uyrPrkCiKwAAuCmAAKCzAlK1H41VNHnkfM8BA","CAACAgIAAxkBAAM-akZLQFBv0OIOctiJr6fkMId9rx4AAj6pAAJm3yhKqvMBtb8whPo8BA","CAACAgIAAxkBAANAakZLQPcwTA45nYeZyUPpexYV-eoAAuCZAAItmAlKVXfnETCLmf08BA"]
bot = Bot(token=API)
dp = Dispatcher()
@dp.message(CommandStart())
@dp.message(F.text == "🔍 Старт")
async def start_command(message: Message):
    await message.answer("Дароу кимпинтяу я те щас нагадаю толсти. Что бы гадать напиши /gadai", reply_markup=kb.mian)
@dp.message(Command("gadai"))
@dp.message(F.text == "🎲 Гадание")
async def gadai_command(message: Message):
    await message.answer_sticker(choice(stikers))

async def main():
    print("Бот успешно запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())