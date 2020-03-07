
def extractor(photo_name):


	import cv2
	import pytesseract

	pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\yara.de.souza.lima\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

	#extraindo texto
	photo_path = photo_name + ".jpeg"
	text = pytesseract.image_to_string(cv2.imread(photo_path), lang='por+eng')
	lista_palavras_imagem = text.split()
	print(lista_palavras_imagem)


	#refatorando quebra de linha
	teste_linha = open("linha.txt", "w")
	teste_linha.write(text)
	teste_linha.close()
	teste_linha = open("linha.txt", "r")
	teste_linha = teste_linha.readlines()


	text = "".join(teste_linha)
	text = text.replace('\n', "<br>")

	html_build = "<html>" + text





	print("----------------------------------------------")

	def loads_dict(txt_name):
		d = {}
		with open(txt_name) as f:
			for line in f:
				line = line.replace('\n', "")
				dict_list = line.split(" ", 1)
				key = dict_list[0].strip('"')
				val = dict_list[1].strip('"')
				#(key, val) = line.split(" ", 1).strip('"')
				d[key] = val

		return d



	word_dict = loads_dict("dict.txt")
	print(word_dict)


	#print(lista_palavras_imagem)


	'''

	for word in lista_palavras_imagem:
		html_build = html_build + " " 
		if word in word_dict:
			translation = word_dict.get(word)
			span_build = "<span title=" + '"' + translation + '"><b>'+ word + "</b></span>" 
			html_build += span_build
		else:
			html_build += word

	html_build += "<!html>"

	'''
	print(lista_palavras_imagem)

	for word in lista_palavras_imagem:
		word = word.strip(",")
		word = word.strip(";")
		word = word.strip("!")
		word = word.strip("?")
		word = word.strip("-")
		word = word.strip(".")
		word = word.lower()
		if word in word_dict:
			print(word)
			translation = word_dict.get(word)
			span_build = "<span title=" + '"' + translation + '"><b> '+ word + "</b></span>"
			html_build = html_build.replace(" "+word, span_build)

	html_build += "<!html>"


	test_file = open("teste.html", "w")
	test_file.write(html_build)
	test_file.close()
	return html_build
