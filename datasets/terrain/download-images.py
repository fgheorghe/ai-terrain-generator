import requests
from tqdm import tqdm
import os

with open(r"images-urls.txt", 'r') as fp:
    image_urls = fp.readlines()

for image_index in tqdm(range(len(image_urls))):
    image_url = image_urls[image_index].strip()
    file_name = os.path.basename(image_url)
    image_data = requests.get(image_url).content
    with open(f'images/{file_name}', 'wb') as handler:
        handler.write(image_data)
