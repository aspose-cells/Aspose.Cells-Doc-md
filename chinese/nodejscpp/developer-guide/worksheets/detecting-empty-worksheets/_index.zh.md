---  
title: 用Node.js和C++检测空工作表  
linktitle: 检测空工作表  
type: docs  
weight: 410  
url: /zh/nodejs-cpp/detecting-empty-worksheets/  
description: 本文演示了使用C++的Node.js API以编程方式检测Excel工作簿中的空工作表的代码。  
keywords: 检测空工作表Node.js，查找空Excel工作表Node.js  
---  

## **检查已填充的单元格**

工作表可能包含一个或多个已填充值的单元格，这些值可以是简单（文本、数字、日期/时间）或基于公式的值或公式。这样，检测某个工作表是否为空就变得容易。只需检查[**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)或[**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--)属性，如果这些属性返回零或正数，表示已填充一个或多个单元格；如果任何一个属性返回-1，则表示该工作表中没有已填充的单元格。

{{% alert color="primary" %}}

行和列集合索引从零开始；因此，位于第0行第0列的单元格即为工作表中的第一个单元格（A1）。

{{% /alert %}}

## **检测空初始化单元格**

所有具有值的单元格会自动初始化；但工作表中也可能只有格式应用的单元格。在这种情况下，[**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--)或[**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--)属性返回-1，表示没有已填充的值，但不能通过此方法检测仅格式化的已初始化单元格。为了检查工作表是否有空的已初始化单元格，建议使用从[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合获取的枚举器上的`Enumerator.MoveNext`方法。如果返回**true**，说明工作表中有一个或多个已初始化的单元格。

## **检查形状**

工作表可能没有任何已填充的单元格，但可能包含形状和对象，如控件、图表、图片等。如果需要检查工作表中是否包含任何形状，可以通过检查[**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--)属性。任何正值都表示工作表中存在形状。

## **编程示例**

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

