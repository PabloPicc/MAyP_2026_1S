import networkx as nx
import random

# TO-DO: completar en función de la representacion asumida para los nodos del grafo (tuplas o string)
BEG = None
END = None

def get_next_word(bot, v):
	r = random.random()
	acum = 0.0

	for w in bot.successors(v):
		acum = acum + bot[v][w]['weight']
		if r <= acum:
			return w


def simulate_comment(bot):
	word = BEG
	ret = word

	# Completar la simulacion. Debe terminar cuando la ultima palabra agregada es END


	# Retornar el comentario generado.
	return ret

def main():

	name = 'debate'
	graph_file = name + '.gml'

	# Lee el digrafo
	bot = nx.read_gml(graph_file)
	# Si se utilizan tuplas como nodos, usar la siguiente linea
	# bot = nx.read_gpickle(graph_file)

	# Simula un comentario
	comment = simulate_comment(bot)
	print(comment)

if __name__ == '__main__':
	main()
