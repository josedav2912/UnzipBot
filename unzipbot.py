import logging
from pyrogram import Client, idle
from Config import Config


logging.basicConfig(
	level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
	"UnzipBot",
	api_id=4680438,
	api_hash="4f006822d68b21592c0b1e817019f6df",
	bot_token="6532946914:AAGWw01eqCvsZctThvlS1XN9AmGHLNpHjNE",
	plugins=dict(root="UnzipBot"),
)


# Run Bot
if __name__ == "__main__":
	app.start()  # Not using run as wanna print...
	uname = app.get_me().username
	print(f"@{uname} Started Successfully!")
	idle()
	app.stop()
	print("Bot stopped. Alvida!")
