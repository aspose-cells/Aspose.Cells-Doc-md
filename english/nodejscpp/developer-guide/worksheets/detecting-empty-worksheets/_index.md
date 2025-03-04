---  
title: Detecting Empty Worksheets with Node.js via C++  
linktitle: Detecting Empty Worksheets  
type: docs  
weight: 410  
url: /nodejs-cpp/detecting-empty-worksheets/  
description: This article shows you code explaining how to detect empty worksheets of Excel workbooks programmatically using the Node.js API with C++ library.  
keywords: detect empty worksheet Node.js via C++, find empty excel worksheet Node.js via C++  
---  

## **Check for Populated Cells**

Worksheets can have one or more cells populated with values where a value can be simple (text, numeric, date/time) or a formula or a formula-based value. In such a case, it is easy to detect if a given worksheet is empty or not. All we have to check is the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/#maxDataRow) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/#maxDataColumn) properties. If the aforementioned properties return zero or positive values that means, one or more cells have been populated; however, if any of these properties return -1, that indicates that none of the cells have been populated in the given worksheet.

{{% alert color="primary" %}}

The rows & columns collections have zero-based indices; therefore, a cell at row 0 & column 0 means the first cell in the worksheet, which is A1.

{{% /alert %}}

## **Check for Empty Initialized Cells**

All cells that have values are automatically initialized; however, there is a possibility that a worksheet has cells with only formatting applied. In such a scenario, the [**Cells.MaxDataRow**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/#maxDataRow) or [**Cells.MaxDataColumn**](https://reference.aspose.com/cells/nodejs-cpp/cells/properties/#maxDataColumn) properties will return -1 indicating the absence of any populated values, but initialized cells due to cell formatting cannot be detected using this approach. In order to check if a worksheet has empty initialized cells, it is advised to use the `Enumerator.MoveNext` method on the enumerator acquired from [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection. If the `Enumerator.MoveNext` method returns **true**, that means there are one or more initialized cells in the given worksheet.

## **Check for Shapes**

It is possible that a given worksheet does not have any populated cells; however, it could contain shapes & objects such as controls, charts, images, and so on. If we need to check if a worksheet contains any shape, we can do it by inspecting the [**ShapeCollection.Count**](https://reference.aspose.com/cells/nodejs-cpp/cells/drawing/shapecollection) property. Any positive value indicates the presence of shape(s) in the worksheet.

## **Programming Sample**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  
  