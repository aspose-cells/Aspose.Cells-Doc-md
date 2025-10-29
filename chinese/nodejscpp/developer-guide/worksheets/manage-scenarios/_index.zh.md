---
title: 使用C++通过Node.js创建、操作或删除工作表的场景
linktitle: 管理场景
type: docs
weight: 190
url: /zh/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: 学习如何使用C++ API通过Node.js以编程方式创建、操作或删除Excel工作表中的场景。
keywords: 使用C++通过Node.js创建场景工作表，删除场景Excel工作表，操作场景工作表
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。方案是一个命名的“假设”模型，其中包含由一个或多个公式链接的可变输入单元格。在创建方案之前，设计工作表，使其至少包含一个依赖于可以插入不同值的单元格的公式。以下示例演示了如何通过Aspose.Cells API在工作簿中的工作表中创建和删除方案。

{{% /alert %}}

Aspose.Cells提供一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection)，[**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario)，[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection)和[**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell)类。它还提供[**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--)属性。下面的示例代码打开一个包含一些方案的XLSX Excel文件，然后删除现有的方案。在保存Excel文件之前，它还向工作表添加了一个新的方案。这个示例使用了一个非常简单的包含方案的模板文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate the Workbook
// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

if (worksheet.getScenarios().getCount() > 0) {
// Remove the existing first scenario from the sheet
worksheet.getScenarios().removeAt(0);

// Create a scenario
const i = worksheet.getScenarios().add("MyScenario");
// Get the scenario
const scenario = worksheet.getScenarios().get(i);
// Add comment to it
scenario.setComment("Test scenario is created.");
// Get the input cells for the scenario
const sic = scenario.getInputCells();
// Add the scenario on B4 (as changing cell) with default value
sic.add(3, 1, "1100000");

const outputFilePath = path.join(dataDir, "outBk_scenarios1.out.xlsx");

// Save the Excel file.
workbook.save(outputFilePath);
console.log("\nProcess completed successfully.\nFile saved at " + outputFilePath);
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
