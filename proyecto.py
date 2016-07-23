import numpy as np
import math
import random

######################################
# Los datos comienzan en el año 2012 #
######################################

poblacion = [10216431, 10248467, 10272182]

provincias = ["Pinar del Río", "La Habana", "Matanzas", 
			  "Cienfuegos", "Sancti Spiritus", "Villa Clara",
			  "Camaguey", "Las Tunas", "Holguín",
			  "Santiago de Cuba", "Granma", "Guantánamo", "Ciego de Ávila"]																												   

paises = ["EEUU", "Canada", "Mexico", "Guatemala", "Honduras", "El Salvador", "Nicaragua", 
		"Costa Rica", "Panama", "Venezuela", "Trinidad & Tobago", "Colombia", "Ecuador", 
		"Peru", "Brasil", "Bolivia", "Chile", "Argentina", "Bahamas", "Puerto Rico", 
		"Republica Dominicana", "Haiti", "Jamaica", "Islandia", "Noruega", "Suecia", 
		"Finlandia", "Rusia", "Estonia", "Letonia", "Dinamarca", "Reino Unido", "Irlanda", 
		"Bielorrusia", "Polonia", "Alemania", "Holanda", "Belgica", "Luxemburgo", "Francia", 
		"Espana", "Portugal", "Austria", "Republica Checa", "Eslovaquia", "Suiza", "Hungria", 
		"Rumania", "Eslovenia", "Italia", "Serbia", "Bulgaria", "Grecia", "Turquia", "Chipre", 
		"Argelia", "China", "Guinea", "Republica del Congo", "Angola", "Namibia", "Sudafrica", 
		"Australia", "Ucrania", "Albania", "Groenlandia"]


#Población de Cuba por provincias
poblacion_provincias = [[587236, 588296, 589664],
						[2105291, 2117343, 2121871],
						[694759, 699215, 702477],
						[404356, 405823, 406911],
						[463784, 465164, 466431],
						[791681, 792292, 792408],
						[771631, 773148, 774766],
						[533419, 535021, 536812],
						[1036613, 1037770, 1038739],
						[1050401, 1053914, 1057402],
						[835414, 836144, 837351],
						[515883, 515898, 516302],
						[425963, 428439, 431048]]

#defunciones por provincias
defunciones_provincias = [
				[4285, 4318, 4630],
				[27343, 28218, 28724],
				[5652, 5706, 6003],
				[3149, 3203, 3384],
				[3886, 3987, 4091],
				[7124, 7308, 7169],
				[6042, 6242, 6381],
				[3499, 3457, 3662],
				[6972, 7081, 7427],
				[7320, 7591, 8021],
				[5491, 5764, 5948],
				[3166, 3244, 3453],
				[3115, 3253, 3376],
]

#Migraciones Internas
migraciones_internas = [
				[[0, 0], [956, 747], [110, 54], [33, 17], [34, 21], [35, 29], [38, 20], [17, 23], [52, 27], [37, 51], [29, 27], [35, 13], [27, 13]],
				[[291, 317], [0, 0], [463, 313], [206, 117], [233, 160], [361, 228], [366, 259], [278, 145], [445, 310], [335, 344], [416, 244], [291, 184], [246, 173]],
				[[40, 28], [693, 443], [0, 0], [171, 121], [122, 99], [350, 242], [174, 103], [96, 60], [180, 104], [156, 164], [198, 184], [115, 91], [116, 264]],
				[[31, 26], [398, 302], [244, 163], [0, 0], [147, 155], [419, 271], [110, 54], [57, 32], [62, 58], [51, 60], [53, 40], [28, 16], [55, 28]],
				[[35, 19], [472, 303], [217, 118], [172, 127], [0, 0], [691, 467], [148, 77], [41, 31], [111, 93], [27, 41], [70, 46], [21, 25], [358, 222]],
				[[28, 21], [826, 614], [691, 474], [494, 322], [570, 416], [0, 0], [128, 79], [64, 66], [68, 66], [21, 42], [50, 41], [29, 36], [186, 89]],
				[[64, 46], [1200, 833], [438, 273], [167, 88], [299, 153], [212, 125], [0, 0], [687, 367], [396, 220], [193, 180], [314, 211], [211, 92], [816, 482]],
				[[29, 22], [771, 619], [271, 173], [86, 80], [104, 104], [110, 116], [796, 502], [0, 0], [559, 410], [113, 107], [230, 165], [70, 38], [197, 187]],
				[[67, 35], [2182, 1645], [591, 409], [156, 89], [318, 241], [162, 125], [622, 380], [599, 475], [0, 0], [336, 306], [376, 249], [329, 209], [554, 417]],
				[[43, 40], [1460, 1837], [525, 551], [179, 142], [105, 99], [102, 90], [342, 308], [128, 131], [441, 393], [0, 0], [360, 345], [263, 220], [316, 346]],
				[[54, 41], [1855, 1454], [856, 628], [139, 84], [186, 156], [177, 120], [525, 298], [289, 214], [448, 321], [301, 349], [0, 0], [89, 62], [547, 438]],
				[[44, 42], [1628, 1247], [531, 422], [119, 108], [151, 183], [84, 79], [387, 286], [148, 89], [497, 321], [395, 408], [136, 89], [0, 0], [358, 528]],
				[[24, 25], [588, 438], [172, 152], [80, 76], [371, 275], [183, 184], [555, 298], [118, 74], [264, 175], [95, 119], [218, 120], [126, 80], [0, 0]],
]

