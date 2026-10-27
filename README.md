# 🤖 Professional Discord Utility Bot

A clean, modular, and entry-level professional Discord bot built in Python. This project serves as a portfolio piece showcasing backend best practices, REST API integration, in-memory binary file processing, and secure environment configuration.

## 🚀 Features

* **`!info`**: Displays bot authorship and project details.

* **`!crypto <coin>`**: Fetches real-time market prices in USD using the public **CoinGecko REST API**.

* **`!news`**: Retrieves the top 3 tech stories from the **HackerNews API** complete with score points and direct article URLs.

* **`!qr <text/url>`**: Dynamically generates QR code images on-the-fly using an **in-memory buffer (`io.BytesIO`)**, avoiding temporary file creation on disk.

* **Auto-Greeting Event**: Listens to server chat messages and automatically welcomes users when they greet in the channel.

## 🛠️ Tech Stack & Libraries

* **Python 3.x**

* **`discord.py`**: Modern async framework for Discord API integration and command processing.

* **`requests`**: Synchronous HTTP library for external API communication.

* **`qrcode` & `Pillow`**: Image generation and binary matrix processing for QR codes.

* **`python-dotenv`**: Secure environment variable management.

## 📁 Project Structure

```
.
├── app.py              # Main application entry point and bot logic
├── requirements.txt    # Project dependencies
├── .env                # Local environment variables (excluded via .gitignore)
├── .gitignore          # Git exclusion rules
└── README.md           # Project documentation

```

## ⚙️ Setup and Installation

Follow these steps to run the bot locally on your machine:

### 1. Clone the repository

```
git clone https://github.com/AlvaroManrique/discord-bot.git
cd discord-bot

```

### 2. Install required dependencies

```
pip install -r requirements.txt

```

### 3. Configure environment variables

Create a `.env` file in the root directory and insert your secret Discord Bot Token:

```
DISCORD_TOKEN=your_discord_bot_token_here

```

### 4. Run the application

```
python app.py

```

## 💡 Usage Examples

In any Discord channel where the bot has read/write permissions, type `!` followed by any of the commands:

```
!info
!crypto bitcoin
!news
!qr https://github.com

```

## 👤 Author

Developed by **Alvaro**.
