import requests
import time
from bs4 import BeautifulSoup
import re
import json
import asyncio
from playwright.async_api import async_playwright

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

bot_url = "https://discord.com/api/webhooks/1394449017554866237/D_RKE8xWuHiw-mYT8cmNM3hC1S5NKx7qCUEuNGM_fujddTPeYfq2V3CnQdlaTHShWxvQ"

products = {
    "Pokémon Trading Card Game: Scarlet & Violet— Paldean Fates Booster Bundle" : "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-paldean-fates-booster-bundle/-/A-89432660#lnk=sametab"
}
def ping_disc(name,url):
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
        await page.goto("https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-paldean-fates-booster-bundle/-/A-89432660#lnk=sametab")
        
        content = await page.content()    
        try:
            await page.click("text=Shop all Pokemon")
            await page.goto("https://www.target.com/co-cart")
            await asyncio.sleep(9999)
        except:
            print("You")   
                  

def main():
    asyncio.run(fye_bot())
    
      
if __name__ == "__main__":
    main()      
        
    