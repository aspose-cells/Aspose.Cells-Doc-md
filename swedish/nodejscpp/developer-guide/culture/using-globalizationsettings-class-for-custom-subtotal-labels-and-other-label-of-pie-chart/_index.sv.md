---
title: Användning av GlobalizationSettings klass för anpassade subtotal etiketter och andra etiketter av cirkeldiagram med Node.js via C++
linktitle: Användning av klassen GlobalizationSettings för anpassade subtotalmärken och andra märken för cirkeldiagram
type: docs
weight: 70
url: /sv/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Lär dig hur du anpassar subtotal etiketter och andra etiketter för cirkeldiagram med hjälp av GlobalizationSettings klassen i Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells API:er har exponerat [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen för att hantera scenarier där användaren vill använda anpassade etiketter för subtotals i ett kalkylblad. Dessutom kan [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen användas för att ändra **Andra**-etiketten för cirkeldiagrammet när du renderar arbetsblad eller diagram.

## **Introduktion till klassen GlobalizationSettings**

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen erbjuder för närvarande följande 3 metoder som kan överskridas i en anpassad klass för att få önskade etiketter för subtotals eller för att rendera anpassad text för **Andra**-etiketten i en cirkeldiagram.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Hämtar det totala namnet på funktionen.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Hämtar det totala namnet på den totala funktionen.


### **Anpassade etiketter för subtotaler**

För att injicera anpassade etiketter måste du tilldela [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-egenskapen till en instans av den ovan nämnda **CustomSettings**-klassen innan du lägger till Subtotals till arbetsbladet.

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

För att injicera anpassade etiketter krävs det att tilldela [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)-egenskapen till en instans av klassen **CustomSettings** som definierats ovan innan du lägger till delsumma i kalkylbladet.

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

[**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-klassen fungerar endast för att lägga till nya subtotals. Om ett kalkylblad redan innehåller subtotals kan deras etiketter inte ändras.

{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
