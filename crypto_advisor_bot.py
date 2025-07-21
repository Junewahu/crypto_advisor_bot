# crypto_advisor_bot.py

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def greet():
    print("""
Hey there! I’m CryptoBuddy 🤖
Your friendly AI-powered financial sidekick!
Ask me about crypto trends, sustainability, or long-term growth.
(Type 'bye' or 'exit' to leave.)
""")

def get_most_sustainable():
    return max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

def get_trending():
    return [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]

def get_long_term():
    # Prioritize rising + high market cap, else best sustainability
    candidates = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if candidates:
        return candidates[0]
    else:
        return get_most_sustainable()

def get_most_profitable():
    # Profitability: rising trend and high market cap
    candidates = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if candidates:
        return candidates[0]
    else:
        return max(crypto_db, key=lambda x: 1 if crypto_db[x]["price_trend"] == "rising" else 0)

def main():
    greet()
    while True:
        user_query = input("You: ").lower()
        if any(word in user_query for word in ["sustainable", "eco", "green"]):
            recommend = get_most_sustainable()
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")
        elif any(word in user_query for word in ["trending", "rising", "up"]):
            trending = get_trending()
            print(f"CryptoBuddy: These cryptos are trending up: {', '.join(trending)} 🚀")
        elif any(word in user_query for word in ["long-term", "growth", "future"]):
            recommend = get_long_term()
            print(f"CryptoBuddy: {recommend} is a great choice for long-term growth! 🚀")
        elif any(word in user_query for word in ["profitable", "profit", "best buy"]):
            recommend = get_most_profitable()
            print(f"CryptoBuddy: {recommend} looks most profitable right now based on trends and market cap!")
        elif any(word in user_query for word in ["bye", "exit", "quit"]):
            print("CryptoBuddy: Remember, crypto is risky—always do your own research! Bye! 👋")
            break
        else:
            print("CryptoBuddy: I can help with questions about trends, sustainability, profitability, or long-term growth! Try asking: 'Which crypto is trending up?' or 'What’s the most sustainable coin?'")

if __name__ == "__main__":
    main() 