---
title: Verwendung der GlobalizationSettings Klasse für benutzerdefinierte Subtotal Labels und andere Labels im Tortendiagramm mit Node.js über C++
linktitle: Verwendung der GlobalizationSettings Klasse für benutzerdefinierte Teilergebnisbezeichnungen und andere Beschriftungen des Kuchendiagramms
type: docs
weight: 70
url: /de/nodejs-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Erfahren Sie, wie man Subtotal Labels und andere Labels im Tortendiagramm mit der GlobalizationSettings Klasse in Aspose.Cells for Node.js via C++ anpasst.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells APIs haben die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse veröffentlicht, um Szenarien zu behandeln, in denen der Benutzer benutzerdefinierte Labels für Subtotals in einer Tabelle verwenden möchte. Außerdem kann die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse verwendet werden, um das **Other**-Label beim Rendern eines Arbeitsblatts oder Diagramms zu ändern.

## **Einführung in die GlobalizationSettings-Klasse**

Die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse bietet momentan die folgenden 3 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um gewünschte Labels für Subtotals oder benutzerdefinierte Texte für das **Other**-Label eines Tortendiagramms zu erhalten.

1. [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-): Gibt den Gesamtwertnamen der Funktion zurück.
1. [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-): Gibt den Gesamtergebnisnamen der Funktion zurück.


### **Benutzerdefinierte Beschriftungen für Zwischensummen**

Die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse kann verwendet werden, um die Subtotal-Labels durch Überschreiben der Methoden [**GlobalizationSettings.getTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getTotalName-consolidationfunction-) & [**GlobalizationSettings.getGrandTotalName(ConsolidationFunction)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getGrandTotalName-consolidationfunction-) wie folgt anzupassen.

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

Um benutzerdefinierte Labels einzufügen, muss die [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--)-Eigenschaft einer Instanz der oben definierten **CustomSettings**-Klasse zugewiesen werden, bevor die Subtotals zum Arbeitsblatt hinzugefügt werden.

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

Die [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings)-Klasse funktioniert nur beim Hinzufügen neuer Subtotals. Wenn ein Arbeitsblatt bereits Subtotals enthält, können deren Labels nicht geändert werden.

{{% /alert %}}

