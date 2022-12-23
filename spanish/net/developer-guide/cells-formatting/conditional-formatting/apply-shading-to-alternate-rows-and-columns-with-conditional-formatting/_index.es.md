---
title: Aplicar sombreado a filas y columnas alternativas con formato condicional
type: docs
weight: 30
url: /es/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells Las API proporcionan los medios para agregar y manipular reglas de formato condicional para el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objeto. Estas reglas se pueden adaptar de varias maneras para obtener el formato deseado en función de las condiciones o reglas. Este artículo demostrará el uso de las API Aspose.Cells for .NET para aplicar sombreado a filas y columnas alternativas con la ayuda de las reglas de formato condicional y las funciones integradas de Excel.

{{% /alert %}}

Este artículo hace uso de las funciones integradas de Excel, como FILA, COLUMNA Y MOD. Aquí hay algunos detalles de estas funciones para una mejor comprensión del fragmento de código que se proporciona a continuación.

- **FILA()** La función devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, se asume que la referencia es la dirección de la celda en la que se ha ingresado la función FILA.
- **COLUMNA()** La función devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, se supone que la referencia es la dirección de la celda en la que se ha introducido la función COLUMNA.
- **MODIFICACIÓN()** La función devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro numérico. Si el divisor es 0, ¡devolverá el #DIV/0! error.

Comencemos a escribir código para lograr este objetivo con la ayuda de Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

La siguiente instantánea muestra la hoja de cálculo resultante cargada en la aplicación Excel.

|![todo:imagen_alternativa_texto](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
|:- |

 Para aplicar el sombreado a columnas alternativas, todo lo que tiene que hacer es cambiar la fórmula**=MOD(FILA(),2)=0** como**=MOD(COLUMNA(),2)=0** , es decir; en lugar de obtener el índice de la fila, modifique la fórmula para recuperar el índice de la columna.
La hoja de cálculo resultante, en este caso, tendrá el siguiente aspecto.

|![todo:imagen_alternativa_texto](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
|:- |
