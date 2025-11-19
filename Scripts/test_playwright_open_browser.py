import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, channel="chrome")
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        await asyncio.sleep(3)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
