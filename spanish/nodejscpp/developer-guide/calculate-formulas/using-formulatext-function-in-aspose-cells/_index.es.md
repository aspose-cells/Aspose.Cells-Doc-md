---
title: Usando la función FormulaText en Aspose.Cells for Node.js via C++
linktitle: Usando la función FormulaText en Aspose.Cells
description: Este artículo introduce cómo usar la función FormulaText en la biblioteca Aspose.Cells para procesar fórmulas en Microsoft Excel. Aprende a obtener y establecer el texto de la fórmula de las celdas y guardar archivos Excel modificados usando Node.js vía C++.
keywords: Aspose.Cells, Excel, funciones FormulaText en Node.js vía C++
type: docs
weight: 60
url: /es/nodejs-cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText es una función de Excel 2013 en adelante. No es compatible con versiones anteriores como Excel 2010 o 2007, etc. Como su nombre indica, imprime el texto de la fórmula que está en una celda dada. Este artículo mostrará cómo usar esta función con Aspose.Cells for Node.js via C++.

{{% /alert %}} 

El siguiente código de ejemplo muestra el uso de FormulaText con Aspose.Cells for Node.js via C++. El código primero escribe una fórmula en la celda A1 y luego imprime el texto de la fórmula usando FormulaText en la celda A2.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a workbook object
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some formula in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.setFormula("=Sum(B1:B10)");

// Get the text of the formula in cell A2 using FORMULATEXT function
const cellA2 = worksheet.getCells().get("A2");
cellA2.setFormula("=FormulaText(A1)");

// Calculate the workbook
workbook.calculateFormula();

// Print the results of A2, It will now print the text of the formula inside cell A1
console.log(cellA2.getStringValue());
```
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
