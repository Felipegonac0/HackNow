import function
import test 
import evaluador

from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

print ("""

Hola, soy Dulas

Estoy aquí para saber como te sientes

""")

function.names()

answers = {
	
	"Triste": ["tristeza", "decaido", "sin ganas"],
	"Feliz" : ["positivo", "relajado", "contento"],
	"Enojo": ["ira", "rabia",]

}

print ("Entonces " + function.apodo + ", ¿Cómo te sientes hoy?")

print ("""

¿Tu sentir es agradable o desagradable?

a) agradable

b) desagradable

""")

function.agrado()
function.energia()
function.ruler_c()

function.edad()

function.genero_f()
function.sexo()
function.medicamentos()
function.psicologo()

print("""

Listo """ + function.apodo +". Ahora voy a hacerte algunas preguntas para poder tener un mejor diagnostico ")

test.test()

evaluador.evaluador()

function.texto_abierto()

keyword_processor.add_keywords_from_dict(function.keyword_dict)

keywords = keyword_processor.extract_keywords(function.texto)



print("""

Eso fue todo """ + function.apodo + """, en un momento enviarémos tu información general y un breve diagnóstigo a un especialista de DulasAPP.


Mientras tanto te haré algunas sugerencias para que te puedas sentir mejor mientras tu diagnostico es analizado.


""" + evaluador.diagnostico_a + evaluador.diagnostico_p + evaluador.diagnostico_e + evaluador.diagnostico_d + """


Muchas gracias, y sabes que estoy aquí para tí. Te quiero """ + function.apodo + """ 


	""")






f = open("recomendaciones_dulas.txt","w+") 


f.write( """\

A quien corresponda, 

Por medio de la presente DulasApp hace llegar un diagnostico psicologico general del paciente """ + function.nombre + """. 

INFORMACIÓN GENERAL:

Nombre: """ + function.nombre + """. 

Edad: """ + str(function.edad) + """.

Género: """ + function.genero + """.

Sexo: """ + function.sexo + """.


MEDICAMENTOS: 

Consume medicamentos actualmente: """ + str(function.medicamentos) + """.

Lista de medicamentos que consume: """ + function.lista_med + """.


EMOCIONAL:

Cuadrante emocional (RULER): """ + function.r_cuadrant + """.

Terapia: """ + str(function.toma_terapia) + """.

Tiempo en terapia (Semanas): """ + str(function.tiempo_t) + """.


RESULTADOS ARROJADOS POR EL TEST: 

Ansiedad: """ + str(test.ansiedad) + """

Depresión: """ + str(test.depresion) + """

Positivo: """ + str(test.positivo) + """

Estrés: """ + str(test.estres) + """

Recomendaciones dadas por Dulas: 

""" + str(evaluador.diagnostico_a) + str(evaluador.diagnostico_p) + str(evaluador.diagnostico_e) + str(evaluador.diagnostico_d) + """


PALABRAS CLAVE ENCONTRADAS EN EL TEXTO ESCRITO: 

""" + str(keywords) + """
""")

f.close()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
# Iniciamos los parámetros del script
remitente = 'user.dulas@gmail.com'
destinatarios = ['Dulas.py.app@gmail.com']
asunto = 'Recomensaciones Dulas'
cuerpo = 'El archivo adjunto contiene info de un solicitante '
ruta_adjunto = 'recomendaciones_dulas.txt'
nombre_adjunto = 'recomendaciones_dulas.txt'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto
 
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login('user.dulas@gmail.com','Dulas2000')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()


