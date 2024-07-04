import re

def extract_image_links(html_text):
    """
    Извлекает ссылки на изображения из HTML-текста.

    Аргументы:
    html_text (str): HTML-текст, из которого извлекаются ссылки на изображения.

    Возвращается:
    список: Список ссылок на изображения, найденных в HTML-тексте.
    """
    pattern = r"src=['\"](https?://[^'\"]+\.(jpg|jpeg|png|gif))['\"]"
    image_links = re.findall(pattern, html_text)
    return [link[0] for link in image_links]

# Example usage
sample_html = "<img src='https://sopranoclub.ru/images/190-epichnyh-anime-artov/file48673.jpg'> <img src='https://i.pinimg.com/originals/78/01/9e/78019ec87cc5c8b38af17c57371852ae.png'> <img src='https://i.pinimg.com/originals/f1/63/11/f16311fd0c32786525f471c685bc516e.gif'>"
image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")