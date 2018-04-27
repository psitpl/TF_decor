from PIL import Image
import os
import pandas as pd

tab = pd.read_csv(r"decor.csv", delimiter=',', engine='python')
is_product = tab['type']
file_name = tab['file']
countries = tab['country']

for i in range(0, len(is_product)):
    if is_product[i]=='product':
        country = countries[i]
        if not os.path.exists(country):
            os.makedirs(country)

        picture_name = file_name[i]
        picture_name = picture_name[:-4]
        img = Image.open((picture_name + ".png"))
        new_img = img.resize( (150, 150) )
        if new_img.mode != "RGB":
            new_img = new_img.convert("RGB")
        new_img.save( country + "/" + picture_name + ".jpg", 'jpeg')
