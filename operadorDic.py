#diccionario de operadores para comparar con los datos recogidos
def operadorD(operador):
	miDict = {"Vodafone":["vodafone","vodafone españa","vodafone operador"], 
				"Orange":["orange","orange españa","orange operador"],
				"Simyo":["simyo","simyo españa","simyo operador"],
				"Movistar":["movistar","movistar españa","movistar operador"],
				"Amena":["amena","amena españa","amena operador"],
				"MasMovil":["masmovil","masmovil españa","masmovil operador"]}
	for key in miDict:
		if operador in miDict[key]:
			operador=key
	if operador not in miDict:
		operador="Otras"		
	return operador