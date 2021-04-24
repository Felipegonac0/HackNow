import function

ansiedad = 0
depresion = 0 
positivo = 0
estres = 0

def validador():

	print("""
Lo siento """ + function.apodo + " ,no entendi. Intenta con un inciso valido " + """
""")

def test():

	global ansiedad
	global depresion
	global positivo
	global estres

	Q_1()
	Q_2()
	Q_3()
	Q_4()
	Q_5()
	Q_6()
	Q_7()
	Q_8()
	Q_9()
	Q_10()
	Q_11()
	Q_12()


########################################################################################################

def Q_1():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""
1) Realizas un trabajo en equipo, pero no sale como lo esperabas, que sucede?


A) Me enojo porque yo queria algo mas 

B) Siento que fue por mi culpa y me desaliento 

C) Busco saber en que me equivoque y mejoro

""") 
	
	q_1 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_1.upper() == "A": 

		ansiedad = ansiedad + 1

	elif q_1.upper() == "B":

		depresion = depresion + 1

	elif q_1.upper() == "C":

		positivo = positivo + 1 

	else:
		validador()
		Q_1()

########################################################################################################

def Q_2():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""
2) Vas a exponer en frente a una multitud, que sucede?

A) Me tranquilizo porque se que estoy preparado 

B) Voy, pero siento que no lo voy hacer bien

C) Siento como si se me acabase el aire


""") 
	
	q_2 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_2.upper() == "A": 

		positivo = positivo + 1

	elif q_2.upper() == "B":

		depresion = depresion + 1

	elif q_2.upper() == "C":

		estres = estres + 1 

	else:
		validador()
		Q_2()

########################################################################################################

def Q_3():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

3) Como soy cuando conozco a gente nueva?

A) Me pongo a pensar en si me van a ver raro 

B) Me presento con ellos y trato de convivir con ellos 

C) Quisiera acercarme a ellos, pero siento que no soy suficiente 

""") 
	
	q_3 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_3.upper() == "A": 

		ansiedad = ansiedad + 1

	elif q_3.upper() == "B":

		positivo = positivo + 1

	elif q_3.upper() == "C":

		depresion = depresion + 1 

	else:
		validador()
		Q_3()

########################################################################################################

def Q_4():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

4) Estas discutiendo con un amigo y te dice que si no les das la razon deja de ser tu amigo, que hace?

A) Le doy la razon, no quiero que me odie 

B) Me entristezco y pienso que no merezco a nadie

C) Me alejo de el, se que hay mejores personas con las que estar 


""") 
	
	q_4 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_4.upper() == "A": 

		ansiedad = ansiedad + 1

	elif q_4.upper() == "B":

		depresion = depresion + 1

	elif q_4.upper() == "C":

		positivo = positivo + 1 

	else:
		validador()
		Q_4()

########################################################################################################

def Q_5():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

5) Hay un rumor de que le gustas a tu crush, que piensas?

A) Me quedo en shock, no puedo pensar y me preocupo

B) Me emociono y pienso en que tengo una oportunidad 

C) Me pongo a pensar de que tal vez sea falso o me intentan enganar

""") 
	
	q_5 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_5.upper() == "A": 

		estres = estres + 1

	elif q_5.upper() == "B":

		positivo = positivo + 1

	elif q_5.upper() == "C":

		ansiedad = ansiedad + 1 

	else:
		validador()
		Q_5()

########################################################################################################

def Q_6():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

6) A lo largo de este mes, Que tan bien descansado te sientes?

A) He dormido bien, pero aun asi me siento cansado 

B) Tengo varias cosas en las que pensar que no he dormido mucho

C) He dormido bien y me siento descansado


""") 
	
	q_6 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_6.upper() == "A": 

		depresion = depresion + 1

	elif q_6.upper() == "B":

		estres = estres + 1

	elif q_6.upper() == "C":

		positivo = positivo + 1 

	else:
		validador()
		Q_6()

########################################################################################################

def Q_7():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

7) A lo largo de la semana te has dado un tiempo para descansar?

A) Si, eso me ayuda a liberarme y concentrarme 

B) No, tengo muchas cosas que hacer y quiero acabarlo ya

C) No, porque se me acumula el trabajo y me agobio 

""") 
	
	q_7 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_7.upper() == "A": 

		positivo = positivo + 1

	elif q_7.upper() == "B":

		ansiedad = ansiedad + 1

	elif q_7.upper() == "C":

		estres = estres + 1 

	else:
		validador()
		Q_7()

########################################################################################################

def Q_8():
	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

8) Actualmente sientes que lo que haces no es suficiente?

A) Siento que lo que hago no es suficiente

B) Siento que yo no soy suficiente

C) Siento que soy importante

""") 
	
	q_8 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_8.upper() == "A": 

		ansiedad = ansiedad + 1

	elif q_8.upper() == "B":

		depresion = depresion + 1

	elif q_8.upper() == "C":

		positivo = positivo + 1 

	else:
		validador()
		Q_8()
########################################################################################################

def Q_9():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

9)  Has sentido que no te puedes concentrarte ultimamente?

A) No, me siento muy enfocado

B) Si, solo me he podido centrar en un tema y me bloqueo 

C) Si, pero porque no siento que pueda hacerlo 

""") 
	
	q_9 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_9.upper() == "A": 

		positivo = positivo + 1

	elif q_9.upper() == "B":

		estres = estres + 1

	elif q_9.upper() == "C":

		depresion = depresion + 1 

	else:
		validador()
		Q_9()

########################################################################################################

def Q_10():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

10) Has sentido momentos de preocupacion irracional?

A) Si, pero despues de un tiempo se me pasa

B) No, solo me preocupo de vez en cuando pero lo suficiente

C) Si, y siento como si aquella sensacion no acabase y estuviese en un bucle 

""") 
	
	q_10 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_10.upper() == "A": 

		estres = estres + 1

	elif q_10.upper() == "B":

		positivo = positivo + 1

	elif q_10.upper() == "C":

		ansiedad = ansiedad + 1 

	else:
		validador()
		Q_10()

########################################################################################################

def Q_11():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

11) He sentido una necesidad irracional de hacer mas cosas?

A) No he sentido esa necesidad 

B) Siento que deberia de hacer mas pero no tengo la energia suficiente 

C) Si, pero no se el que y me preocupa

""") 
	
	q_11 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_11.upper() == "A": 

		positivo = positivo + 1

	elif q_11.upper() == "B":

		depresion = depresion + 1

	elif q_11.upper() == "C":

		estres = estres + 1 

	else:
		validador()
		Q_11()

########################################################################################################

def Q_12():

	global ansiedad
	global depresion
	global positivo
	global estres

	print("""

12)  Normalmente piensas demasiado en el...

A) Presente y todo lo que hay que hacer ya 

B) Futuro y lo que va suceder dependiendo por cada pequena cosa que haga

C) Pienso lo necesario acerca de mi futuro y presente

""") 
	
	q_12 = raw_input("Escribe el inciso de tu opcion: ") 
	
	if q_12.upper() == "A": 

		estres = estres + 1

	elif q_12.upper() == "B":

		ansiedad = ansiedad + 1

	elif q_12.upper() == "C":

		positivo = positivo + 1 

	else:
		validador()
		Q_12()
