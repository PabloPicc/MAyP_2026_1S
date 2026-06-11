import json

def extract_comments_text(input_file, output_file):
	# 1. Abre el archivo input_file como lectura y output_file como escritura.
	# 2. Para cada linea, genera el json usando json.loads.
	# 3. Guarda el texto en el archivo de output en una nueva linea.
	# 3. Si el comentario tiene respuestas, entonces guarda el texto de cada respuesta 
	# en el archivo de output en una nueva linea.
	pass

def main():

	# Nombre del archivo
	name = 'debate'
	filename = name + '.data'

	# Extrae los comentarios de la data cruda
	comments_filename = name + '.comments.txt'
	extract_comments_text(filename, comments_filename)


if __name__ == '__main__':
	main()