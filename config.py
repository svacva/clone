#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = "Your_Telegram_bot_token"

    # Get from my.telegram.org
    APP_ID = int(25149611)

    # Get from my.telegram.org
    API_HASH = "1793851895dd1376678214542445c652"

    # Generate a user session string
    TG_USER_SESSION = "BQF_wKsAu_YQHsn5NSEEZGA2VCQNoVaLGJVLtYHSAjZFlRWNP3S19vCXAF3Y3dKvIXEntkhJfLuzKMUaeL3ySh-3c_P7Ij7t24Uv01xJ0onoszo5nuisqM8xIUbmo9uH1KDtD8XopjbTIqVUG7XNB0l9CTJln8cVJRl_nwLShUDlkX_JnC3ltv1EeHQVZU692LbmwSF7OTXQdtjHiuegNsKJHNvUM9qU1EjF-tsKw0ABJkGtkMkOLhNfnyD15gNFtMu3ZtIWbomkFwuqmRxlUML4CuH1VoC0XCDzsSnpXub8GnBcOlVFRupGJHs__76kQN1HowgRYICWKmDyOrqe6jVENH69YAAAAABVXjtZAA"

    # Database URI
    DB_URI = "mongodb+srv://cva5545:IUOHUwWxVdlDyzbH@cluster0.l031f.mongodb.net/?retryWrites=true&w=majority"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
