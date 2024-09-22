#Importamos el módulo 'random' que nos permite realizar operaciones aleatorias
import random

#Definimos una lista de tuplas que contiene preguntas y respuestas correctas sobre Python que se le presentaran al usuario.
preguntas_respuestas = [
    ("¿Cuál es la función para imprimir en pantalla en Python?", "print"),
    ("¿Qué símbolo se usa para asignar el valor de una variable", "="),
    ("Que función se emplea para conocer el tipo de dato contenido en una variable", "type"),
    ("¿Qué símbolo se usa para los comentarios en una sola línea?", "#"),
    ("¿Qué tipo de dato estaría contendio dentro de la siguiente variable: age = 23.4","float"),
    ("¿Qué operador retorna un valor True sí y solo sí todas las variables comparadas sean verdaderas?","and"),
    ("¿Qué técnica nos pemrite extrar elemento de una cadena de texto","indexing"),
    ("¿Qué palabra clave se usa para definir una función en Python?", "def"),
    ("Para obtener una sublista de elementos en Python ¿qué método empleamos?","slicing"),
    ("¿Cómo se llama la estructura que permite almacenar múltiples elementos en orden en Python y me puede modificarse?", "lista"),
    ("¿Qué operador se usa para la comparación de igualdad en Python?", "=="),
    ("¿Qué palabra clave se usa para detener un ciclo?", "break"),
    ("¿Qué tipo de dato devuelve la función input?", "str"),
    ("¿Qué función se usa para obtener la longitud de un elemento en el código de Python?", "len"),
    ("¿Con que extensión termina un archivo que tiene le formato Python?","py"),
    ("¿Se considera que Python es un lenguaje de programacion de bajonivel, nivel medio o altonivel?","altonivel"),
    ("¿De qué país proviene el creador de Python?", "holanda"),
]

#Definimos la función 'greeting()' que imprime un mensaje de bienvenida al juego, además explica al jugador que debe hacer para poder ganar este juego
def greeting():
    print("¡Bienvenido al 🎮 de preguntas sobre Python! 🐍")
    print("Para ganar 🏆, debes responder la mayoría de las preguntas correctamente 🤓✅")
    print("¡Veamos 🔍 si eres un buen Padawan en tu camino a la programación con Python 🐍\n")

#Antes de comenzar a mostrar las preguntas, creamos la función 'user()'para obtener el nombre del usuario y validar si tiene la edad sufiente para participar en el juego
def user():
    #Solicitamos el nombre del usuario y empleando el metodo de str capitalize() para aseguranos que la primera letra del nombre vaya en Mayúscula
    name = input("¿Cuál es tu nombre?: ").capitalize()
    #Solicitamos la edad del usuario y empleando la funcion float, lo que nos permite convertir el dato en un numero. Decidimos usar float en vez de int por asi acaso el user pone un valor decimal
    age = float(input("¿Cuántos años tienes?: "))
    
    #Comparamos la edad ingresada por el usuario para corroborar si es mayor o igual a 18 años y dejarlo ingresar al juego usando los condicionales if, else
    if age >= 18:
        #Si es mayor de 18 años, podra ingresar al juego y recibira un mensaje de bienvenida 
        print(f"Bienvenido {name} a la trivia de Python 🐍. Prepárate para saber cuánto sabes de este lenguaje de programación.\n")
        print(f"{name}, tienes 3 vidas ❤️ para ganar. Cada vez que contestes mal, se te restara una vida. Asi que usalas con sabiduria 🦉 \n")
        return True  #Retorna True para indicar al programa que puede dejar ingresar al user y jugar
    else:
        #Si es menor de 18 años, el user no podra ingresar y el programa culminara dandole un mensaje que le indica que debe ser mayor de 18 para jugar
        print("Lo siento, debes tener al menos 18 años para jugar.")
        return False  #Retorna False para indicar que el programa debe para y el jugador no puede acceder al juego

#Aquí definimos la función principal del juego
def python_game():
    #Agregamno las variables 'vida' para contabilizar si el jugador pierde puntos si contesta mal alguna pregunta
    #Tambien agregamos la variable 'puntos' para sumar los puntos que ira ganado cada vez que responde bien alguna pregunta
    vidas = 3
    puntos = 0
    
    #Creamos una copia de la lista de preguntas para evitar modificar la original
    preguntas = preguntas_respuestas.copy()
    
    #Mezclamos las preguntas para que el orden sea aleatorio y no aparezcan en el orden en que han sido escritas.
    #Al haber importado el módulo 'random' previamente, si el usuario vuelve a jugar las preguntas no se mostran en el mismo orden que la primera ocación
    random.shuffle(preguntas)
    
    #Iniciamos el juego y empleamos el ciclo 'for' para recorrer las 16 preguntas escritas en la lista
    for i in range(16):
        #Extraemos la pregunta y respuesta extrayendo los valores de la variable 'preguntas' declaradamente
        pregunta, respuesta_correcta = preguntas[i]
        #la variable 'pregunta' contendra el texto de la pregunta que es el primer elemento de cada tupla creada
        #la variable 'respuesta_correcta' mostrar el texto de la pregunta y comparar el contenido de este con la respuesta dada por el user
        
        #Mostramos la pregunta al usuario
        print(f"Pregunta {i+1}: {pregunta}")
        
        #Recibimos la respuesta del usuario y la normalizamos usando la funcion strip()
        #Ademas nos aseguramos que la palabra sea en minúsculas con la funcion lower() ya que las todas respuestas están escritas en minúsculas
        respuesta_usuario = input("Tu respuesta: ").strip().lower() 
       
        #Comparamos la respuesta del usuario con la respuesta correcta
        if respuesta_usuario == respuesta_correcta.lower():
            #Si es correcta, sumamos un punto a la variable 'puntos' y damos un mensaje positivo
            puntos += 1
            print("Correcto, sigue avanzando. ¡Tú puedes hacerlo! 💪🏻\n")
        else:
            #Si es incorrecta, restamos un valor a la variable 'vida' y damos un mensaje de error
            vidas -= 1
            print("Has fallado, debes repasar esto 💡\n")
        
        #Si el jugador pierde todas las vidas, terminamos el juego antes de seguir con las preguntas
        if vidas == 0:
            print("Has perdido todas tus vidas. ¡Fin del juego!\n")
            break  # Salimos del bucle si las vidas llegan a 0
    
    #Una vez terminadas las preguntas o si se pierden las vidas, evaluamos el puntaje
    if puntos >= 13:
        # Si tiene 13 o más respuestas correctas, el jugador gana
        print(f"¡Felicidades! Has ganado con {puntos} puntos. Sigue estudiando Python 🎉")
        print("Sigue tu camino joven Padawan, vas muy bien 💚🎮")
    else:
        #Si tiene menos de 13 puntos, el jugador pierde y se le motiva a seguir aprendiendo
        print(f"Has conseguido {puntos} puntos. Necesitas estudiar más. ¡Sigue intentándolo!\n")

#Para finalmente comenzar el juego debemos llamar las funciones que hemos creado.
# Comenzamos llamando a la función de bienvenida greeting() para saludar a la persona
greeting()

#Deespues de dar el saludo inicial, llamamos a la función que le va a solicitar el nombre y la edad al user 
#Ademas que corroborara si el user tiene 18 o mas años para jugar
if user():
    #Y cuncluimos llamando a la funcion donde se ejecuta las preguntas aleatoriamente al llamar a la funcion python_game()
    python_game()
