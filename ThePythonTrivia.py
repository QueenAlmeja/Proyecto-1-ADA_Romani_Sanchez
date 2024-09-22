import random

preguntas_respuestas = [
    ("¿Cuál es la función para imprimir en pantalla en Python?", "print"),
    ("¿Qué símbolo se usa para asignar el valor de una variable","="),
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
    ("¿Con que extensión termina un archivo que tiene le formato Python?",".py"),
    ("¿Se considera que Python es un lenguaje de programacion de bajonivel, nivel medio o altonivel?","altonivel"),
    ("¿De que país proviene el creador de Python? ","holanda"),
]
def greeting():
    print("¡Bienvenido al 🎮 de preguntas sobre Python! 🐍")
    print("Para ganar 🏆, debes responder la mayoría de las preguntas correctamente 🤓✅")
    print("¡Veamos si eres un buen Padawan en tu camino a la programación con Python 🐍\n")

def user():
    name = input("¿Cuál es tu nombre?: ").capitalize()
    age = float(input("¿Cuántos años tienes?: "))
    if age >= 18:
        print(f"Bienvenido {name} a la trivia de Python 🐍. Prepárate para saber cuánto sabes de este lenguaje de programación.\n")
        print(f"{name}, tienes 3 vidas ❤️ para ganar. Cada vez que contestes mal, se te restara una vida. Asi que usalas con sabiduria 🦉 \n")
        return True
    else:
        print("Lo siento, debes tener al menos 18 años para jugar.")
        return False
    
def python_game():
    vidas = 3
    puntos = 0
    preguntas = preguntas_respuestas.copy()  
    random.shuffle(preguntas)  
   
    for i in range(16):  
        pregunta, respuesta_correcta = preguntas[i]
        print(f"Pregunta {i+1}: {pregunta}")
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        
        if respuesta_usuario == respuesta_correcta.lower():
            puntos += 1
            print("Correcto, sigue avanzando. ¡Tú puedes hacerlo! 💪🏻\n")
        else:
            vidas -= 1
            print("Has fallado, debes repasar esto 💡\n")
        
        if vidas == 0:
            print("Has perdido todas tus vidas. ¡Fin del juego!\n")
            break
    
    if puntos >= 13:
        print(f"¡Felicidades! Has ganado con {puntos} puntos. Sigue estudiando Python 🎉")
        print("Sigue tu camino joven Padawan, vas muy bien 💚🎮")
    else:
        print(f"Has conseguido {puntos} puntos. Necesitas estudiar más. ¡Sigue intentándolo!\n")

greeting()
if user():
    python_game()