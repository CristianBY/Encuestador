import tkinter as tk
from tkinter import simpledialog

application_window = tk.Tk().withdraw()
respuesta=[]

fr=open("encuesta","a",encoding="iso-8859-1")
entry=True
while entry:
	answer = None
	while answer is None:
		answer = simpledialog.askstring("Input", "¿En que ciudad vives?",
	                                parent=application_window)
		if answer is not None:
			respuesta.append(answer)
	answer=None
	while answer is None:
		answer = simpledialog.askinteger("Input", "¿Cuantos años tienes?",
	                                parent=application_window,
	                                 minvalue=0, maxvalue=100)
		if answer is not None:
			respuesta.append(answer)    
	answer= None
	while answer is None:
		answer = simpledialog.askstring("Input", "¿Que compañia de movil tienes?",
	                               parent=application_window)
		if answer is not None:
			respuesta.append(answer)
	i=1
	for v in respuesta:
		if len(respuesta)==i:
			fr.write(str(v)+"\n")
		else:
			fr.write(str(v)+":")
		i+=1
	while len(respuesta)>0:
		respuesta.pop()
	answer = simpledialog.askstring("Input","¿Finaliza la encuesta?",
								parent=application_window)
	if answer == "si" or answer == "Si":
		entry= False
fr.close()
