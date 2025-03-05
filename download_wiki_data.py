import requests

# URL файла для скачивания
url = "https://dumps.wikimedia.org/ruwiki/latest/ruwiki-latest-abstract.xml.gz"

# Путь для сохранения файла
output_file = r"D:\LastWayVersions\Alpha2_Lastway_pro\data\ruwiki-latest-abstract.xml.gz"

response = requests.get(url)
with open(output_file, "wb") as file:
    file.write(response.content)

print("Файл скачан успешно!")
