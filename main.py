import function
import test 

from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

print ("""Hola, soy Dulas
Estoy aqui para saber como te sientes""")
print ("")

function.names()



print ("Entonces " + function.apodo + ", como te sientes hoy?")

print ("""Tu sentir es agradable o desagradable?

a) agradable

b) desagradable

""")
"""
function.agrado()
function.energia()
function.ruler_c()

function.edad()

function.genero_f()
function.sexo()
function.medicamentos()
function.psicologo()

print("Listo " + function.apodo +". Ahora voy a hacerte algunas preguntas para poder tener un mejor diagnostico ")

test.test()

"""
function.texto_abierto()

keyword_processor.add_keywords_from_dict(function.keyword_dict)

keywords = keyword_processor.extract_keywords(function.texto)

"""
print("Nombre completo: " + function.nombre)
print("Apodo: " + function.apodo)
print(function.r_cuadrant)
print(function.genero)
print(function.edad)
print(function.sexo)
print("Toma medicamentos: " + str(function.medicamentos))
print("Lista Medica: " + function.lista_med)
print("Terapia: " + function.toma_terapia)
#print("Toma/o terapia: " + str(function.terapia))
print("Semanas en terapia: " + function.tiempo_t)
#print("Esta dad@ de alta: " + str(function.alta))
print("Ansiedad: " + str(test.ansiedad))
print("Depresion: " + str(test.depresion))
print("Positivo: " + str(test.positivo))
print("Estres: " + str(test.estres))
"""
#print(str(function.texto))
print(keywords)


