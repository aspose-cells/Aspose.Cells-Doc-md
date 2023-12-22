---
title: "Excel: estilo de referencia R1C1 frente a A1"
type: docs
weight: 30
url: /es/net/r1c1-reference-style-vs-a1/
description: Estilo de referencia R1C1 VS. Estilo A1 usando Aspose.Cells for Python via .NET API.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

En Excel, R1C1 y A1 son dos estilos de referencia diferentes que se utilizan para identificar celdas en una hoja de trabajo. Tenga en cuenta que la elección entre A1 y R1C1 es en gran medida una cuestión de preferencia personal. La mayoría de los usuarios están más familiarizados con el estilo A1, pero R1C1 puede resultar útil en determinadas situaciones, especialmente cuando se trabaja con fórmulas y cálculos.

{{% /alert %}}

##  **Estilo de referencia A1**

Este es el estilo de referencia predeterminado en Excel. En el estilo A1, las columnas se identifican con letras (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) y las filas se identifican con números (1, 2, 3,...).
Por ejemplo, la celda de la primera columna y la segunda fila se denomina A2.

##  **Estilo de referencia R1C1**

En el estilo R1C1, tanto las filas como las columnas se identifican mediante números. La letra "R" representa el número de fila y la letra "C" representa el número de columna. Por ejemplo, R2C1 se refiere a la celda de la segunda fila y la primera columna.

Cualquier número entre corchetes se refiere a la distancia relativa desde la celda actual. A diferencia de A1, que se refiere a columnas seguidas de un número de fila, R1C1 hace lo contrario: filas seguidas de columnas (a lo que cuesta acostumbrarse). Los números positivos se referirán a las celdas de abajo y/o a la derecha. Los números negativos se referirán a las celdas de arriba y/o a la izquierda.

Por ejemplo, R[2]C[3] es una celda 2 filas hacia abajo y 3 columnas a la derecha. R[-1]C[-4] es una celda 1 fila hacia arriba y 4 columnas a la izquierda. Si no se muestra ningún número entre paréntesis, entonces se está refiriendo a la misma fila o columna, es decir, R[3]C será una celda 3 filas debajo de la celda actual en la misma columna.
<br>
<image src="2.png" width="70%" />

##  **Comparación del estilo de referencia R1C1 y el estilo de referencia A1**
Aquí hay una comparación rápida:
|**Estilo A1**|**Estilo R1C1**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **Cómo cambiar entre el estilo de referencia R1C1 y el estilo de referencia A1**
Puede cambiar entre estos estilos de referencia en la configuración de Excel. Para cambiar el estilo de referencia:

1. Vaya a la pestaña "Archivo".
1. Seleccione "Opciones" en la parte inferior.
1. En el cuadro de diálogo Opciones de Excel, vaya a la categoría "Fórmulas".
1. En la sección "Trabajar con fórmulas", marca o desmarca la opción "Estilo de referencia R1C1".
1. Haga clic en "Aceptar" para aplicar los cambios.
<br>
<image src="1.png" width="70%" />

##  **Cómo utilizar el estilo de referencia R1C1 y el estilo de referencia A1 en Excel**
El siguiente ejemplo muestra cómo calcular la suma de dos valores de celda en dos estilos.
<br>
Estilo de referencia A1:
<br>
<image src="4.png" width="70%" />

Estilo de referencia R1C1:
<br>
<image src="3.png" width="70%" />
