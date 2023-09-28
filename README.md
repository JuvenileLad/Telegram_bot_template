# Telegram Bot using Pyrogram Template
This is a template for creating a Telegram bot using the Pyrogram library in Python. Pyrogram is a powerful and asynchoronous library for building Telegram bots.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/JuvenileLad/tg-todoer-bot)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg?&style=flat-square)](https://github.com/JuvenileLad/tg-todoer-bot#copyright--license)

### <div id="preq">Prequisites</div>
This is not a beginner's guide to making telegram bots. Beginner to Intermediate familiarity with Python3.6+ is recommended.

*Obtain all the required API credentials*

- Go to https://my.telegram.org/auth
- Follow [this](https://core.telegram.org/api/obtaining_api_id#obtaining-api-id) guide to obtain Telegram API hash & API key
- Obtain the bot token from https://t.me/BotFather
	
### <div id="config">Configuration</div>
copy the contents of `config.env_example` to a new file `config.env` by using the following command:

*Windows*
```bash
copy config.env_example config.env
```
*Linux/maxOS (Unix-like systems)*
```bash
cp config.env_example config.env
```

or you can just rename `config.env_example` to `config.env`. After that, edit the config.env file and replace the values as follows:

*(do not add quotes(" ") symbol in any value)*
- in `TELEGRAM_SESSION_NAME` enter whatever you want as session name in telegram
- enter telegram API Hash in `TELEGRAM_API_HASH` & API ID in `TELEGRAM_API_ID`
- enter telegram bot token in `TELEGRAM_BOT_TOKEN`
- the `VERSION` could be anything. It will be printed in the console whenever the bot is deployed.
## Installation
1) Clone this repository to your local machine:
```bash
git clone https://github.com/JuvenileLad/Telegram_bot_template.git
```

2) Change to the project directory:
```bash
cd Telegram_bot_template
```

3) Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

4) Run the bot:
```bash
python3 -m app_name
```

*change all instaces of app_name to the name of your project/bot.*
## Usage

- Start a chat with your bot on Telegram and send it `/start` command to interact with it.

## Bot Development

You can start building your bot by customizing the `app_name/core/main.py` file. Pyrogram provides a comprehensive API to interact with Telegram's Bot API, allowing you to handle messages, send replies, and perform various actions.
This template follows a modular system in which the utility modules would be inside the `app_name/utils` folder. There is also a separate folder for database related modules in `app_name/db`. A plugins folder can also be added if the need arises.


## Resources

- [Pyrogram Documentation](https://docs.pyrogram.org/)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)

## Contributing

Contributions are welcome! If you'd like to contribute to this template or report issues, please create a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/JuvenileLad/Telegram_bot_template/blob/main/LICENSE.md) file for details.

---

**Note:** This is a basic template to help you get started with building a Telegram bot using Pyrogram. Be sure to explore Pyrogram's documentation and Telegram's Bot API documentation for more advanced features and capabilities.