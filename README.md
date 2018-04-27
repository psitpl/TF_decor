## TF_decor
* This program is the image classifier for traditional products from Russia, Poland, Turkey and Belarus
* It bases on image classifier [tensorflow-for-poets-2](https://github.com/googlecodelabs/tensorflow-for-poets-2)

* Accuracy achieved: 93.8%

### How to use it? step-by-step
* Download all files
* Move `tf_files` into `tensorflow-for-poets-2`
* Open a console and go to the folder `tensorflow-for-poets-2`
* Run command: `py -m scripts.label_image --graph=tf_files/retrained_graph.pb --image={IMAGE}`
In {IMAGE} put path to picture you want to recognize, for example `tf_files/decor/test_pol.jpg` (this image was not used to train neural net, program see this image for the first time)
* You should get the results simillar to following:

`valuation time (1-image): 0.291s`

`poland 0.9998863`

`turkey 0.000112255446`

`russia 1.4300568e-06`

`belarus 9.3076646e-10`
	
### Used dataset and sel_conv_reloc.py file
Images of products from [this database](https://www.kaggle.com/olgabelitskaya/traditional-decor-patterns/data) were in .png extension and were mixed with images of patterns.
Info about images was in `decor.csv` file (country, decor, type, file name), but there were some mistakes in column "type_label", so it was needed to use "type" column instead.
`sel_conv_reloc.py` (located in tf_files) does all that things: selects images with products, converts them into a .jpg and puts them into a proper folder.
	
Piotr Sowiński

piotr.sowinski.itpl@gmail.com
