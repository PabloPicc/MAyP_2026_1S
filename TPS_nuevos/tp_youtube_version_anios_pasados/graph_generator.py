from nltk.tokenize import word_tokenize
import pickle
import networkx as nx
import random
import matplotlib.pyplot as plt

BEG = '__beg__ __beg__'
END = '__end__ __end__'

def process_comments(comments_filename):
	# Toma los textos del archivo con los comentarios procesados, y devuelve una lista de lista de strings
	# con los comentarios tokenizados.
	# La posicion i de la lista principal corresponde al comentario i del archivo de entrada tokenizado.
	pass

def add_text_to_digraph(text, D):
	# Agrega un determinado texto tokenizado al grafo, actualizando correctamente los pesos del mismo.
	# Notar que algunos ejes ya podrian estar definidos de comentarios anteriores.
	# Los pesos deben ser la cantidad de apariciones del correspondiente eje (bigrama)
	# Los cambios se aplican directamente sobre D.
	pass

def generate_graph(tknzd_text):
	# Funcion general encargada de armar la primera version del grafo.
	# Llama a la funcion auxiliar add_text_to_digraph.
	pass

def adjust_out_edges_weight(D,v):
	# Funcion que se encarga de convertir los pesos de los ejes salientes de v en frecuencias.
	# Trabaja directamente sobre el grafo D.
	pass

def calculate_markov_chain(D):
	for v in D.nodes:
		adjust_out_edges_weight(D,v)

def main():

	name = 'debate'
	comments_filename = name + '.comments.txt'

	# Procesa los comentarios
	tknzd_text = process_comments(comments_filename)

	# Genera el grafo pesado
	D = generate_graph(tknzd_text)
	
	# Convierte los pesos de las aristas a probabilidades
	calculate_markov_chain(D)

	# Informacion para debug
	print('Graph statistics:', D.number_of_nodes(), D.number_of_edges())

	# Persiste en memoria el digrafo
	graph_file = name + '.gml'
	nx.write_gml(D, graph_file)
	# si se utilizan tuplas como nodos, usar la siguiente linea
	# actualizar convenientemente en bot.py
	# nx.write_gpickle(D, graph_file)

if __name__ == '__main__':
	main()