migraciones_externas = [
   [(19505,9),(19505,9),(19505,9),(19505,9)],
   [(261,1),(261,1),(261,1),(261,1)],
   [(304,6),(304,6),(304,6),(304,6)],
   [(50,1),(50,1),(50,1),(50,1)],
   [(8,0),(8,0),(8,0),(8,0)],
   [(2,0),(2,0),(2,0),(2,0)],
   [(16,4),(16,4),(16,4),(16,4)],
   [(102,0),(102,0),(102,0),(102,0)],
   [(49,1),(49,1),(49,1),(49,1)],
   [(197,3),(197,3),(197,3),(197,3)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(31,3),(31,3),(31,3),(31,3)],
   [(52,1),(52,1),(52,1),(52,1)],
   [(16,1),(16,1),(16,1),(16,1)],
   [(43,0),(43,0),(43,0),(43,0)],
   [(31,1),(31,1),(31,1),(31,1)],
   [(53,3),(53,3),(53,3),(53,3)],
   [(19,3),(19,3),(19,3),(19,3)],
   [(7,0),(7,0),(7,0),(7,0)],
   [(230,2),(230,2),(230,2),(230,2)],
   [(66,2),(66,2),(66,2),(66,2)],
   [(43,15),(43,15),(43,15),(43,15)],
   [(31,5),(31,5),(31,5),(31,5)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(17,0),(17,0),(17,0),(17,0)],
   [(47,0),(47,0),(47,0),(47,0)],
   [(10,0),(10,0),(10,0),(10,0)],
   [(38,33),(38,33),(38,33),(38,33)],
   [(0,0),(0,0),(0,0),(0,0)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(8,0),(8,0),(8,0),(8,0)],
   [(46,1),(46,1),(46,1),(46,1)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(4,2),(4,2),(4,2),(4,2)],
   [(250,5),(250,5),(250,5),(250,5)],
   [(23,0),(23,0),(23,0),(23,0)],
   [(12,0),(12,0),(12,0),(12,0)],
   [(0,0),(0,0),(0,0),(0,0)],
   [(82,2),(82,2),(82,2),(82,2)],
   [(2160,78),(2160,78),(2160,78),(2160,78)],
   [(27,0),(27,0),(27,0),(27,0)],
   [(15,0),(15,0),(15,0),(15,0)],
   [(7,3),(7,3),(7,3),(7,3)],
   [(2,0),(2,0),(2,0),(2,0)],
   [(56,0),(56,0),(56,0),(56,0)],
   [(10,1),(10,1),(10,1),(10,1)],
   [(1,1),(1,1),(1,1),(1,1)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(577,4),(577,4),(577,4),(577,4)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(5,2),(5,2),(5,2),(5,2)],
   [(6,0),(6,0),(6,0),(6,0)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(1,0),(1,0),(1,0),(1,0)],
   [(0,1),(0,1),(0,1),(0,1)],
   [(0,5),(0,5),(0,5),(0,5)],
   [(4,0),(4,0),(4,0),(4,0)],
   [(9,0),(9,0),(9,0),(9,0)],
   [(0,2),(0,2),(0,2),(0,2)],
   [(11,0),(11,0),(11,0),(11,0)],
   [(28,0),(28,0),(28,0),(28,0)],
   [(15,0),(15,0),(15,0),(15,0)],
   [(0,10),(0,10),(0,10),(0,10)],
   [(0,2),(0,2),(0,2),(0,2)],
   [(0,1),(0,1),(0,1),(0,1)],
]

