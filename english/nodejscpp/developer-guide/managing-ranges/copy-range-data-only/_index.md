---  
title: Copy Range Data Only with Node.js via C++  
linktitle: Copy Range Data Only  
type: docs  
weight: 600  
url: /nodejs-cpp/copy-range-data-only/  
description: Learn how to copy data from one range of cells to another using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
Sometimes, you need to copy data from one range of cells to another, copying the data only, not the formatting. Aspose.Cells offers this feature.  

This article provides a sample code that uses Aspose.Cells to copy a range of data.  
{{% /alert %}}  

This example shows how to:  

1. Create a workbook.  
2. Add data to cells in the first worksheet.  
3. Create a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
4. Create a [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object with specified formatting attributes.  
5. Apply the style formatting to the range.  
6. Create another range of cells.  
7. Copy data of the first range to this second range.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++) {
    for (let j = 0; j < 10; j++) {
        cells.get(i, j).putValue(`${i},${j}`);
    }
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the Excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
