########################################################################################################
nombre = ""
apodo = ""
def names():

	global nombre 
	global apodo

	nombre = input("Cual es tu nombre completo? ")
	print ("")
	apodo = input("Como te gustaria que te llamara? ")
	print ("")

########################################################################################################

# Evaluacion RULER

agrado_i = 0
energia_i = 0
# agrado_r es para la seleccion // agrado_i es para la evaluacion en RULER

def agrado():
	
	global agrado_i

	agrado_r = input("Escribe el inciso de tu opcion: ") 
	
	if agrado_r.upper() == "A": 

		agrado_i = agrado_i + 1

	elif agrado_r.upper() == "B":

		agrado_i = 0 

	else:

		print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un inciso valido " + """
""")
		agrado()

# energia_r es para la seleccion // energia_i es para la evaluacion en RULER

def energia():

	print (""" 
Cuanta energia tienes en una escala del 1 al 10?
		""")

	energia_r = input("Escribe el numero en la escala: ")
	
	global energia_i

	if energia_r.isdigit() or energia_r.startswith('-') and energia_r[1:].isdigit():

		if int(energia_r) >= 6 and int(energia_r) <= 10: 

			energia_i = energia_i + 1

		elif int(energia_r) >= 1 and int(energia_r) <= 5:

			energia_i = 0 

		elif int(energia_r) < 1 or int(energia_r) > 10: 

			print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un numero dentro de la escala " + """
""")
			energia()

	else:

		print("""
Lo siento """ + apodo + " ,no entendi. Intenta insertar un numero " + """
""")
		energia() 

r_cuadrant = "NONE"

def ruler_c(): 

	global r_cuadrant

	if agrado_i == 1 and energia_i == 1: 

		r_cuadrant = "Cuadrante amarillo"

	elif agrado_i == 1 and energia_i == 0: 

		r_cuadrant = "Cuadrante verde"

	elif agrado_i == 0 and energia_i == 1: 

		r_cuadrant = "Cuadrante rojo"

	elif agrado_i == 0 and energia_i == 0: 

		r_cuadrant = "Cuadrante azul"

# El codigo abajo es solo para verificar la modificacion de variables con las funciones anteriores

"""print("agrado_i: " + str(function.agrado_i) + " energia_i: " + str(function.energia_i))

print("Cudrante RULER identificado: " + function.r_cuadrant)"""
########################################################################################################

#EDAD
edad = ""

def edad():

	global edad 

	edad_r = input("Cual es tu edad? ")

	if edad_r.isdigit():

		if int(edad_r) >= 18 and int(edad_r) <= 100:
		
			edad = edad_r
	
		if int(edad_r) < 18: 

			print(apodo + ", pide ayuda a tu tutor legal para poder continuar con tu diagnostico")

			exit()

		if int(edad_r) > 100:

			print(apodo + """, pide ayuda a un adulto de confianza para continuar. 
En caso de que colocaste mal tu edad intentalo de nuevo""")
			edad()

	else: 
		print("""
Lo siento """ + apodo + " ,no entendi. Intenta insertar un numero " + """
""")
		edad()


########################################################################################################

#GENERO

genero = ""

def genero_f():

	print (apodo + """, con que genero te identificas?

a) Mujer 

b) Hombre

c) otro 

""")
	
	global genero

	genero_r = input("Escribe el inciso de tu opcion: ") 
	
	if genero_r.upper() == "A": 

		genero = "Mujer"

	elif genero_r.upper() == "B":

		genero = "Hombre" 

	elif genero_r.upper() == "C":

		genero = "Otro"

	else:

		print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un inciso valido " + """
""")
		genero_f()	

########################################################################################################

#SEXO

sexo= "NONE"

def sexo():
	
	global sexo
	
	print("""Con que sexo naciste?

a) Macho (XX)

b) Hembra (XY)

c) Otro

		""")

	sexo_r = input("Escribe el inciso de tu opcion: ")

	if sexo_r.upper() == 'A':
		
		sexo = "Macho"

	elif sexo_r.upper() == 'B':
		
		sexo = "Hembra"

	elif sexo_r.upper() == 'C':
		
		sexo = "Otro"
	
	else:
		print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un inciso valido " + """
""")

		sexo()

########################################################################################################

#MEDICAMENTOS

medicamentos = False 
lista_med = "No toma medicamentos"

def medicamentos():
	
	global medicamentos
	global lista_med
	
	print("""Estas tomando medicamentos?
a) Si
b) No

""")

	medicamentos_r = input("Escribe el inciso de tu opcion: ")

	if medicamentos_r.upper() == 'A':
		
		print("De acuerdo ")
		
		medicamentos = True
		
		lista_med_r = input("Puedes poner los nombres de los medicamentos que consumes en estos momentos: ")
		
		lista_med = lista_med_r

	elif medicamentos_r.upper()== 'B':

		medicamentos = False

	else:
		print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un inciso valido " + """
""")

		medicamentos()

########################################################################################################

#Psicologo

toma_terapia = "No aplica"
tiempo_t = ""


def psicologo():
	
	terapia = False
	alta = False

	global toma_terapia
	global tiempo_t
	
	print("""Alguna vez has asistido al psicologo? 
(Recuerda que no tiene nada de malo pedir ayuda, todos la necesitamos en algun momento)

a) Asisto actualmente
b) Asisti
c) Nunca he asistido

""")

	terapia_r = input("Escribe el inciso de tu opcion: ")

	if terapia_r.upper() == 'A':
		
		print("Me podrias decir durante cuantas semanas has estado asistiendo? ")
		
		terapia = True
		alta = False
		
		tiempo_t_r = input("Coloca el numero de semanas: ")
		
		if tiempo_t_r.isdigit():

			if int(tiempo_t_r) >= 1:

				tiempo_t = tiempo_t_r

			else:

				print(apodo + """,
ingresa un numero positivo o mayor a 0, por favor """)
				psicologo()	
		else:

			print (apodo + """, 
ingresa un numero valido""")

	elif terapia_r.upper() == 'B':

		
		print("Me podrias decir durante cuantas semanas asististe? ")
		
		terapia = True
		alta = True
		
		tiempo_t_r = input("Coloca el numero de semanas: ")
		
		if tiempo_t_r.isdigit():

			if int(tiempo_t_r) >= 1:

				tiempo_t = tiempo_t_r

			else:

				print(apodo + """,
ingresa un numero positivo o mayor a 0, por favor """)
				psicologo()

		else:

			print(apodo + """,
ingresa un numero valido, por favor """)
			psicologo()

	elif terapia_r.upper()== 'C':

		terapia = False
		alta = False

	else:
		print("""
Lo siento """ + apodo + " ,no entendi. Intenta con un inciso valido " + """
""")
		psicologo()



	if terapia == True and alta == True:

		toma_terapia = "Asistio" 

	elif terapia == True and alta == False:

		toma_terapia = "Asiste"

	else:

		toma_terapia = "No ha tomado terapia"

########################################################################################################

texto = "NONE"

def texto_abierto():

	global texto

	print ("""Ahora """ + apodo + """, puedes describirme en al menos un parrafo como te has sentido en los ultimos 3 dias?""")

	texto_r = input("""Escribelo aqui tu respuesta """ + apodo + """: """)

	texto = texto_r.lower()

keyword_dict = {
	
	"Triste": ["tristeza", "decaido", "sin ganas"],
	"Feliz" : ["positivo", "relajado", "contento"],
	"Enojo": ["ira", "rabia",]

}

