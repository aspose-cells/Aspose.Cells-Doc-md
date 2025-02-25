---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and Other Label of Pie Chart with Node.js via C++
linktitle: Using GlobalizationSettings Class for Custom Subtotal Labels and Other Label of Pie Chart
type: docs
weight: 70
url: /nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Learn how to customize subtotal labels and other labels of pie charts using GlobalizationSettings class in Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**

Aspose.Cells APIs have exposed the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class in order to deal with the scenarios where the user wishes to use custom labels for Subtotals in a spreadsheet. Moreover, the [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class can also be used to modify the **Other** label for the Pie chart while rendering worksheet or chart.

## **Introduction to GlobalizationSettings Class**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class currently offers the following 3 methods which can be overridden in a custom class to get desired labels for the Subtotals or to render custom text for the **Other** label of a Pie chart.

1. [**GlobalizationSettings.getTotalName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getTotalName): Gets the total name of the function.
1. [**GlobalizationSettings.getGrandTotalName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getGrandTotalName): Gets the grand total name of the function.
1. [**GlobalizationSettings.getOtherName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getOtherName): Gets the name of "Other" labels for Pie charts.

### **Custom Labels for Subtotals**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class can be used to customize the Subtotal labels by overriding the [**GlobalizationSettings.getTotalName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getTotalName) & [**GlobalizationSettings.getGrandTotalName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getGrandTotalName) methods as demonstrated ahead.

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

In order to inject custom labels, it is required to assign the [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/properties/globalizationsettings) property to an instance of the **CustomSettings** class defined above before adding the Subtotals to the worksheet.

```javascript
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
```

{{% alert color="primary" %}}

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class only works for adding new Subtotals. If a spreadsheet already contains Subtotals, their labels cannot be modified.

{{% /alert %}}

### **Custom Text for Other Label of Pie Chart**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings) class offers [**getOtherName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getOtherName) method which is useful to give the "Other" label of Pie charts a custom value. The following snippet defines a custom class and overrides the [**getOtherName**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/methods/getOtherName) method to get a custom label based on the system's culture identifier.

```javascript
const AsposeCells = require("aspose.cells.node");

class GlobalCustomSettings extends AsposeCells.ChartGlobalizationSettings {
    // Overrides the GetOtherName method
    getOtherName() {
        // Gets the culture identifier for the current system
        const lcid = new Intl.Locale(navigator.language).baseName; // Adjust this line for actual LCID retrieval
        switch (lcid) {
            // Handles case for English
            case "en-US":
                return "Other";
            // Handles case for French
            case "fr-FR":
                return "Autre";
            // Handles case for German
            case "de-DE":
                return "Andere";
            // Handle other cases
            default:
                return super.getOtherName();
        }
    }
}
```

The following snippet loads an existing spreadsheet containing a Pie chart and renders the chart to an image while utilizing the **CustomSettings** class created above.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Loads an existing spreadsheet containing a pie chart
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Assigns the GlobalizationSettings property of the WorkbookSettings class to the class created in first step
workbook.getSettings().setGlobalizationSettings(new AsposeCells.GlobalizationSettings());

// Accesses the 1st worksheet from the collection which contains pie chart
const sheet = workbook.getWorksheets().get(0);

// Accesses the 1st chart from the collection
const chart = sheet.getCharts().get(0);

// Refreshes the chart
chart.calculate();

// Renders the chart to image
chart.toImage(path.join(dataDir, "output_out.png"), new AsposeCells.ImageOrPrintOptions());
```
