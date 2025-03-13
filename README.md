# README - Analizador1.py

## Descripción
`Analizador1.py` es un analizador léxico escrito en Python. Su objetivo es analizar el contenido de un archivo de código fuente (`Prueba.py`) y reconocer tokens, palabras reservadas, identificadores, números y operadores.

## Características
- Detecta y clasifica tokens comunes como operadores, símbolos y signos de puntuación.
- Reconoce palabras reservadas del lenguaje Python.
- Identifica identificadores y números enteros.
- Maneja correctamente comentarios y cadenas de texto.
- Reporta errores léxicos en caso de encontrar caracteres no válidos.

## Estructura del Código
1. **Definición de Tokens**: Un diccionario con los símbolos y operadores reconocidos.
2. **Palabras Reservadas**: Conjunto de palabras clave del lenguaje Python.
3. **Verificación de Identificadores**: Función para determinar si una cadena es un identificador válido.
4. **Función `analizar_lexico(codigo)`**:
   - Recorre el código línea por línea.
   - Detecta y clasifica los distintos tipos de tokens.
   - Imprime el resultado del análisis léxico.
5. **Carga de Archivo**: Lee el contenido de `Prueba.py` y lo analiza léxicamente.

## Ejecución
Para ejecutar el analizador léxico, asegúrate de que el archivo `Prueba.py` contiene el código fuente que deseas analizar y luego ejecuta:
```bash
python Analizador1.py
```

## Salida Esperada
El analizador imprimirá los tokens detectados con su tipo y posición en el código. Ejemplo:
```
<id, variable, 1, 1>
<tkn_asig, =, 1, 10>
<numero_entero, 42, 1, 12>
```

Si encuentra un error léxico, mostrará un mensaje como:
```
>>>Error léxico(Fila:2,Columna:5)
```

## Requisitos
- Python 3.x



