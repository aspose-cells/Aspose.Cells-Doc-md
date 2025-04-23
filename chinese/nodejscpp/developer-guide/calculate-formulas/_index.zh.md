---
title: 通过 Node.js 使用 C++ 计算公式
linktitle: 计算公式
description: 本文介绍如何使用 Aspose.Cells 库，通过 C++ 在 Node.js 中计算 Microsoft Excel 公式。通过加载现有Excel文件或创建新文件，利用 Aspose.Cells 提供的方法计算公式并获取结果。最后保存修改后的Excel文件到磁盘。
keywords: Aspose.Cells、Excel、公式、计算、公式直接计算、重复计算公式、通过 C++ 在 Node.js 中添加公式
type: docs
weight: 125
url: /zh/nodejs-cpp/calculate-formulas/
---

## **添加公式及计算结果**

Aspose.Cells 有内嵌的公式计算引擎。它不仅可以重新计算导入设计模板中的公式，还支持计算在运行时添加的公式的结果。

Aspose.Cells 支持大部分Microsoft Excel中的公式或函数（请阅读[支持的公式函数列表]( /cells/zh/nodejs-cpp/supported-formula-functions/)）。这些函数可以通过API或设计器电子表格使用。Aspose.Cells支持大量的数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用公式。

使用 [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) 属性或 [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) 方法将公式添加到单元格中。应用公式时，字符串前始终以等号（=）开始，就像在Microsoft Excel中创建公式一样，用逗号（,）分隔函数参数。

为了计算公式结果，可以调用 [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) 方法，该方法处理Excel文件中所有嵌入的公式；或者调用 [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) 方法，处理工作表中的所有嵌入公式；或者调用 [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) 方法，处理单个单元格的公式：

```javascript
const path = require("path");
const fs = require("fs");
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

### **公式重复计算的重要信息**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的 **Formula** 属性和 **setFormula(...)** 方法与 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 和 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的 **calculate** 方法不同。**Formula** 属性和 **setFormula(...)** 方法仅将公式添加到单元格，但不会在运行时计算结果。若要获取公式的结果，请调用 **calculate** 方法。

{{% /alert %}}

## **直接计算公式**

Aspose.Cells内置了一个公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式的结果。

有时，您需要在不将其添加到工作表的情况下直接计算公式结果。已在工作表中的单元格值已经存在，您只需根据某个Microsoft Excel公式计算这些值的结果，无需在工作表中添加公式。

您可以使用 Aspose.Cells 的公式计算引擎API [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 来 [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) 这些公式的结果，而不必将它们添加到工作表中：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

以上代码生成以下输出：
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **如何重复计算公式**

当工作簿中有大量公式、用户需要反复计算而只修改少部分内容时，启用公式链计算可能对性能有帮助：[**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建计算链也需要额外的时间，第一次计算公式（[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)）可能会比没有计算链的公式计算消耗更多的CPU处理时间和内存。如果用户不需要重复计算公式，默认行为（直接计算公式而不创建计算链）应该是更好的选择。

{{% /alert %}}

## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [计算数据表的数组公式](/cells/zh/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [计算Excel 2016的MINIFS和MAXIFS函数](/cells/zh/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少 Cell.calculate 方法的计算时间](/cells/zh/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [检测循环引用](/cells/zh/nodejs-cpp/detecting-circular-reference/)
- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [中断或取消工作簿的公式计算](/cells/zh/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [设置工作簿的公式计算模式](/cells/zh/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [在 Aspose.Cells 中使用 FormulaText 函数](/cells/zh/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
