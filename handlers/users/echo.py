
#Ob havo bot kodlari


import requests
import datetime
from data.config import open_weather_token
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp


@dp.message_handler(Command("start"))
@dp.message_handler(Command("obhavo"))
async def start_command(message: types.Message):
    await message.reply("Assalomu alaykum menga hudud nomini kiriting ob havo ma'lumotini aytaman!")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Bulutli \U00002601",
        "Rain": "Yomg'ir \U00002614",
        "Drizzle": "Yomg'ir \U00002614",
        "Thunderstorm": "Momaqaldiroq \U000026A1",
        "Snow": "Qor \U0001F328",
        "Mist": "Tuman \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Ob-havo qandayligini tushunmayapman!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***<b>{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}</b>***\n"
              f"<b>Ob-havo ma'lumoti:</b> {city}\n<b>Harorat:</b> {cur_weather}C° {wd}\n"
              f"<b>Namlik:</b> {humidity}%\n<b>Bosim:</b> {pressure} мм.рт.ст\n<b>Shamol tezligi:</b> {wind} м/с\n"
              f"<b>Quyosh chiqishi:</b> {sunrise_timestamp}\n<b>Quyosh botishi:</b> {sunset_timestamp}\n<b>Kun uzunligi:</b> {length_of_the_day}\n"
              f"***😊<b>Kuningiz Xayrli bo'lsin!</b>***"
              )

    except:
        await message.reply("❗️Hudud nomini noto'g'ri kiritdingiz ")