El programa pide tres números enteros y primero compara a con b.
Después compara el tercer número c para saber si debe ir al inicio, en el medio o al final.
Finalmente muestra los tres números de menor a mayor usando solamente if, else y comparaciones.


Caso	               |  Entrada	    |    Esperado	|  Mi algoritmo
Desordenados	       | 7, 2, 5	    |   2, 5, 7     |  	  ok
Desordenados al revés  | 9, 5, 1        | 	1, 5, 9	    |     ok
Repetidos	           | 5, 1, 5	    |   1, 5, 5	    |     ok
Negativos	           | -3, 5, -1	    |  -3, -1, 5	|     ok
Todos iguales	       | 4, 4, 4	    |   4, 4, 4	    |     ok

¿Cuántas comparaciones se necesitan como mínimo para ordenar tres números?

Para garantizar que tres números queden ordenados en cualquier caso, pueden ser necesarias hasta 3 comparaciones.

Por ejemplo, con:

7, 2, 5

primero podemos comparar 7 con 2, pero todavía necesitamos comparar el 5 para saber si va antes, en medio o después.

En algunos casos bastan 2 comparaciones, pero en el peor caso se necesitan 3.