#Nacimientos anuales por Provincias
nacimientos_provincias = [[6745, 6465, 6480],
						  [5818 + 19561 + 4008, 5732 + 20198 + 4096, 5714 + 19176 + 4009],
						  [7574, 7473, 7325],
						  [4352, 4362, 4266],
						  [5039, 5062, 5093],
						  [7872, 7909, 7825],
						  [8653, 8576, 8301],
						  [6257, 6204, 6355],
						  [11794, 11843, 11137],
						  [13849, 14125, 13825],
						  [11005, 10829, 10428],
						  [982, 1001, 998],
						  [4878, 4952, 4711]]



########################
# Migraciones Externas #
##########################################################################

migracion_externa_provincias = []

def migraciones_externas_provincias_iniciales():
	for i in range(len(poblacion_provincias)):
		migracion_externa_provincias.append([])
		for j in range(len(migraciones_externas)):
			migracion_externa_provincias[i].append([(
													int(poblacion_provincias[i][0]*migraciones_externas[j][1][0]/poblacion[0]),
													int(poblacion_provincias[i][0]*migraciones_externas[j][1][1]/poblacion[0])
													),
													(
													int(poblacion_provincias[i][1]*migraciones_externas[j][2][0]/poblacion[1]),
													int(poblacion_provincias[i][1]*migraciones_externas[j][2][1]/poblacion[1])
													),
													(
													int(poblacion_provincias[i][2]*migraciones_externas[j][3][0]/poblacion[2]),
													int(poblacion_provincias[i][2]*migraciones_externas[j][3][1]/poblacion[2])
													)])

def proporciones_iniciales_migraciones_externas():
	p = []
	for i in range(len(migracion_externa_provincias)):
		p.append([])
		for j in range(len(migracion_externa_provincias[i])):
			p[i].append([(
						float(migracion_externa_provincias[i][j][0][0])/poblacion_provincias[i][0],
						float(migracion_externa_provincias[i][j][0][1])/poblacion_provincias[i][0]
						),
						(
						float(migracion_externa_provincias[i][j][1][0])/poblacion_provincias[i][1],
						float(migracion_externa_provincias[i][j][1][1])/poblacion_provincias[i][1]
						),
						(
						float(migracion_externa_provincias[i][j][2][0])/poblacion_provincias[i][2],
						float(migracion_externa_provincias[i][j][2][1])/poblacion_provincias[i][2]
						)
						])
	return p

def actualizar_proporciones_migraciones_externas(matriz, proporciones_externas):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])): 
			a = SerieDeTiempo(matriz[i][j][-1][0],matriz[i][j][-2][0],matriz[i][j][-3][0])
			b = SerieDeTiempo(matriz[i][j][-1][1],matriz[i][j][-2][1],matriz[i][j][-3][1])
			if(proporciones_externas[i][j][0] != -1):
				a = proporciones_externas[i][j][0]
			if(proporciones_externas[i][j][1] != -1):
				b = proporciones_externas[i][j][1]
			if a < 0:
				a = 0
			if b < 0:
				b = 0
			matriz[i][j].append((a,b))
	return matriz

def actualizar_migraciones_externas(proporciones):
	for i in range(len(poblacion_provincias)):
		for j in range(len(migracion_externa_provincias[i])):
			migracion_externa_provincias[i][j].append((int(poblacion_provincias[i][-1]*proporciones[i][j][-1][0]), 
													int(poblacion_provincias[i][-1]*proporciones[i][j][-1][1])))

########################
# Migraciones Internas #
###########################################################################

def proporciones_iniciales_migraciones_internas():
	p = []
	for i in range(len(migraciones_internas)):
		p.append([])
		for j in range(len(migraciones_internas[i])):
			p[i].append([(migraciones_internas[i][j][0]/poblacion_provincias[i][-2]),
														 (migraciones_internas[i][j][1]/poblacion_provincias[i][-1])])
	return p

#Genera un nuevo valor para la matriz de migraciones internas
def actualizar_migraciones_internas(proporciones):
	#Modelo Fij = Oj*Wi
	#
	for i in range(len(migraciones_internas)):
		for j in range(len(migraciones_internas[i])):
			migraciones_internas[i][j].append(int(proporciones[i][j][-1]*poblacion_provincias[i][-1]))

