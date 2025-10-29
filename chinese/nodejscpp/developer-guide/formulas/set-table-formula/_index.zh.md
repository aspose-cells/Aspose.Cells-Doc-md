---
title: 通过 C++ 在 Node.js 中自动在新行输入时传播表格或列表对象中的公式
linktitle: 设置Table公式
type: docs
weight: 260
url: /zh/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: 学习如何在使用 Aspose.Cells for Node.js via C++ 时，在输入新行数据时自动传播表格或列表对象中的公式。
---

## **可能的使用场景**
有时，你希望表格或列表对象中的公式在输入新数据时自动传播到新行。这是Microsoft Excel的默认行为。要实现相同功能利用Aspose.Cells for Node.js via C++，请使用[ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--)属性。

## ** 自动在新行输入时传播表格或列表对象中的公式**
以下示例代码以此方式创建了一个表格或列表对象，使得在第 B 列中的公式会在输入新数据时自动传播到新行。请查看此代码生成的 [输出 Excel 文件](5115469.xlsx)。如果在 A3 单元格中输入任何数字，你会看到 B2 单元格中的公式会自动传播到 B3。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
