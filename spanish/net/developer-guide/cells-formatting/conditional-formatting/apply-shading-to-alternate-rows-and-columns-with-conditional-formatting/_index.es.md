---
title: Aplicar sombreado a filas y columnas alternativas con formato condicional
description: Cómo utilizar la biblioteca Aspose.Cells en C# para aplicar sombras de formato condicional para alternar filas y columnas. Al ajustar estos criterios, tiene más control sobre el aspecto y la apariencia de las células.
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /es/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells Las API proporcionan los medios para agregar y manipular reglas de formato condicional para el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objeto. Estas reglas se pueden adaptar de varias maneras para obtener el formato deseado según las condiciones o reglas. Este artículo demostrará el uso de las API Aspose.Cells for .NET para aplicar sombreado a filas y columnas alternativas con la ayuda de reglas de formato condicional y las funciones integradas de Excel.

{{% /alert %}}

Este artículo utiliza las funciones integradas de Excel, como FILA, COLUMNA y MOD. A continuación se muestran algunos detalles de estas funciones para una mejor comprensión del fragmento de código que se proporciona a continuación.

- **ROW()** La función devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, se supone que la referencia es la dirección de celda en la que se ingresó la función FILA.
- **COLUMN()**La función devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, se supone que la referencia es la dirección de celda en la que se ingresó la función COLUMNA.
- **MOD()** La función devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto desea encontrar y el segundo parámetro es el número utilizado para dividir en el parámetro numérico. Si el divisor es 0, devolverá el #DIV/0. error.

Comencemos a escribir código para lograr este objetivo con la ayuda de Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

La siguiente instantánea muestra la hoja de cálculo resultante cargada en la aplicación Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

 Para aplicar el sombreado a columnas alternativas, todo lo que tienes que hacer es cambiar la fórmula**=MOD(FILA(),2)=0** como *=MOD(COLUMN(),2)=0**, es decir; en lugar de obtener el índice de la fila, modifique la fórmula para recuperar el índice de la columna.
La hoja de cálculo resultante, en este caso, tendrá el siguiente aspecto.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
