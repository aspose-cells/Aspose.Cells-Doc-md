---
title: 用Node.js通过C++管理Excel文件的公式
linktitle: 公式
type: docs
weight: 122
url: /zh/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: 学习如何通过Aspose.Cells for Node.js via C++管理Excel文件中的公式。Aspose.Cells可以轻松获取、设置和计算Excel的公式。
keywords: 在Node.js通过C++中如何计算公式、使用公式和函数、管理内置函数、使用插件函数，使用数组公式，使用R1C1公式。
---

## **介绍**

Microsoft Excel的一个引人注目的功能是其使用公式和函数处理数据的能力。Microsoft Excel提供了一组内置函数和公式，帮助用户快速执行复杂计算。Aspose.Cells还提供了大量内置函数和公式，帮助开发者轻松计算值。Aspose.Cells还支持插件函数。此外，Aspose.Cells支持数组和R1C1公式。

## **如何使用公式和函数**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供了一个[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)集合。Cells集合中的每个项都代表了[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的对象。

可以使用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类提供的属性和方法将公式应用到单元格中，下面将更详细地讨论。

- 使用内置函数。
- 使用插件函数。
- 使用数组公式。
- 创建R1C1公式。

## **如何使用内置函数**

内置函数或公式作为现成的功能提供，以减少开发者的努力和时间。请参阅[支持的内置函数列表](/cells/zh/nodejs-cpp/supported-formula-functions/)。这些函数按字母顺序列出。未来将支持更多函数。

Aspose.Cells支持Microsoft Excel提供的大部分公式或函数。开发者可以通过API或[设计器电子表格](/cells/zh/nodejs-cpp/what-is-a-designer-spreadsheet/)使用这些公式。Aspose.Cells支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。

使用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--)属性向单元格添加公式。**复杂的公式**，例如

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

Aspose.Cells也支持定义的函数。在将公式应用于单元格时，始终要以等号（=）开头，就像在Microsoft Excel中创建公式时一样，并使用逗号（，）来分隔函数参数。

在下面的示例中，复杂的公式应用于工作表的第一个单元格的[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合。该公式使用Aspose.Cells提供的内置**IF**函数。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **如何使用Add-in函数**

我们可以有一些自定义的公式，我们希望将其包含为Excel加载项。当设置cell.Formula函数内置函数正常工作时，但需要使用加载项函数设置自定义函数或公式。

Aspose.Cells提供功能来使用[**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-)注册加载项函数。之后，当我们设置cell.Formula = anyFunctionFromAddIn时，输出的Excel文件包含从AddIn函数计算出的值。

可以下载以下XLAM文件以注册以下示例代码中的加载项函数。类似地，可以下载输出文件"test_udf.xlsx"以检查输出。

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **如何使用数组公式**

数组公式是以数组作为参数的函数所组成的公式。在显示数组公式时，会用大括号({})括起来。

某些Microsoft Excel函数返回值数组。要使用数组公式计算多个结果，请将数组输入到与数组参数具有相同行数和列数的单元格范围中。

可以通过调用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-)方法将数组公式应用于单元格。[**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-)方法接受以下参数：

- **数组公式**，数组公式。
- **行数**，要填充数组公式结果的行数。
- **列数**，要填充数组公式结果的列数。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **如何使用R1C1公式**

使用[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的[**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--)属性向单元格添加**R1C1**引用样式的公式。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **高级主题**
- [前导和从属](/cells/zh/nodejs-cpp/precedents-and-dependents/)
- [设置公式中的外部链接](/cells/zh/nodejs-cpp/set-external-links-in-formulas/)
- [在输入新数据时自动传播表或列表对象中的公式](/cells/zh/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [为命名范围设置公式](/cells/zh/nodejs-cpp/setting-formula-for-named-range/)
- [设置公式-非英语用户注意事项](/cells/zh/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [设置共享公式](/cells/zh/nodejs-cpp/setting-shared-formula/)
- [指定共享公式的最大行数](/cells/zh/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [支持的Excel函数](/cells/zh/nodejs-cpp/supported-formula-functions/)

