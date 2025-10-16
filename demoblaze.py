from playwright.async_api import async_playwright
import asyncio, csv
from urllib.parse import urljoin

url = "https://demoblaze.com/"
path_csv = r"C:\Users\ighik\OneDrive\Escritorio\html\py-js\playwirght_projet\ex10.csv"
data = []

async def scrape(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        await page.locator("a#login2").click()
        await page.wait_for_selector("input#loginusername")

        await page.fill("input#loginusername", "rys.73")
        await page.fill("input#loginpassword", "123456789")

        await page.locator("button:has-text('Log in')").click()
        await page.wait_for_timeout(3000)
        if await page.locator("a#logout2").is_visible():
          print("Connecter avec succès")

          while True:
             
             await page.wait_for_function(
                "document.querySelectorAll('div.col-lg-4.col-md-6.mb-4').length > 0")
             
             produits = page.locator("div.col-lg-4.col-md-6.mb-4")
             count = await produits.count()
             print(f"Page Actuelle : {page.url} ===> ({count} produits)")

             for i in range(count):
                url_href = await produits.nth(i).locator("a.hrefch").get_attribute("href")
                if not url_href:
                   continue
                url_produit = urljoin(url, url_href)

                produit_page = await browser.new_page()
                await produit_page.goto(url_produit)
                await produit_page.wait_for_selector("h2.name")

                nom = await produit_page.locator("h2.name").inner_text()
                prix = await produit_page.locator("h3.price-container").inner_text()
                img_src = await produit_page.locator("div#imgp img").get_attribute("src")
                img_url = urljoin(url, img_src)
                data.append({"Nom": nom.strip(), "Prix": prix.strip(), "URL_IMG": img_url.strip()})
                print(f" {nom} ajouté")
                await produit_page.close()

             next_btn = page.locator("button#next2")
             if await next_btn.is_visible():
               await next_btn.click()
               await page.wait_for_timeout(1000)
             else:
               print("Fin de pagination.")
               break
          with open(path_csv, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["Nom", "Prix", "URL_IMG"])
            writer.writeheader()
            writer.writerows(data)
          print(f"Données sauvegardées dans {path_csv}")
        else:
           print("Erreur de connexion")

        await browser.close()


asyncio.run(scrape(url))