def actualizar_proporciones_migraciones_internas(matriz, proporciones_internas):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			a =SerieDeTiempo(matriz[i][j][-1], matriz[i][j][-2])
			if (proporciones_internas[i][j] != -1):
				a = proporciones_internas[i][j]
			if (a< 0):
				a = 0
			matriz[i][j].append(a)
	return matriz


###############
# Nacimientos #
############################################################################

#Devuelve una lista con los nacimientos en cada provincia para el día
def nacimientos_de_hoy():
	nacimientos = []
	for i in range(len(nacimientos_provincias)):
		nacimientos.append(int(nacimientos_provincias[i][-1]/365))
	return nacimientos

#Genera el número de nacimientos para el año actual
def generar_nacimientos():
	actualizar_proporcion_nacimientos()
	actualizar_variable(poblacion_provincias, proporciones_nacimientos_provincias, nacimientos_provincias)

###############
# Defunciones #
############################################################################

def muertes_de_hoy():
	muertes = []
	for i in range(len(defunciones_provincias)):
		muertes.append(int(defunciones_provincias[i][-1]/365))
	return muertes

def generar_defunciones():
	actualizar_proporcion_defunciones()
	actualizar_variable(poblacion_provincias, proporciones_defunciones_provincias, defunciones_provincias)

########################
# Análisis Estadístico #
#############################################################################

def proporciones(a,b, c):
	for i in range(len(a)):
		c[i] = []
		c[i].append(a[i][-3] / b[i][-3])
		c[i].append(a[i][-2] / b[i][-2])
		c[i].append(a[i][-1] / b[i][-1])

#Genera las proporciones de nacimientos por provincia para el año completo.
def actualizar_proporcion_nacimientos():
	actualizar_proporcion_en_el_tiempo(proporciones_nacimientos_provincias)

def actualizar_proporcion_defunciones():
	actualizar_proporcion_en_el_tiempo(proporciones_defunciones_provincias)

#Actualiza valores de "D" usando una serie de tiempo
#Implementación para valores enteros
def actualizar_variable_en_el_tiempo(d):
	for i in range(len(d)):
		d[i].append(int(SerieDeTiempo(
										d[i][-1],
										d[i][-2],
										d[i][-3])))
		

#Actualiza valores de "D" usando una serie de tiempo
#Implementación para float
def actualizar_proporcion_en_el_tiempo(d):
	for i in range(len(d)):
		d[i].append(SerieDeTiempo(
										d[i][-1],
										d[i][-2],
										d[i][-3]))

#Serie de tiempo: proceso autoregresivo
def SerieDeTiempo(a,b,c = -1):
	a = float(a)
	b = float(b)
	if c != -1:
		c = float(c)
		promedio = (a + b + c )/3
		varianza = ((a-promedio)**2 +(b-promedio)**2 + (c-promedio)**2)/2
		proceso_autoregresivo = (3/6)*a + (2/6)*b + (1/6)*c + random.normalvariate(0,math.sqrt(varianza))
		return  proceso_autoregresivo
	else:
		promedio = (a+b)/2
		varianza = ((a-promedio)**2 +(b-promedio)**2)
		proceso_autoregresivo = (4/6)*a + (2/6)*b + random.normalvariate(0,math.sqrt(varianza))
		return proceso_autoregresivo


####################
# Actualizar Datos #
################################################################################

#Devuelve una lista con la población por provincias del último año registrado
def poblacion_actual_anual():
	poblacion_actual = []
	for i in range(len(poblacion_provincias)):
		poblacion_actual.append(poblacion_provincias[i][-1])
	return poblacion_actual

def actualizar_poblacion_anual(nueva_poblacion):
	for i in range(len(poblacion_provincias)):
		poblacion_provincias[i].append(nueva_poblacion[i])

#Genera los valores de población para el año completo
#Actualiza los valores de poblacion_diaria para el primer día del año
#Los guarda en la lista "poblacion_de_hoy"
def actualizar_valores_anuales():
	generar_nacimientos()
	generar_defunciones()

#Actualiza valores(d) 
#multiplicando totales y proporciones
def actualizar_variable(total, proporciones, d):
	for i in range(len(total)):
		d[i].append(int(total[i][-1] * proporciones[i][-1]) )

def decrecimiento_diario_flujo_migratorio_interno(i):
	return int(flujo_migratorio(i)[0]/365)

def crecimiento_diario_flujo_migratorio_interno(i):
	return int(flujo_migratorio(i)[1]/365)

