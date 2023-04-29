

import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("5878358617:AAGMJwKJ4zyUIoCqpPTp7ZH7IQhqu81OEZY"))  # Bot token
ADMINS = list(os.environ.get("1344087138"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili
open_weather_token = str(os.environ.get("open_weather_token"))