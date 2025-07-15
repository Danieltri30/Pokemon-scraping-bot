import requests
import time
from bs4 import BeautifulSoup
import re
import json
import asyncio
from playwright.async_api import async_playwright

with open("config.json", "r") as f:
    config = json.load(f)

Headers = config["headers"]
bot_url = config["bot_url"]
products = config["products"]

def ping_disc(name, url):
    payload = {
        "content": f"🚨 **{name}** is now IN STOCK!\n{url}"
    }
    res = requests.post(bot_url, json=payload)
    if res.status_code == 204:
        print("✅ Alert sent to Discord.")
    else:
        print(f"❌ Failed to send alert: {res.status_code}")

async def fye_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        page = await browser.new_page()
        for name, url in products.items():
            await page.goto(url)
            content = await page.content()

            try:
                await page.click("text= Shop all Pokemon")
                await page.goto("https://www.target.com/co-cart")
                ping_disc(name, url)
                await asyncio.sleep(9999)  # Keep browser open for inspection
            except Exception as e:
                print(f"❌ {name} might be out of stock or button not clickable.")
                print(f"Error: {e}")

def main():
    asyncio.run(fye_bot())

if __name__ == "__main__":
    main()