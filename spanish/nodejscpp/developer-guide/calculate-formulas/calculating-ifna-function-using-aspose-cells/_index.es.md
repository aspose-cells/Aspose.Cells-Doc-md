---
title: Cálculo de la función IFNA usando Aspose.Cells for Node.js via C++
description: Cómo calcular funciones IFNA usando la biblioteca Aspose.Cells para Node.js en C++. Carga un archivo Excel existente o crea uno nuevo, y calcula la función IFNA para obtener el resultado. Finalmente, guarda el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, funciones IFNA, cálculos Node.js a través de C++
type: docs
weight: 40
url: /es/nodejs-cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells soporta el cálculo de la función IFNA de Excel. La función IFNA devuelve el valor que especificas si la fórmula devuelve el error #N/A; de lo contrario, devuelve el resultado de la fórmula.

{{% /alert %}} 
## **Cálculo de la función IFNA usando Aspose.Cells for Node.js via C++**
El código de muestra siguiente ilustra el cálculo de la función IFNA usando Aspose.Cells for Node.js via C++.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create new workbook
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add data for VLOOKUP
worksheet.getCells().get("A1").putValue("Apple");
worksheet.getCells().get("A2").putValue("Orange");
worksheet.getCells().get("A3").putValue("Banana");

// Access cell A5 and A6
const cellA5 = worksheet.getCells().get("A5");
const cellA6 = worksheet.getCells().get("A6");

// Assign IFNA formula to A5 and A6
cellA5.setFormula('=IFNA(VLOOKUP("Pear",$A$1:$A$3,1,0),"Not found")');
cellA6.setFormula('=IFNA(VLOOKUP("Orange",$A$1:$A$3,1,0),"Not found")');

// Calculate the formula of workbook
workbook.calculateFormula();

// Print the values of A5 and A6
console.log(cellA5.getStringValue());
console.log(cellA6.getStringValue());
```
## **Salida de la consola**
Aquí está la salida en consola del código de muestra anterior.

{{< highlight javascript >}}
 Not found

Orange
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
