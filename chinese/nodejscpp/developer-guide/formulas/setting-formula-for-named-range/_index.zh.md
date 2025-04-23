---
title: 通过 C++ 在 Node.js 中为命名区域设置公式
linktitle: 设置命名范围公式
type: docs
weight: 20
url: /zh/nodejs-cpp/setting-formula-for-named-range/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 为电子表格中的命名区域设置公式。
---

## **为命名范围设置公式**
 类似于Excel应用，Aspose.Cells API 提供在使用 [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--) 属性时，为命名区域指定公式的能力。此功能有许多使用场景，以下列举部分：

### **为命名范围设置简单公式**
简单公式可能是对同一（或不同）工作表中另一个单元格的引用。下面的示例创建一个新电子表格中的命名范围，并将其引用设置为另一个单元格。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "NewNamedRange"
const index = worksheets.getNames().add("NewNamedRange");

// Access the newly created Named Range
const name = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
name.setRefersTo("=Sheet1!$A$3");

// Set the formula in the cell A1 to the newly created Named Range
worksheets.get(0).getCells().get("A1").setFormula("NewNamedRange");

// Insert the value in cell A3 which is being referenced in the Named Range
worksheets.get(0).getCells().get("A3").putValue("This is the value of A3");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```

### **为命名范围设置复杂公式**
复杂公式可以是任何内容，例如动态范围或跨不同工作表多个单元格的公式。下面的示例使用INDEX函数创建一个动态范围，根据其位置从列表中获取值。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "data"
let index = worksheets.getNames().getCount();
worksheets.getNames().add("data");

// Access the newly created Named Range from the collection
const data = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a cell range in same worksheet
data.setRefersTo("=Sheet1!$A$1:$A$10");

// Add another Named Range with name "range"
index = worksheets.getNames().getCount();
worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property to a formula using the Named Range data
range.setRefersTo("=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

// Save the workbook
book.save(path.join(dataDir, "output_out.xlsx"));
```

这是另一个示例，使用命名范围对不同工作表中的2个单元格的值进行求和。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Insert some data in cell A1 of Sheet1
worksheets.get("Sheet1").getCells().get("A1").putValue(10);

// Add a new Worksheet and insert a value to cell A1
worksheets.get(worksheets.add()).getCells().get("A1").putValue(10);

// Add a new Named Range with name "range"
const index = worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a SUM function
range.setRefersTo("=SUM(Sheet1!$A$1,Sheet2!$A$1)");

// Insert the Named Range as formula to 3rd worksheet
worksheets.get(worksheets.add()).getCells().get("A1").setFormula("range");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```
