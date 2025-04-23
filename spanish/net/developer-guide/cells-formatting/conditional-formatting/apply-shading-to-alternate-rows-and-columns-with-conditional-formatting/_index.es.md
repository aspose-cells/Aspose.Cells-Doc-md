---
title: Aplicar sombreado a filas y columnas alternas con formato condicional
description: Cómo usar la librería Aspose.Cells en C# para aplicar sombras de formato condicional para filas y columnas alternas. Al ajustar estos criterios, se tiene más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional, C#, Filas alternas, Columnas alternas, Sombras
type: docs
weight: 30
url: /es/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells proporcionan los medios para agregar y manipular reglas de formato condicional para el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Estas reglas pueden adaptarse de varias maneras para obtener el formato deseado basado en condiciones o reglas. Este artículo demostrará el uso de las APIs de Aspose.Cells for .NET para aplicar sombreado a filas y columnas alternas con la ayuda de reglas de formato condicional y las funciones integradas de Excel.

{{% /alert %}}

Este artículo utiliza las funciones integradas de Excel como ROW, COLUMN y MOD. Aquí hay algunos detalles de estas funciones para una mejor comprensión del fragmento de código proporcionado a continuación.

- La función **ROW()** devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función ROW.
- La función **COLUMN()** devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función COLUMN.
- La función **MOD()** devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto se desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro del número. Si el divisor es 0, devolverá el error #DIV/0!.

Comencemos a escribir algo de código para lograr este objetivo con la ayuda de la API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

La siguiente captura de pantalla muestra la hoja de cálculo resultante cargada en la aplicación de Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Para aplicar el sombreado a las columnas alternas, todo lo que tiene que hacer es cambiar la fórmula **=MOD(ROW(),2)=0** a **=MOD(COLUMN(),2)=0**, es decir, en lugar de obtener el índice de fila, modifique la fórmula para obtener el índice de columna. 
La hoja de cálculo resultante, en este caso, se verá como sigue.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
