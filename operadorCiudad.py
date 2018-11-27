from operadorDic import operadorD
datos={}
fe=open("encuesta","r")
fs=open("mapaOperador","w")
entry = fe.readline().strip()
while entry:	
	registro = entry.split(':')
	operador = registro[2].lower()
	operador = operadorD(operador)
	if operador not in datos.keys():
		datos[operador] = registro[0]
	else:
		if registro[0] not in datos[operador]: 
			datos[operador] += (', '+registro[0])
	entry = fe.readline().strip()
fs.write("Compañia""%20s" % "Ciudades""\n\n")
for k in datos:
	fs.write(k+"\t\t"+datos[k]+"\n")
fe.close()
fs.close()