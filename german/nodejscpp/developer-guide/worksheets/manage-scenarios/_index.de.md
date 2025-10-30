---
title: Szenarien in Arbeitsblättern mit Node.js über C++ erstellen, manipulieren oder entfernen
linktitle: Szenarien verwalten
type: docs
weight: 190
url: /de/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Lernen Sie, wie Sie Szenarien in Excel Tabellen programmatisch mit Node.js und C++ API erstellen, manipulieren oder entfernen.
keywords: Szenario erstellen Node.js via C++, Szenario aus Excel Arbeitsblatt entfernen Node.js via C++, Szenario manipulieren Node.js via C++
---

{{% alert color="primary" %}}

Manchmal müssen Sie Szenarien in Tabellenkalkulationen erstellen, manipulieren oder löschen. Ein Szenario ist ein benanntes 'Was-wäre-wenn?'-Modell, das variable Eingabezellen enthält, die durch eine oder mehrere Formeln verknüpft sind. Vor dem Erstellen eines Szenarios entwerfen Sie das Arbeitsblatt so, dass es mindestens eine Formel enthält, die von Zellen abhängt, in die unterschiedliche Werte eingegeben werden können. Das folgende Beispiel zeigt, wie Sie Szenarien in einem Arbeitsblatt einer Arbeitsmappe über die Aspose.Cells-APIs erstellen und entfernen.

{{% /alert %}}

Aspose.Cells bietet einige nützliche Klassen, wie z.B. [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection) und [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell) Klassen. Es bietet auch die [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--)-Eigenschaft. Der Beispielscode unten öffnet eine XLSX-Excel-Datei, die einige Szenarien enthält, und entfernt ein vorhandenes Szenario. Es fügt auch ein neues Szenario zum Arbeitsblatt hinzu, bevor die Excel-Datei gespeichert wird. Das Beispiel verwendet eine sehr einfache Vorlagendatei, die ein Szenario enthält.

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
