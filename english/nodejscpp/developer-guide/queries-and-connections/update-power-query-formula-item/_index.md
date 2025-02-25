---
title: Update Power Query Formula Item with Node.js via C++
linktitle: Update Power Query Formula Item
type: docs
weight: 120
url: /nodejs-cpp/update-power-query-formula-item/
description: Learn how to update the Power Query Formula item data source in an Excel file using Aspose.Cells for Node.js via C++.
---

## **Usage Scenario**

There might be cases where the data source files are moved and the Excel file is unable to locate the file. In such cases, Aspose.Cells API provides the option to update the Power Query Formula item by using the [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem) class to update the location of the source file.

## **Updating Power Query Formula Item**

Aspose.Cells API provides the ability to update Power Query Formula Items. The following code snippet demonstrates updating the data source file location in the Excel file by using the [**PowerQueryFormulaItem.value**](https://reference.aspose.com/cells/nodejs-cpp/powerqueryformulaitem/#value-string-) property. The source and output files attached for your reference.

- [Source File 1](106364953.xlsx)
- [Source File 2](106364954.xlsx)
- [Output File](106364955.xlsx)

## **Sample Code**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Working directories
const sourceDir = RunExamples.Get_SourceDirectory();
const outputDir = RunExamples.Get_OutputDirectory();

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SamplePowerQueryFormula.xlsx"));
const mashupData = workbook.getDataMashup();
mashupData.getPowerQueryFormulas().forEach(formula => {
    formula.getPowerQueryFormulaItems().forEach(item => {
        if (item.getName() === "Source") {
            item.setValue(`Excel.Workbook(File.Contents("${path.join(sourceDir, "SamplePowerQueryFormulaSource.xlsx")}", null, true)`);
        }
    });
});

// Save the output workbook.
workbook.save(path.join(outputDir, "SamplePowerQueryFormula_out.xlsx"));
```
