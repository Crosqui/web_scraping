import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.cl/computacion/notebooks-accesorios/notebooks/apple/nuevo/apple-m1-8-core-gpu/rm-metropolitana/macbook-m1_NoIndex_True#applied_filter_id%3DITEM_CONDITION%26applied_filter_name%3DCondici%C3%B3n%26applied_filter_order%3D4%26applied_value_id%3D2230284%26applied_value_name%3DNuevo%26applied_value_order%3D1%26applied_value_results%3D10%26is_custom%3Dfalse"

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find("ol", {"class": "ui-search-layout ui-search-layout--stack shops__layout"})

#Order for values 
sorted_results = sorted(results, key=lambda data: float(data.find("span", {"class": "price-tag-fraction"}).get_text().replace(".", "")))

#Create archive .txt with data returned
with open("data.txt", "w") as archive:
#Extract and build information 
    for data in sorted_results:
        try:
            title = data.find("a", {"class": "ui-search-item__group__element shops__items-group-details ui-search-link"}).get_text()
            value = data.find("span", {"class": "price-tag-fraction"}).get_text()
            website = data.find("a").get("href")
            data = "Titulo: {}\nValor:{}\nLink:{}\n"
            data = data.format(title, value, website)
            archive.write(data)
            archive.write("\n") 

        except Exception as e:
            print("An error occurred in the search: " ,e)
            pass
