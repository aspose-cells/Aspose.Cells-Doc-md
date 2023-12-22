---
title: Usando la función FormulaText en Aspose.Cells
description: Este artículo presenta cómo utilizar la función FormulaText en la biblioteca Aspose.Cells para procesar fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar el método proporcionado por Aspose.Cells para obtener y configurar el texto de la fórmula de la celda y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /es/net/using-formulatext-function-in-aspose-cells/
---
{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 y posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como sugiere su nombre, imprime el texto de la fórmula que está presente en una celda determinada. Este artículo le mostrará cómo utilizar esta función utilizando Aspose.Cells.

{{% /alert %}} 

El siguiente código de muestra muestra el uso de FormulaText con Aspose.Cells. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
##  **Salida de consola**
Aquí está la salida de la consola del código de muestra anterior.

{{< highlight "java" >}}

 =SUM(B1:B10)

{{< /highlight >}}
