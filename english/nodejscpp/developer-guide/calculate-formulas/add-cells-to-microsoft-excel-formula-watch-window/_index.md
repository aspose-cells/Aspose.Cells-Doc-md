---  
title: Add Cells to Microsoft Excel Formula Watch Window with Node.js via C++  
linktitle: Add Cells to Microsoft Excel Formula Watch Window  
description: How to use the Aspose.Cells library to add cells to the formula watch window in Excel using Node.js via C++. By loading an existing Excel file or creating a new one, you can manipulate the cells in it and set formulas. Finally, you save the modified Excel file to disk.  
keywords: Aspose.Cells, Excel, Formula Watch Window, Cells, Adding, Node.js via C++  
type: docs  
weight: 60  
url: /nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**  

Microsoft Excel Watch Window is a useful tool to watch cell values and their formulas conveniently in a window. You can open the *Watch Window* in Microsoft Excel by clicking **Formulas > Watch Window**. It has an *Add Watch* button that can be used to add cells for inspection. Similarly, you can use the [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cellwatchcollection/#add-number-number-) method to add cells to the *Watch Window* using the Aspose.Cells API.  

## **Add Cells to Microsoft Excel Formula Watch Window**  

The following sample code sets the formulas of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as an [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.  

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an empty workbook.
const wb = new AsposeCells.Workbook();

// Access the first worksheet.
const ws = wb.getWorksheets().get(0);

// Put some integer values in cells A1 and A2.
ws.getCells().get("A1").putValue(10);
ws.getCells().get("A2").putValue(30);

// Access cell C1 and set its formula.
const c1 = ws.getCells().get("C1");
c1.setFormula("=SUM(A1,A2)");

// Add cell C1 to cell watches by name.
ws.getCellWatches().add(c1.getName());

// Access cell E1 and set its formula.
const e1 = ws.getCells().get("E1");
e1.setFormula("=A2*A1");

// Add cell E1 to cell watches by its row and column indices.
ws.getCellWatches().add(e1.getRow(), e1.getColumn());

// Save the workbook in XLSX format.
wb.save("outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
