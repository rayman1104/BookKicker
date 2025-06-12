# Book Kicker
Telegram bot. https://telegram.me/BookKicker_bot

Allows reading book via telegram. 

Reminds every day with a little piece of text

Input file format: .epub

Output: message with the next piece of text

Auto-send every hour.

## How to run

Create a `.env` file based on `.env.example`:
```
TEST_TOKEN=your_test_bot_token_here
PRODUCTION_TOKEN=your_production_bot_token_here
BOT_SERVER_IP=your_bot_server_ip_here
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_NAME=your_db_name
```

You’ll need a PostgreSQL database and a host with a public IP address to receive incoming webhooks from Telegram.

Then run:
```
pip install -r /path/to/requirements.txt
nohup python3 telebot_handler.py /dev/null 2>&1&
```

## SSL Configuration

The bot supposes a reverse proxy approach for SSL termination, which is more secure and easier to manage. You'll need to set up a reverse proxy (like nginx) to handle SSL.

### For development/testing with self-signed certificates:
```
openssl genrsa -out key.pem 2048
openssl req -new -x509 -days 3650 -key key.pem -out cert.pem
```

When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
with the same value you put in `BOT_SERVER_IP`.
