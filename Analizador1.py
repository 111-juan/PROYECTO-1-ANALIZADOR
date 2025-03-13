# Definición de tokens y palabras reservadas
tokens = {
    'tkn_dos_puntos': ':',
    'tkn_punto': '.',
    'tkn_asig': '=',
    'tkn_div': '/',
    'tkn_suma': '+',
    'tkn_resta': '-',
    'tkn_mult': '*',
    'tkn_modulo': '%',
    'tkn_div_asig': '/=',
    'tkn_div_entera': '//',
    'tkn_mod_asig': '%=',
    'tkn_menor_menor': '<<',
    'tkn_mayor_mayor': '>>',
    'tkn_punto_y_coma': ';',
    'tkn_coma': ',',
    'tkn_corchete_izq': '[',
    'tkn_corchete_der': ']',
    'tkn_llave_izq': '{',
    'tkn_llave_der': '}',
    'tkn_par_izq': '(',
    'tkn_par_der': ')',
    'tkn_mayor': '>',
    'tkn_menor': '<',
    'tkn_ejecuta': '->',
    'tkn_potencia': '**',
    'tkn_mayor_igual': '>=',
    'tkn_menor_igual': '<=',
    'tkn_igual': '==',
    'tkn_distinto': '!=',
    'tkn_mas_asig': '+=',
    'tkn_menos_asig': '-=',
    'tkn_mult_asig': '*=',
    'tkn_arroba': '@',
    'tkn_comentario': '#',
    'tkn_ampersand': '&',
    'tkn_interrogacion': '?',
    'tkn_tilde': '~',
    'tkn_barra_piso': '_',
    'tkn_exclamacion': '!'
}

# Palabras reservadas en Python
palabras_reservadas = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
}

# Tipos de datos
tipos_datos = {'int': 'int', 'float': 'float', 'str': 'str', 'bool': 'bool'}

# Función para verificar si es un identificador válido
def es_identificador(cadena):
    if not cadena or cadena[0].isdigit():
        return False  
    for char in cadena:
        if not char.isalnum() and char not in {'_', '.'}:  # Ahora permite puntos
            return False  
    return True

# Analizador léxico
def analizar_lexico(codigo):
    fila = 0
    columna = 0
    palabra = ''
    comentario = False
    dentro_cadena = False
    cadena_actual = ''
    
    lineas = codigo.split('\n')

    for linea in lineas:
        fila += 1
        columna = 0
        comentario = False
        palabra = ''

        while columna < len(linea):
            char = linea[columna]
            columna += 1

            if comentario:
                continue

            # Manejo de cadenas
            if dentro_cadena:
                palabra += char
                if char == cadena_actual:  # Solo cierra si es la misma comilla
                    print(f"<tkn_cadena, {palabra}, {fila}, {(columna - len(palabra)) + 1}>")
                    palabra = ''
                    dentro_cadena = False
                continue

            # Detectar inicio de cadenas con comillas simples o dobles
            if char in {'"', "'"}:
                cadena_actual = char
                palabra = char
                dentro_cadena = True
                continue

            # Manejo de comentarios
            if char == '#':
                comentario = True
                continue

            # Manejo de números
            if char.isdigit():
                inicio_numero = columna - 1
                while columna < len(linea) and linea[columna].isdigit():
                    columna += 1
                print(f"<tk_entero, {linea[inicio_numero:columna]}, {fila}, {inicio_numero + 1}>")
                palabra = ''
                continue

            # Manejo de identificadores y palabras reservadas
            if es_identificador(char):
                inicio_identificador = columna - 1
                while columna < len(linea) and es_identificador(linea[columna]):
                    columna += 1
                token = linea[inicio_identificador:columna]

                if token in palabras_reservadas:
                    print(f"<{token}, {fila}, {inicio_identificador + 1}>")
                elif token in tipos_datos:
                    print(f"<tipo_dato, {token}, {fila}, {inicio_identificador + 1}>")
                else:
                    print(f"<id, {token}, {fila}, {inicio_identificador + 1}>")
                palabra = ''
                continue

            # Manejo de operadores y símbolos especiales
            if char.isspace() or char in tokens.values():
                if palabra:
                    if palabra in palabras_reservadas:
                        print(f"<{palabra}, {fila}, {columna - len(palabra)}>")

                    elif palabra in tipos_datos:
                        print(f"<tipo_dato, {palabra}, {fila}, {columna - len(palabra)}>")

                    elif es_identificador(palabra):
                        print(f"<id, {palabra}, {fila}, {columna - len(palabra)}>")

                    else:
                        try:
                            numero_entero = int(palabra)
                            print(f"<numero_entero, {palabra}, {fila}, {columna - len(palabra)}>")
                        except ValueError:
                            print(f">>>Error léxico(Fila:{fila},Columna:{columna - len(palabra)})")
                            return
                    palabra = ''

                if char in tokens.values():
                    for token, value in tokens.items():
                        if columna >= len(value) and linea[columna - len(value):columna] == value:
                            print(f"<{token}, {fila}, {columna - len(value) + 1}>")
                            palabra = ''
                            break
            else:
                palabra += char

# Cargar el código desde un archivo
with open('Prueba.py', 'r', encoding='utf-8') as file:
    input_text = file.read()

# Realizar el análisis léxico
analizar_lexico(input_text)
