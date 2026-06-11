import os  
import google.auth  
from googleapiclient.discovery import build 
import json

# Llenar con tu api key creada en https://console.developers.google.com/
DEVELOPER_KEY = ''
 

def download(video_ids, output):

	# Crear cliente para la API de YouTube
	youtube = build('youtube', 'v3', developerKey = DEVELOPER_KEY)  

	with open(output, 'w') as file:
		for video_id in video_ids:
			# Llamo a la API para obtener los comentarios
			results = youtube.commentThreads().list(  
			    part = 'id, snippet, replies',  
			    videoId = video_id,  
			    textFormat = 'plainText',  
			    ).execute()  
			  
			# Itero sobre los comentarios  
			while results:
				for item in results['items']:
					data = json.dumps(item)
					file.write(data + "\n")

				# Checkeo si hay mas comentarios y sigo iterando
				if 'nextPageToken' in results:
					results = youtube.commentThreads().list(
						part = 'id, snippet, replies',
						videoId = video_id,
						textFormat = 'plainText',
						pageToken = results['nextPageToken']
					).execute()
				else:
					break  
	

def main():

	# ids de los videos de donde quiero descargar los comentarios
	video_ids = ['0xQ4vsDK8Hk', 'qYwlqx-JLok', '2S4QZSRoYJA', 's3WJ9AXcT4Q']
	name = 'debate'

	# Nombre del archivo para guardar los datos
	filename = name + '.data'

	# Descargo la informacion cruda
	download(video_ids, filename)


if __name__ == '__main__':
	main()