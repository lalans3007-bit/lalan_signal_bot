import telebot
import yfinance as yf

BOT_TOKEN = "ISI_TOKEN_BOT_KAMU_DI_SINI"
bot = telebot.TeleBot(BOT_TOKEN)

# === Fungsi Cek Breakout + Retest ===
def check_breakout(pair="EURUSD=X"):
    data = yf.download(pair, period="2d", interval="5m")
    last = data.iloc[-1]
    prev = data.iloc[-2]

    # Breakout Sederhana
    if last['Close'] > prev['High']:
        return f"📈 *BREAKOUT UP* pada {pair}\nHarga terakhir: {last['Close']}"
    elif last['Close'] < prev['Low']:
        return f"📉 *BREAKOUT DOWN* pada {pair}\nHarga terakhir: {last['Close']}"
    else:
        return f"⏳ Belum ada breakout pada {pair}"

# === Perintah /signal ===
@bot.message_handler(commands=['signal'])
def send_signal(message):
    pairs = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "EURGBP=X"]
    results = []

    for p in pairs:
        results.append(check_breakout(p))

    bot.reply_to(message, "\n\n".join(results), parse_mode="Markdown")

# === Start Bot ===
bot.polling()
