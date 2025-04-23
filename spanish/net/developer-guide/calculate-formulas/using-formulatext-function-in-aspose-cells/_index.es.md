---
title: Usando la función FormulaText en Aspose.Cells
description: Este artículo introduce cómo utilizar la función FormulaText en la librería Aspose.Cells para procesar fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar el método proporcionado por Aspose.Cells para obtener y establecer el texto de la fórmula de la celda y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones FormulaText
type: docs
weight: 60
url: /es/net/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 y posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre sugiere, imprime el texto de la fórmula que se encuentra en una celda dada. Este artículo te mostrará cómo hacer uso de esta función con Aspose.Cells.

{{% /alert %}} 

El siguiente código de muestra muestra el uso de FormulaText con Aspose.Cells. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingFormulaTextFunction-UsingFormulaTextFunction.cs" >}}
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
