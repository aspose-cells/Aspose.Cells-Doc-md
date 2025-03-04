---
title: Create, Manipulate or Remove Scenarios from Worksheets with Node.js via C++
linktitle: Manage Scenarios
type: docs
weight: 190
url: /nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Learn how to create, manipulate, or remove scenarios from Excel Worksheets programmatically using Node.js with C++ API.
keywords: create scenario worksheet node.js via C++, remove scenario excel worksheet node.js via C++, manipulate scenario worksheet node.js via C++
---

{{% alert color="primary" %}}

Sometimes, you need to create, manipulate or delete scenarios in spreadsheets. A scenario is a named 'what if?' model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so that it contains at least one formula that depends on cells that different values can be inserted into. The following example shows how to create and remove scenarios from a worksheet in a workbook via Aspose.Cells APIs.

{{% /alert %}}

Aspose.Cells provides some useful classes, for example, [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection), and [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell) classes. It also provides the [**Worksheet.Scenarios**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/properties/scenarios) property. The sample code below opens an XLSX Excel file that contains some scenarios and removes an existing scenario. It also adds a new scenario to the worksheet before saving the Excel file. The example uses a very simple template file that contains a scenario.

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
