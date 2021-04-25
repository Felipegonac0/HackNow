import function
import test

diagnostico_a = ""
diagnostico_p = ""
diagnostico_e = ""
diagnostico_d = ""

def evaluador():

	ansiedad_d()
	depresion_d()
	positivo_d()
	estres_d()

def ansiedad_d ():

	global diagnostico_a

	if test.ansiedad >= 3 and test.ansiedad <= 5 :

		diagnostico_a = """

Te recomiendo que hagas ejercicio durante 30 minutos al día, esto de 3 a 5 días por semana, 
haz ejercicios que te mantengan activo y feliz, como por ejemplo correr o trotar.Me gustaría recomendarte una dieta en la que puedas comer carbohidratos complejos como la avena,
quinoa, panes y cereales integrales, de igual manera podrias adaptar algunos hábitos como pueden ser el mantenerse bien hidratado y agregar proteína a tu desayuno, 
de igual manera deberías evitar o al menos disminuir el consumo de alcohol y cafeína """

	elif test.ansiedad > 5:

		diagnostico_a = """ 

Te recomiendo que hagas ejercicio durante 30 minutos al día, esto de 3 a 5 días por semana, 
haz ejercicios que te mantengan activo y feliz, como por ejemplo correr o trotar.Me gustaría recomendarte una dieta en la que puedas comer carbohidratos complejos como la avena,
quinoa, panes y cereales integrales, de igual manera podrias adaptar algunos hábitos como pueden ser el mantenerse bien hidratado y agregar proteína a tu desayuno, 
de igual manera deberías evitar o al menos disminuir el consumo de alcohol y cafeína. 

Y si esta tus posibilidades consulta a un especilista"""

def depresion_d ():

	global diagnostico_d

	if test.depresion >=3 and test.depresion <=5 :

		diagnostico_d = """

Me gustaría recomendarte ejercicios aeróbicos, como correr, nadar, trotar, etc.
Ya que estos te ayudarán más que ejercicios basados en fuerza, como el levantamiento de pesas. Me gustaría recomendarte que te alimentaras de alimento ricos en triptófano como el 
pavo, pollo, lácteos, de igual manera que el magnesio es muy importante y lo puedes encontrar en cereales integrales, semillas, almendras y chocolate, 
finalmente también te recomiendo consumir alimentos con omega-3 como el salmón, los mariscos, la yema de hueva y aceite de linaza, pero busca evitar el exceso de azúcares y carbohidratos, 
así como las dietas ricas de carnes rojas y alimentos confeccionados """

	elif test.depresion > 5:

		diagnostico_d = """

Me gustaría recomendarte ejercicios aeróbicos, como correr, nadar, trotar, etc.
Ya que estos te ayudarán más que ejercicios basados en fuerza, como el levantamiento de pesas. Me gustaría recomendarte que te alimentaras de alimento ricos en triptófano como el 
pavo, pollo, lácteos, de igual manera que el magnesio es muy importante y lo puedes encontrar en cereales integrales, semillas, almendras y chocolate, 
finalmente también te recomiendo consumir alimentos con omega-3 como el salmón, los mariscos, la yema de hueva y aceite de linaza, pero busca evitar el exceso de azúcares y carbohidratos, 
así como las dietas ricas de carnes rojas y alimentos confeccionados

Y si esta tus posibilidades consulta a un especilista

"""

def positivo_d ():

	global diagnostico_p

	if test.positivo >=3 and test.positivo <=5 :

		diagnostico_p = """

Te encuentras bien, pero recuerda que puedes estar aún mejor,
realiza cualquier tipo de actividad física que te llame la atención, como bailar, 
correr o practicar algún deporte. Hola solo te quiero decir que vas bien, 
simplemente recuerda que una buena alimentación es de lo mejor para tu cuerpo mente, 
come frutas y verduras y si quieres de vez en cuando algún que otro gustito."""

	elif test.positivo > 5:

		diagnostico_p = """

Te encuentras bien, pero recuerda que puedes estar aún mejor,
realiza cualquier tipo de actividad física que te llame la atención, como bailar, 
correr o practicar algún deporte. Hola solo te quiero decir que vas bien, 
simplemente recuerda que una buena alimentación es de lo mejor para tu cuerpo mente, 
come frutas y verduras y si quieres de vez en cuando algún que otro gustito.

Y si esta tus posibilidades consulta a un especilista

"""

def estres_d ():

	global diagnostico_e

	if test.estres >=3 and test.estres <=5 :

		diagnostico_e = """ 

Me gustaría recomendarte ejercicios que involucren que estés en movimiento constante, como por ejemplo trotar, 
pero también puedes hacer alguna actividad física que te guste como bailar, practicar algún deporte, etc. Me gustaría recomendarte una dieta en que puedas comer alimento ricos en magnesio, 
tales como el chocolate, las legumbre y lentejas, de igual podrías comer tubérculos como la yuca, la papa y la calabaza y unos alimentos que te ayudaran mucho serán los arándanos y uvas,
pero eso sí, evita el exceso de azúcares y sales, así como los alimentos de comida rápida."""

	elif test.estres > 5:

		diagnostico_e = """ 

Me gustaría recomendarte ejercicios que involucren que estés en movimiento constante, como por ejemplo trotar, 
pero también puedes hacer alguna actividad física que te guste como bailar, practicar algún deporte, etc. Me gustaría recomendarte una dieta en que puedas comer alimento ricos en magnesio, 
tales como el chocolate, las legumbre y lentejas, de igual podrías comer tubérculos como la yuca, la papa y la calabaza y unos alimentos que te ayudaran mucho serán los arándanos y uvas,
pero eso sí, evita el exceso de azúcares y sales, así como los alimentos de comida rápida.

Y si esta tus posibilidades consulta a un especilista

"""




