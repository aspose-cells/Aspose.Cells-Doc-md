---
title: Aplicar sombreado a filas y columnas alternas con formato condicional
linktitle: Aplicar sombreado a filas y columnas alternas con formato condicional
description: Cómo usar la biblioteca Aspose.Cells en Node.js vía C++ para aplicar sombras de formato condicional en filas y columnas alternas. Al ajustar estos criterios, tienes mayor control sobre cómo lucen y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional, Filas alternas, Columnas alternas, Sombras
type: docs
weight: 30
url: /es/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells proporcionan los medios para agregar y manipular reglas de formato condicional para el objeto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Estas reglas pueden ajustarse de varias formas para lograr el formato deseado en función de condiciones o reglas. Este artículo demostrará el uso de las APIs Aspose.Cells for Node.js via C++ para aplicar sombreado en filas y columnas alternas con la ayuda de reglas de formato condicional y funciones integradas de Excel.

{{% /alert %}}

Este artículo utiliza las funciones integradas de Excel como ROW, COLUMN y MOD. Aquí hay algunos detalles de estas funciones para una mejor comprensión del fragmento de código proporcionado a continuación.

- La función **ROW()** devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función ROW.
- La función **COLUMN()** devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función COLUMN.
- La función **MOD()** devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto se desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro del número. Si el divisor es 0, devolverá el error #DIV/0!.

Comencemos a escribir algo de código para lograr este objetivo con la ayuda de la API Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyShadingToAlternateRowsAndColumns.js" >}}


La siguiente captura de pantalla muestra la hoja de cálculo resultante cargada en la aplicación de Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Para aplicar el sombreado a las columnas alternas, todo lo que tiene que hacer es cambiar la fórmula **=MOD(ROW(),2)=0** a **=MOD(COLUMN(),2)=0**, es decir, en lugar de obtener el índice de fila, modifique la fórmula para obtener el índice de columna.  
La hoja de cálculo resultante, en este caso, se verá como sigue.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
