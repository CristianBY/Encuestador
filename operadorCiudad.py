datos={}
fe=open("encuesta","r")
fs=open("mapaOperador","w")
entry = fe.readline().strip()
while entry:	
	registro = entry.split(':')
	if registro[2] not in datos.keys():
		datos[registro[2]] = registro[0]
	else:
		if registro[0] not in datos[registro[2]]: 
			datos[registro[2]] += (', '+registro[0])
	entry = fe.readline().strip()
fs.write("Compañia""%20s" % "Ciudades""\n\n")
for k in datos:
	fs.write(k+"\t\t"+datos[k]+"\n")
fe.close()
fs.close()