---
title: 使用GlobalizationSettings类为饼图的自定义小计标签和其他标签设置Node.js via C++
linktitle: 使用GlobalizationSettings类自定义小计标签和饼状图的其他标签
type: docs
weight: 70
url: /zh/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: 学习如何使用Aspose.Cells for Node.js via C++中的GlobalizationSettings类自定义饼图的小计标签和其他标签。
---

## **可能的使用场景**

Aspose.Cells API公开了[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)类以应对用户希望在电子表格中为小计使用自定义标签的场景。此外，[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)类也可以用于修改渲染工作表或图表时的“其他”标签。

## **GlobalizationSettings类简介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)类目前提供以下3个方法，可以在自定义类中重写以获得所需的小计标签或为饼图的“其他”标签渲染自定义文本。

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-)：获取函数的总名称。
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-)：获取函数的总计名称。


### **自定义小计标签**

可以通过重写[**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-)和[**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-)方法，使用[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)类来自定义小计标签，如下面所示。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}
```

为了注入自定义标签，在将小计添加到工作表之前，需将[**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)属性赋值为上面定义的**CustomSettings**类的实例。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Defines a custom class derived from GlobalizationSettings class
class CustomSettings extends AsposeCells.GlobalizationSettings {
// Overrides the GetTotalName method
getTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "AVG";
// Handle other cases as per requirement
default:
return super.getTotalName(functionType);
}
}

// Overrides the GetGrandTotalName method
getGrandTotalName(functionType) {
// Checks the function type used to add the subtotals
switch (functionType) {
// Returns custom value based on the function type used to add the subtotals
case AsposeCells.ConsolidationFunction.Average:
return "GRD AVG";
// Handle other cases as per requirement
default:
return super.getGrandTotalName(functionType);
}
}
}

try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing some data
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class created
workbook.getSettings().setGlobalizationSettings(new CustomSettings());

// Accesses the 1st worksheet from the collection which contains data that resides in the cell range A2:B9
const sheet = workbook.getWorksheets().get(0);

// Adds Subtotal of type Average to the worksheet
sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

// Calculates Formulas
workbook.calculateFormula();

// Auto fits all columns
sheet.autoFitColumns();

// Saves the workbook on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
console.error(`Test failed: ${error.message}`);
throw error;
}
```

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)类仅适用于添加新的小计。如果工作表已经包含小计，则无法修改其标签。

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
