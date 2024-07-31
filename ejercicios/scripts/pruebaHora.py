from datetime import datetime

fechaActual=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('/workspaces/exercise-terminal-challenge/ejercicios/helloWorld.py',"a") as archivo:
	archivo.write(f'Tarea finalizada a las {fechaActual}')
