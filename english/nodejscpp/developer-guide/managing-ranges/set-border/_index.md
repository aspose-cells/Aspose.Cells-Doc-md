---  
title: Set Range Border with Node.js via C++  
linktitle: Set Range Border  
type: docs  
weight: 600  
url: /nodejs-cpp/set-range-border/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
When you want to set the border for a range, you don't need to set each cell individually. You can set the border on the range. Aspose.Cells for Node.js via C++ offers this feature.  
This article provides a sample code that uses Aspose.Cells for Node.js via C++ to set a range border.  

## **Set Range Border in Excel**  
To set the border of a range in Excel, you can follow these steps:  
1. Select the range of cells that you want to apply the border to.  
2. In the "Home" tab of the ribbon, locate the "Font" group.  
3. Within the "Font" group, click on the "Borders" drop‑down button.  
<br>  
<img src="border.png" />  
4. Choose the type of border that you want to apply from the options in the drop‑down menu. You can choose from preset border styles or customize your own border.  
5. Once you have selected the desired border style, the border will be applied to the selected range of cells.  

## **Set Range Border Using Aspose.Cells for Node.js via C++**  
This example shows how to:  

1. Create a workbook.  
2. Add data to cells in the first worksheet.  
3. Create a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Set the inner border of the range.  
5. Set the outer border of the range.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const ws = workbook.getWorksheets().get(0);
const cells = ws.getCells();

// Setting the value to the cells
let cell = cells.get("A1");
cell.putValue("Fruit");
cell = cells.get("B1");
cell.putValue("Count");
cell = cells.get("C1");
cell.putValue("Price");

cell = cells.get("A2");
cell.putValue("Apple");
cell = cells.get("A3");
cell.putValue("Mango");
cell = cells.get("A4");
cell.putValue("Blackberry");
cell = cells.get("A5");
cell.putValue("Cherry");

cell = cells.get("B2");
cell.putValue(5);
cell = cells.get("B3");
cell.putValue(3);
cell = cells.get("B4");
cell.putValue(6);
cell = cells.get("B5");
cell.putValue(4);

cell = cells.get("C2");
cell.putValue(5);
cell = cells.get("C3");
cell.putValue(20);
cell = cells.get("C4");
cell.putValue(30);
cell = cells.get("C5");
cell.putValue(60);

// Create a range (A1:C5).
const range = cells.createRange("A1", "C5");

// set inner border of range
const innerColor = workbook.createCellsColor();
innerColor.setColor(AsposeCells.Color.Red);
range.setInsideBorders(AsposeCells.BorderType.Vertical, AsposeCells.CellBorderType.Thin, innerColor);
innerColor.setColor(AsposeCells.Color.Green);
range.setInsideBorders(AsposeCells.BorderType.Horizontal, AsposeCells.CellBorderType.Thin, innerColor);

// set outer border of range
const outerColor = workbook.createCellsColor();
outerColor.setColor(AsposeCells.Color.Blue);
range.setOutlineBorders(AsposeCells.CellBorderType.Thin, outerColor);

workbook.save("out.xlsx");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
