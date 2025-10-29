---  
title: 使用 C++ 通过 Node.js 插入或删除 Excel 工作表中的行  
linktitle: 在Excel工作表中插入或删除行  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: 本文提供了使用 C++ 的 Node.js 代码，用于在 Excel 工作表中插入和删除行。  
keywords: Node.js 在 Excel 工作表中插入或删除行，Node.js 插入或删除 Excel 行，Node.js 在 Excel 中插入行，Node.js 删除 Excel 中的行，使用 Node.js 在 Excel 工作表中插入或删除行，使用 Node.js 在 Excel 中插入或删除行，使用 Node.js 在 Excel 中插入行，使用 Node.js 删除 Excel 行  
---  

{{% alert color="primary" %}}  

在创建新工作表或操作已有工作表时，可能需要添加额外的行或列以容纳数据。也可能需要删除指定位置的行或列。  

{{% /alert %}}  

Aspose.Cells for Node.js via C++ 提供两种插入和删除行的方法：[**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) 和 [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-)。这些方法经过优化，执行速度非常快。  

建议在插入或删除多行时，始终使用 [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) 和 [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) 方法，而不是在循环中使用 [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) 或 [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) 方法。  

Aspose.Cells的工作方式与Microsoft Excel相同。当添加行或列时，工作表内容向下和向右移动。当删除行或列时，工作表内容向上或向左移动。添加或删除行时，其他工作表和单元格中的引用会得到更新。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
