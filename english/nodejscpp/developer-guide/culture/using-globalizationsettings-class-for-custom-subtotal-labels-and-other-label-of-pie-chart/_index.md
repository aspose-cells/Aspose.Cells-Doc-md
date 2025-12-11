---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and the Other Label of a Pie Chart with Node.js via C++
linktitle: Using GlobalizationSettings Class for Custom Subtotal Labels and the Other Label of a Pie Chart
type: docs
weight: 70
url: /nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Learn how to customize subtotal labels and the other label of pie charts using the GlobalizationSettings class in Aspose.Cells for Node.js via C++.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells APIs have exposed the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class in order to handle scenarios where the user wishes to use custom labels for subtotals in a spreadsheet. Moreover, the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class can also be used to modify the **Other** label for a pie chart while rendering a worksheet or chart.

## **Introduction to GlobalizationSettings Class**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class currently offers the following three methods, which can be overridden in a custom class to obtain desired labels for the subtotals or to render custom text for the **Other** label of a pie chart.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Gets the total name of the function.  
2. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Gets the grand total name of the function.

### **Custom Labels for Subtotals**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class can be used to customize the subtotal labels by overriding the [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) and [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) methods, as demonstrated below.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings
class CustomSettings extends AsposeCells.GlobalizationSettings {
    // Overrides the getTotalName method
    getTotalName(functionType) {
        // Checks the function type used to add the subtotals
        switch (functionType) {
            // Returns a custom value based on the function type used to add the subtotals
            case AsposeCells.ConsolidationFunction.Average:
                return "AVG";
            // Handle other cases as required
            default:
                return super.getTotalName(functionType);
        }
    }

    // Overrides the getGrandTotalName method
    getGrandTotalName(functionType) {
        // Checks the function type used to add the subtotals
        switch (functionType) {
            // Returns a custom value based on the function type used to add the subtotals
            case AsposeCells.ConsolidationFunction.Average:
                return "GRD AVG";
            // Handle other cases as required
            default:
                return super.getGrandTotalName(functionType);
        }
    }
}
```

To inject custom labels, assign the `WorkbookSettings.setGlobalizationSettings()` property to an instance of the **CustomSettings** class defined above before adding the subtotals to the worksheet.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Defines a custom class derived from GlobalizationSettings
class CustomSettings extends AsposeCells.GlobalizationSettings {
    // Overrides the getTotalName method
    getTotalName(functionType) {
        switch (functionType) {
            case AsposeCells.ConsolidationFunction.Average:
                return "AVG";
            default:
                return super.getTotalName(functionType);
        }
    }

    // Overrides the getGrandTotalName method
    getGrandTotalName(functionType) {
        switch (functionType) {
            case AsposeCells.ConsolidationFunction.Average:
                return "GRD AVG";
            default:
                return super.getGrandTotalName(functionType);
        }
    }
}

try {
    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");

    // Loads an existing spreadsheet containing some data
    const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

    // Assigns the GlobalizationSettings property of the WorkbookSettings class to a custom class instance
    workbook.getSettings().setGlobalizationSettings(new CustomSettings());

    // Accesses the first worksheet, which contains data in the range A2:B9
    const sheet = workbook.getWorksheets().get(0);

    // Adds a subtotal of type Average to the worksheet
    sheet.getCells().subtotal(AsposeCells.CellArea.createCellArea("A2", "B9"), 0, AsposeCells.ConsolidationFunction.Average, [1]);

    // Calculates formulas
    workbook.calculateFormula();

    // Auto-fits all columns
    sheet.autoFitColumns();

    // Saves the workbook to disk
    workbook.save(path.join(dataDir, "output_out.xlsx"));
} catch (error) {
    console.error(`Test failed: ${error.message}`);
    throw error;
}
```

{{% alert color="primary" %}}
The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class only works for adding new subtotals. If a spreadsheet already contains subtotals, their labels cannot be modified.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
