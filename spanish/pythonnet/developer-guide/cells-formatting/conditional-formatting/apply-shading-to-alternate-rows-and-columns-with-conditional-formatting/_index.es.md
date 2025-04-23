---
title: Aplicar sombreado a filas y columnas alternas con formato condicional
description: Cómo usar la biblioteca Aspose.Cells en Python para aplicar sombras de formato condicional en filas y columnas alternas. Ajustando estos criterios, tienes mayor control sobre la apariencia de las celdas.
keywords: Aspose.Cells, Formato condicional, Python filas alternas, Columnas alternas, Sombras
type: docs
weight: 30
url: /es/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Las APIs de Aspose.Cells para Python via .NET permiten agregar y manipular reglas de formato condicional para el objeto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Estas reglas pueden personalizarse de varias maneras para obtener el formato deseado basado en condiciones o reglas. Este artículo demostrará cómo usar las APIs de Aspose.Cells para Python via .NET para aplicar sombreado a filas y columnas alternas usando reglas de formato condicional y funciones integradas de Excel.

{{% /alert %}}

Este artículo utiliza las funciones integradas de Excel como ROW, COLUMN y MOD. Aquí hay algunos detalles de estas funciones para una mejor comprensión del fragmento de código proporcionado a continuación.

- La función **ROW()** devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función ROW.
- La función **COLUMN()** devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función COLUMN.
- La función **MOD()** devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto se desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro del número. Si el divisor es 0, devolverá el error #DIV/0!.

Comencemos a escribir código para lograr este objetivo con la ayuda de Aspose.Cells para Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyShadingToAlternateRowsColumns-1.py" >}}

La siguiente captura de pantalla muestra la hoja de cálculo resultante cargada en la aplicación de Excel.

|![todo:image_alt_text](1.png)|
| :- |

Para aplicar el sombreado a las columnas alternas, todo lo que tiene que hacer es cambiar la fórmula **=MOD(ROW(),2)=0** a **=MOD(COLUMN(),2)=0**, es decir, en lugar de obtener el índice de fila, modifique la fórmula para obtener el índice de columna. 
La hoja de cálculo resultante, en este caso, se verá como sigue.

|![todo:image_alt_text](2.png)|
| :- |

