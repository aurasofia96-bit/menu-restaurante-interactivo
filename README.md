# Menú de Restaurante Interactivo

Programa interactivo desarrollado en Python para simular la toma de pedidos en la terminal de un restaurante, mostrando un menú dinámico y validando la selección del usuario.

## Descripción

El programa despliega de forma automática la lista de productos disponibles en el restaurante utilizando un bucle. Solicita al usuario ingresar el número del producto que desea ordenar y cuenta con un sistema de control de errores que impide avanzar si se introduce un número fuera del rango del menú, asegurando que la orden final siempre sea válida.

## Características

* Generación dinámica de la lista del menú en pantalla.
* Ajuste automático de índices (conversión de selección humana 1-6 a índice de programación 0-5).
* Bucle de validación estricta ante entradas de números inválidos.
* Modularización mediante funciones para separar la bienvenida y la obtención del producto.

## Tecnologías

* Python 3

## Cómo ejecutar

1. Clona este repositorio o descarga el archivo.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:
   python menu_restaurante.py

## Ejemplo de salida

==================================================
Bienvenidos a cookie Love.
==================================================
Menú:
1 🍔 Cheeseburger
2 🍟 Fries
3 🥤 Soda
4 🍦 Ice Cream
5 🍪 Cookie
6 🍕 Pizza

¿Que vas a ordenar? 8
Error: Valor no valido escoja un número del 1 al 6

¿Que vas a ordenar? 5
Ordenaste 🍪 Cookie

...

## Lo que practiqué

En este proyecto utilicé:
* Definición y ejecución de funciones con parámetros (`def get_item(x)`)
* Retorno de valores en funciones (`return`)
* Bucles `for` combinados con la función `range()` y `len()` para recorrer listas dinámicamente
* Bucles `while` para la validación continua de datos de entrada
* Manipulación de listas y desfase de índices (`[x-1]`)
* Formateo de cadenas de texto (f-strings)

## Próximas mejoras

* **Sistema de carrito y cuenta final:** Modificar la estructura del menú para incluir precios y permitir al usuario agregar múltiples productos a un carrito de compras, mostrando el total acumulado al finalizar.
* **Manejo de errores:** Implementar bloques de control para evitar que el programa se cierre inesperadamente si el usuario ingresa texto o letras en lugar de un número.
* **Integración con archivos externos:** Cargar el menú y los precios de forma dinámica desde un archivo (como un Excel o CSV) para permitir modificaciones fáciles sin alterar el código fuente.

## Estado del proyecto

Proyecto finalizado como práctica de Python.