# Book Kicker
Telegram bot. https://telegram.me/BookKicker_bot

Allows reading book via telegram. 

Reminds every day with a little piece of text

Input file format: .epub

Output: message with the next piece of text

Auto-send every hour.


## Start server
nohup python3 telebot_handler.py /dev/null 2>&1&

### How to run

Create a file tokens.py (will be moved to .env or config later)
```
test_token='bot_token'
production_token='bot_token'
bot_server_ip='bot_server_ip'
user="db_user"
password="db_pass"
host="db_server"
db="db_name"
```

You will need database(Postgres) and host with public ip (for incoming webhooks from tg).
Then run ```pip install -r /path/to/requirements.txt```

To run server - run ```nohup python3 telebot_handler.py /dev/null 2>&1&```

### Quick'n'dirty SSL certificate generation
```
openssl genrsa -out key.pem 2048
openssl req -new -x509 -days 3650 -key key.pem -out cert.pem
```

When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
with the same value in you put in [WEBHOOK_HOST](https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/webhook_examples/webhook_flask_echo_bot.py#L23-L29).
