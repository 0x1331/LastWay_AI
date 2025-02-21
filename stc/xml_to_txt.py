import xml.etree.ElementTree as ET

def parse_xml(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        # Загружаем XML-данные
        tree = ET.parse(f)
        root = tree.getroot()

        with open(output_file, 'w', encoding='utf-8') as out_file:
            # Проходим по всем статьям в XML
            for page in root.findall(".//page"):
                title = page.find("title").text
                revision = page.find("revision")
                text = revision.find("text").text if revision is not None else ""
                
                # Если текст статьи есть, пишем в файл
                if text:
                    out_file.write(f"Title: {title}\n")
                    out_file.write(f"Text: {text}\n\n")

# Пример использования
input_file = r"D:\LastWayVersions\Alpha2_Lastway_pro\data\ruwiki-latest-abstract.xml"
output_file = "data/dataset.txt"
parse_xml(input_file, output_file)

