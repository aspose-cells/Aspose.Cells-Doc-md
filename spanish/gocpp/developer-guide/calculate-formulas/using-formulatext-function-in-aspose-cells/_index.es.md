---
title: Usar la función FormulaText en Aspose.Cells con Golang mediante C++
linktitle: Uso de la función FormulaText
description: Este artículo introduce cómo utilizar la función FormulaText en la librería Aspose.Cells para procesar fórmulas en Microsoft Excel. Al cargar un archivo de Excel existente o crear uno nuevo, podemos utilizar el método proporcionado por Aspose.Cells para obtener y establecer el texto de la fórmula de la celda y obtener el resultado. Finalmente, guardamos el archivo de Excel modificado en el disco.
keywords: Aspose.Cells, Excel, funciones FormulaText
type: docs
weight: 60
url: /es/go-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 y posteriores. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre sugiere, imprime el texto de la fórmula que se encuentra en una celda dada. Este artículo te mostrará cómo hacer uso de esta función con Aspose.Cells.

{{% /alert %}} 

El siguiente código de muestra muestra el uso de FormulaText con Aspose.Cells. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingFormulatextFunctionInAsposeCells.go" >}}
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
