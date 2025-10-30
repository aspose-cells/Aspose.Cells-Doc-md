---  
title: Especificar filas máximas de fórmula compartida con Node.js mediante C++  
linktitle: Especificar el número máximo de filas de la fórmula compartida  
type: docs  
weight: 40  
url: /es/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Aprende cómo especificar las filas máximas para fórmulas compartidas usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

El máximo predeterminado de filas para la fórmula compartida es 64. Puede ser cualquier número, por ejemplo, 1000. El rendimiento de la fórmula compartida varía con el número de filas. Por ello, Aspose.Cells ofrece la propiedad [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--) que puede usarse para especificar el máximo de filas de la fórmula compartida. La fórmula compartida se dividirá en varias fórmulas compartidas si el total de filas de la fórmula supera ese límite, como se muestra en la siguiente captura de pantalla.  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **Especificar el número máximo de filas de la fórmula compartida**  

El siguiente código de ejemplo explica el uso de la propiedad [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--). Establece el máximo de filas de la fórmula compartida en 5 y añade la fórmula en la celda D1 para 100 filas, guardando en el [archivo de Excel de salida](61767856.xlsx). Si extraes el contenido del archivo de Excel de salida y revisas *sheet1.xml*, verás que la fórmula compartida se divide cada 5 filas, como se destaca en la captura anterior.  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
