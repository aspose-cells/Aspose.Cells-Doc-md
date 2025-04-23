---
title: Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel con Node.js mediante C++
linktitle: Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel
description: Cómo usar la biblioteca Aspose.Cells para agregar celdas a la ventana de seguimiento de fórmulas en Excel usando Node.js a través de C++. Al cargar un archivo Excel existente o crear uno nuevo, podemos manipular las celdas en él y establecer fórmulas. Finalmente, guardamos el archivo Excel modificado en disco.
keywords: Aspose.Cells, Excel, Ventana de seguimiento de fórmulas, Celdas, Agregar, Node.js a través de C++
type: docs
weight: 60
url: /es/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Escenarios de uso posibles**

La ventana de seguimiento de Excel es una herramienta útil para observar los valores de las celdas y sus fórmulas cómodamente en una ventana. Puedes abrir la *Ventana de seguimiento* en Microsoft Excel haciendo clic en *Formulas > Watch*. Tiene el botón *Add Watch* que se puede usar para agregar celdas para inspección. De manera similar, puedes usar el método [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) para agregar celdas a *Watch Window* usando la API de Aspose.Cells.

## **Agregar celdas a la ventana de seguimiento de fórmulas de Microsoft Excel**

El código de ejemplo siguiente establece la fórmula de las celdas C1 y E1 y añade ambas a la ventana de seguimiento. Luego, guarda el libro como [archivo Excel de salida](67338481.xlsx). Si abres el archivo Excel de salida y ves la *Ventana de seguimiento*, verás ambas celdas como se muestra en esta captura.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cell A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=Sum(A1,A2)");

// Add cell C1 into cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 into cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save workbook to output XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```
