# Web-Scraping Mini-Projet
##1. 
- J'ai scraper le site demoblaze, un site assez facile a scraper, mais mais pousse le code encore plus loin avec un login automatiser avec "page.wait_for_function(...)" plus pousser, j'ai fait ce code en asychrone pour permettre de montrer que je maitrise bien le côté "async et await" de playwright.
##2.
- Ce code est essentiellement focus sur le JavaScript du site, au boutton "Next", au lieu de faire par rapport au nombre de page j'ai fait, if not next_btn_is_visible() alors break et fin de la boucle pour dire qu'il y a plus de next donc plus de page.
#3.
- J'ai scrape les produits (15 produits plus precisement), j'ai scrape leur nom (modèle), le Prix, et l'url de l'image.
#4.
- Pour finir j'ai sauvearder ses informations sur un fichier csv.