def decrecimiento_diario_flujo_migratorio_externo(i):
	n = 0
	for j in range(len(migracion_externa_provincias[i])):
		n += int(migracion_externa_provincias[i][j][-1][0]/365)
	return n

def crecimiento_diario_flujo_migratorio_externo(i):
	n = 0
	for j in range(len(migracion_externa_provincias[i])):
		n += int(migracion_externa_provincias[i][j][-1][1]/365)
	return n

def migraciones_externas_anual():
	l = []
	for i in range(len(migracion_externa_provincias)):
		l.append([])
		for j in range(len(migracion_externa_provincias[i])):
			l[i].append((migracion_externa_provincias[i][j][-1][0],migracion_externa_provincias[i][j][-1][1]))
	return l

def migraciones_internas_anual():
	l = []
	for i in range(len(migraciones_internas)):
		l.append([])
		for j in range(len(migraciones_internas[i])):
			l[i].append(migraciones_internas[i][j][-1])
	return l

def proporciones_migraciones_internas_anual(pmi):
	l = []
	for i in range(len(pmi)):
		l.append([])
		for j in range(len(pmi[i])):
			l[i].append(pmi[i][j][-1])
	return l

def proporciones_migraciones_externas_anual(pme):
	l = []
	for i in range(len(pme)):
		l.append([])
		for j in range(len(pme[i])):
			l[i].append((pme[i][j][-1][0],pme[i][j][-1][1]))
	return l

###################################################################################

#Devuelve una tupla cuyo primer elemento es la cantidad
#de personas que se fueron a otras provincias
#y el segundo elemento es la cantidad de personas que se mudaron
#a esta provincia
def flujo_migratorio(provincia):
	llegan = 0
	se_van = 0
	for i in range (len(migraciones_internas)):
		se_van += migraciones_internas[provincia][i][-1]
		llegan += migraciones_internas[i][provincia][-1]
	return(se_van, llegan)


################
#  Simulación  #
##############################################################################################

#Establecer las proporciones con los datos iniciales
proporciones_nacimientos_provincias = [0 for i in range(len(provincias))]
proporciones(nacimientos_provincias, poblacion_provincias, proporciones_nacimientos_provincias)

proporciones_defunciones_provincias = [0 for i in range(len(provincias))]
proporciones(defunciones_provincias, poblacion_provincias, proporciones_defunciones_provincias)

proporciones_migraciones_internas = proporciones_iniciales_migraciones_internas()

migraciones_externas_provincias_iniciales()
proporciones_migraciones_externas = proporciones_iniciales_migraciones_externas()

l_proporciones_migraciones_internas = proporciones_migraciones_internas_anual(proporciones_migraciones_internas) 
l_proporciones_migraciones_externas = proporciones_migraciones_externas_anual(proporciones_migraciones_externas)


def simulacion(proporciones_internas, proporciones_externas):
	
	poblacion_actual = poblacion_actual_anual()
	poblacion_diaria = poblacion_actual
		
	pmi = actualizar_proporciones_migraciones_internas(proporciones_migraciones_internas, proporciones_internas)
	actualizar_migraciones_internas(pmi)

	pme = actualizar_proporciones_migraciones_externas(proporciones_migraciones_externas, proporciones_externas)
	actualizar_migraciones_externas(pme)
		
	l_migraciones_internas = migraciones_internas_anual()
	l_migraciones_externas = migraciones_externas_anual()

	#print(l_migraciones_internas)
	#print(l_migraciones_externas)
	#print(poblacion_diaria)
	actualizar_valores_anuales()
	n = 365
	while n > 0:
		n -= 1
		nacimientos = nacimientos_de_hoy()
		muertes = muertes_de_hoy()
		for i in range(len(poblacion_diaria)):
			poblacion_diaria[i] += nacimientos[i]
			poblacion_diaria[i] -= muertes[i]
			poblacion_diaria[i] -= decrecimiento_diario_flujo_migratorio_interno(i)
			poblacion_diaria[i] += crecimiento_diario_flujo_migratorio_interno(i)
			poblacion_diaria[i] -= decrecimiento_diario_flujo_migratorio_externo(i)
			poblacion_diaria[i] += crecimiento_diario_flujo_migratorio_externo(i) 
	actualizar_poblacion_anual(poblacion_diaria)
	#print(poblacion_actual_anual())
	return([(l_migraciones_internas, l_migraciones_externas), (l_proporciones_migraciones_internas, l_proporciones_migraciones_externas)])

#print(proporciones_migraciones_externas)
