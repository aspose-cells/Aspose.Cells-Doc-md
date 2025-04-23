---  
title: Excel – Estilo de referencia R1C1 vs. A1 con C++  
linktitle: Excel  Estilo de Referencia R1C1 vs. A1  
type: docs  
weight: 30  
url: /es/cpp/r1c1-reference-style-vs-a1/  
description: Estilo de referencia R1C1 vs. estilo A1 usando Aspose.Cells con C++.  
keywords: Estilo de referencia R1C1 VS. estilo A1, Estilo de referencia R1C1, Cómo cambiar entre el estilo de referencia R1C1 y el estilo de referencia A1, Estilo de referencia A1  
---  

## **Introducción**

En Excel, R1C1 y A1 son dos estilos de referencia diferentes utilizados para identificar celdas en una hoja de cálculo. Tenga en cuenta que la elección entre A1 y R1C1 es en gran medida una cuestión de preferencia personal. La mayoría de los usuarios están más familiarizados con el estilo A1, pero R1C1 puede ser útil en ciertas situaciones, especialmente al trabajar con fórmulas y cálculos.

## **Estilo de Referencia A1**

Este es el estilo de referencia predeterminado en Excel. En estilo A1, las columnas se identifican mediante letras (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), y las filas mediante números (1, 2, 3, ...). Por ejemplo, la celda en la primera columna y segunda fila se refiere como A2.

## **Estilo de Referencia R1C1**

En el estilo R1C1, tanto las filas como las columnas se identifican por números. La letra "R" representa el número de fila y la letra "C" representa el número de columna. Por ejemplo, R2C1 se refiere a la celda en la segunda fila y primera columna.

Cualquier número entre corchetes se refiere a la distancia relativa desde la celda actual. A diferencia de A1 que se refiere a columnas seguidas por el número de fila, R1C1 hace lo contrario: filas seguidas por columnas (lo que requiere cierto tiempo para acostumbrarse). Los números positivos se referirán a celdas debajo y/o a la derecha. Los números negativos se referirán a celdas arriba y/o a la izquierda.

Por ejemplo, R[2]C[3] es una celda a 2 filas abajo y 3 columnas a la derecha. R[-1]C[-4] es una celda 1 fila arriba y 4 columnas a la izquierda. Si no se muestra ningún número entre corchetes, entonces te estás refiriendo a la misma fila o columna, por ejemplo, R[3]C será una celda 3 filas debajo de la celda actual en la misma columna.  
<br>  
<image src="2.png" width="70%" />  

## **Comparación entre Estilo de Referencia R1C1 y Estilo de Referencia A1**  
Aquí hay una rápida comparación:  
|**Estilo A1**|**Estilo R1C1**|  
| :- | :- |  
|A1|R1C1  
|B3|R3C2  
|G10|R10C7  
|AA25|R25C27  

## **Cómo cambiar entre el estilo de referencia R1C1 y el estilo de referencia A1**  
Puede cambiar entre estos estilos de referencia en la configuración de Excel. Para cambiar el estilo de referencia:

1. Vaya a la pestaña "Archivo".  
1. Seleccione "Opciones" en la parte inferior.  
1. En el cuadro de diálogo Opciones de Excel, vaya a la categoría "Fórmulas".  
1. En la sección "Trabajar con fórmulas", active o desactive la opción "Estilo de referencia R1C1".  
1. Haga clic en "Aceptar" para aplicar los cambios.  
<br>  
<image src="1.png" width="70%" />  

## **Cómo utilizar el estilo de referencia R1C1 y el estilo de referencia A1 en Excel**  
El siguiente ejemplo muestra cómo calcular la suma de dos valores de celda en dos estilos.  
<br>  
Estilo de referencia A1:  
<br>  
<image src="4.png" width="70%" />  

Estilo de referencia R1C1:  
<br>  
<image src="3.png" width="70%" />  
