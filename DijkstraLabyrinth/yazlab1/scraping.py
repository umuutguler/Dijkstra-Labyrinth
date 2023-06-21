import requests
from bs4 import BeautifulSoup




headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


class Sites:


    def hepsiburada(self):

        i = int
        band_name = []
        models_name = []
        computers_list = []
        rating_list = []
        ekran_boyutu_list = []
        islemci_list = []
        islemci_tipi_list = []
        isletim_sistemi_list = []
        ssd_kapasitesi_lst = []
        ram_list = []
        URLL = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa="
        for i in range(1, 50):

            URL = URLL + str(i)
            R = requests.get(URL, headers=headers)
            soup = BeautifulSoup(R.content, "lxml")
            st1 = soup.find("div", attrs={"class": "productListContent-pXUkO4iHa51o_17CBibU"})
            st2 = st1.find("ul", attrs={"class": "productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm"})
            st3 = st2.find_all("li", attrs={"class": "productListContent-zAP0Y5msy8OHn5z7T_K_"}) if st2 is not None else None

            for computersinformations in st3:
                linksonu = computersinformations.a.get("href")
                linkbasi = "https://www.hepsiburada.com/"

                if "adservice" in linksonu:
                    link = linksonu
                else:
                    link = linkbasi + linksonu
                r1 = requests.get(link, headers=headers)
                soup1 = BeautifulSoup(r1.content, "lxml")
                soup2 = soup1.find("table", attrs={"class": "data-list tech-spec"})

                soup3 = [e.text for e in soup2.find_all("th")]
                soup4 = [e.text for e in soup2.find_all("td")]
                for b in range(0, len(soup4)):
                    a = soup4[b].strip('\n')
                    soup4[b] = a

                soup_price = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceBeforePoint'"}).text.strip()
                soup_price2 = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceAfterPoint'"}).text.strip()

                soup_rating = soup1.find("div", attrs={"class": "first-eveluate"})
                rating = soup1.find("span", attrs={"class": "rating-star"}).text if soup_rating is None else None
                a = rating.strip('\r\n ') if rating is not None else None
                rating = a
                rating_list = "Puanı", rating

                tittles = computersinformations.a.get("title")
                titles_split = tittles.split()

                # Marka Isimleri
                band_name = "Marka", titles_split[0]

                # Model Isimleri
                models_name = "Model", titles_split[1]


                prices = (soup_price + "," + soup_price2)   # TODO: should be string type return to int
                for soup in soup3:
                    if soup == "Ekran Boyutu":
                        index_ekran_boyutu = soup3.index("Ekran Boyutu")
                        ekran_boyutu_list = soup, soup4[index_ekran_boyutu]
                    elif soup == "İşlemci Nesli":
                        index_islemci = soup3.index("İşlemci Nesli")
                        islemci_list = soup, soup4[index_islemci]
                    elif soup == "İşlemci Tipi":
                        index_islemci_tipi = soup3.index("İşlemci Tipi")
                        islemci_tipi_list = soup, soup4[index_islemci_tipi]
                    elif soup == "İşletim Sistemi":
                        index_isletim_sistemi = soup3.index("İşletim Sistemi")
                        isletim_sistemi_list = soup, soup4[index_isletim_sistemi]
                    elif soup == "SSD Kapasitesi":
                        index_ssd_kapasitesi = soup3.index("SSD Kapasitesi")
                        ssd_kapasitesi_lst = soup, soup4[index_ssd_kapasitesi]
                    elif soup == "Ram (Sistem Belleği)":
                        index_ram = soup3.index("Ram (Sistem Belleği)")
                        ram_list = soup, soup4[index_ram]

                computers_list = link, band_name, models_name, prices, rating_list, ekran_boyutu_list, islemci_list, islemci_tipi_list, isletim_sistemi_list, ssd_kapasitesi_lst, ram_list

                #print(computers_list)
    def vatan(self):
        URLL = "https://www.vatanbilgisayar.com/notebook/?page="

        for i in range(1, 2):
            URL = URLL + str(i)
            # Number of page
            #print(i)
            R = requests.get(URL, headers=headers)
            soup = BeautifulSoup(R.content, "lxml")
            page = soup.find("div", attrs={"id": "productsLoad"})
            products = page.find_all("div", attrs={"class": "product-list product-list--list-page"})

            for details in products:
                link = "https://www.vatanbilgisayar.com" + details.a.get("href")
                #print(link)
                r1 = requests.get(link, headers=headers)
                soup1 = BeautifulSoup(r1.content, "lxml")

                name = soup1.find("h1", attrs={"class": "product-list__product-name"}).text
                #print(name)

                price = soup1.find("span", attrs={"class": "product-list__price"}).text
                price = price.split(".")
                price = price[0] + price[1]
                price = int(price)

                #print(price)

                features = soup1.find("div", attrs={"id": "urun-ozellikleri"})
                features2 = [e.text for e in features.find_all("td")]

                for i in range(0, len(features2)):
                    a = features2[i].strip('\n')
                    features2[i] = a

                index = 0

                for x in features2:
                    if index == len(features2):
                        break
                    ozellikler = [features2[index], features2[index+1]]
                    index = index + 2

                rate = soup1.find("span", attrs={"class": "score"})
                rate1 = str(rate)
                rate2 = rate1.split()
                rate3 = rate2[4].strip('%;"></span>')
                rate4 = int(rate3)
                if rate4 == 0:
                    rating = 'Henüz Değerlendirilmedi'
                else:
                    rating = rate4 / 20

                #print(rating)

                image = soup1.find_all("a", attrs={"data-fancybox": "images"})
                image = image[0]
                image = str(image)
                image = image.split("=")
                image = image[2]
                image = image.strip(' <img alt')
                image = image.strip('\n ">')
                #print(image)

                # Check Ozellikler
                computers = (["Pc adı ,", name], ["Ozellikler", ozellikler], ["Puanlandırma", rating], ["Link", link], ["image", image])
                print(computers)

    def teknosa(self):
        i = int
        band_name = []
        models_name = []
        computers_list = []
        rating_list = []
        ekran_boyutu_list = []
        islemci_list = []
        islemci_tipi_list = []
        isletim_sistemi_list = []
        ssd_kapasitesi_lst = []
        ram_list = []
        URLL ="https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page="
        for i in range(1, 67):
            URL = URLL + str(i)
            #print(i)
            R = requests.get(URL, headers=headers)
            soup = BeautifulSoup(R.content, "lxml")
            page = soup.find("div", attrs={"class": "products"})
            products = page.find_all("div", attrs={"id": "product-item"})

            for details in products:
                link = "https://www.teknosa.com/" + details.a.get("href")
                #print(link)
                r1 = requests.get(link, headers=headers)
                soup2 = BeautifulSoup(r1.content, "lxml")

                name = details.a.get("title")
                #print(name)

                price = soup2.find("span", attrs={"class": "prc prc-last"})
                price = price.text if price is not None else None

                #print(price)

                features = soup2.find("div", attrs={"class": "ptf-body"})
                features2 = [e.text for e in features.find_all("th")] if features is not None else None
                features3 = [e.text for e in features.find_all("td")] if features is not None else None

                #print("features2 bu", features2)
                #print("features3 bu", features3)

                for feature in features2:
                    if feature == "SSD Kapasitesi":
                        index_ekran_boyutu = features2.index("SSD Kapasitesi")
                        ekran_boyutu_list = feature, features3[index_ekran_boyutu]
                    elif feature == "Ekran Boyutu":
                        index_islemci = features2.index("Ekran Boyutu")
                        islemci_list = feature, features3[index_islemci]
                    elif feature == "Ekran Çözünürlüğü (Piksel)":
                        index_islemci_tipi = features2.index("Ekran Çözünürlüğü (Piksel)")
                        islemci_tipi_list = feature, features3[index_islemci_tipi]
                    elif feature == "İşlemci Nesli":
                        index_isletim_sistemi = features2.index("İşlemci Nesli")
                        isletim_sistemi_list = feature, features3[index_isletim_sistemi]
                    elif feature == "İşlemci":
                        index_ssd_kapasitesi = features2.index("İşlemci")
                        ssd_kapasitesi_lst = feature, features3[index_ssd_kapasitesi]
                    elif feature == "Ekran Kartı Modeli":
                        index_ram = features2.index("Ekran Kartı Modeli")
                        ram_list = feature, features3[index_ram]



                image = soup2.find("div", attrs={"data-type": "image"})
                image = str(image)
                image = image.split("data-srcset")
                image = image[1]
                image = image.split(" ")
                image = image[0]
                image = image.strip('="')

                computers_list = link, name, ekran_boyutu_list, islemci_list, islemci_tipi_list, isletim_sistemi_list, ssd_kapasitesi_lst, ram_list

                #print(computers_list)

    def trendyol(self):
        URLL = "https://www.trendyol.com/laptop-x-c103108?pi="

        for i in range(1, 51):
            URL = URLL + str(i)
            #print(i)
            R = requests.get(URL, headers=headers)
            soup = BeautifulSoup(R.content, "lxml")
            page = soup.find("div", attrs={"class": "prdct-cntnr-wrppr"})
            products = page.find_all("div", attrs={"class": "p-card-wrppr with-campaign-view"})

            for details in products:
                link = "https://www.trendyol.com" + details.a.get("href")
                #print(link)
                r1 = requests.get(link, headers=headers)
                soup1 = BeautifulSoup(r1.content, "lxml")

                features = soup1.find("ul", attrs={"class": "detail-attr-container"})
                features2 = [e.text for e in features.find_all("span")] if features is not None else None

                index = 0
                for x in features2:
                    if index == len(features2):
                        break
                    ozellikler = [features2[index], features2[index+1]]
                    index = index + 2

                brand = details.span.get("title")
                model = soup1.find("h1", attrs={"class": "pr-new-br"}).span.text
                name = brand + model

                price = soup1.find("span", attrs={"class": "prc-dsc"}).text
                price = price.strip(' TL')
                price = price.split(".")
                price = price[0] + price[1]
                price = price.split(",")
                if len(price) == 2:
                    price = price[0] + "." + price[1]
                else:
                    price = price[0]
                price = float(price)
                #print(price)

                #print(name)
                #print(price)
                #print(features2)

                image = soup1.find("div", attrs={"class": "product-container"})
                image = image.find("div", attrs={"class": "product-slide focused"})
                if image is not None:
                    image = str(image)
                    image = image.split("src=")
                    image = image[1]
                    image = image.strip('"/></div>')

                #print(image)

                # Check Ozellikler
                computers = (["Pc adı ,", name], ["Ozellikler", ozellikler], ["Link", link],["image", image])