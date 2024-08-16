# Planeador de Comidas y Generador de Lista de Ingredientes
Bienvenidos a mi proyecto para la materia de Pensamiento Computacional para Ingeniería  en el 1er Semestre Otoño-Invierno 2024 en el Tecnológico de Monterrey Campus Querétaro.
__ __
## **Contexto del proyecto:**

La planeación de las comidas para la semana así como la compra de los ingredientes es un proceso repetitivo el cual se realiza al menos una vez cada dos semanas en la mayoría de las familias mexicanas.

La primer mitad de este proceso se compone de **pensar en los platillos** a cocinar y  buscar una variación en sabores y proteinas que sean la alegría de la semana; por otro lado la **descomposición de los platillos y acumulación de ingredientes** para cocinarlos nos dan como resultado una lista de compras que usaremos en nuestra siguiente visita al supermercado.

El presente proyecto busca automatizar esta rutina generando una lista de desayunos, comidas y cenas sin repetición alguna, así como la entrega de una lista de ingredientes específica para todas las recetas previamente seleccionadas.  
-- --
## **Algoritmo del Programa**

-	**Entradas**
	- Orden para generar una nueva semana de comidas. (Texto String)
	- Número de dias a planear. (Número Entero)
	
-	**Proceso**
1. Pedir orden para generar semana de comidas: "Nueva".
2. Proceso empieza si recibe "Nueva".
3. Pedir número de días a planear. Ejemplo "4".

	3.1. Creación de la variable número entero:  `num_dias`
5. Obtención de recetas: `num_dias` de Desayunos.

	  4.1. Uso de la función `obten_random` la cual sortea las listas y obtiene `num_dias`  de recetas sin repetir.

6. Obtención de recetas: `num_dias` de Comidas.

	5.1. Uso de la función `obten_random` en base a  `num_dias`

8. Obtención de recetas: `num_dias` de Cenas.
	  6.1. Uso de la función `obten_random` en base a  `num_dias`

10. Llamar los ingredientes de cada receta a través de una función.
11. Colección de ingredientes de cada receta en una lista expansible.
12. Al encontrarse el mismo nombre de ingrediente su cantidad aumenta más no se agrega de nuevo a la lista.
13. Creación del archivo de texto.
14. Colocar toda la información dentro del archivo.

	  11.1. Colocar recetas Desayuno dentro del archivo de texto.

	  11.2. Colocar recetas Comida dentro del archivo de texto.

	  11.3. Colocar recetas Cena dentro del archivo de texto.

	  11.4. Colocar lista de Ingredientes justo a sus cantidades.

    
15. Guardar archivo de texto.
16. Exportar archivo de texto al usuario.
17. Finalizar el programa.
18. Si no, finalizar el programa
-	**Salidas**

	-	Lista de recetas de comidas e ingredientes. (Archivo de Texto)

-- --
**Requisitos previos para su funcionamiento:**
-	Creación de las funciones y algoritmos a utilizar.
-	Creación de las listas de recetas en Desayuno, Comida y Cena con sus respectivos ingredientes.

##	Gracias por su atención

