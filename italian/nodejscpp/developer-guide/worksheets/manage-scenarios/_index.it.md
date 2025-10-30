---
title: Crea, manipola o rimuovi scenari dai Fogli di Lavoro con Node.js tramite C++
linktitle: Gestire gli scenari
type: docs
weight: 190
url: /it/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Impara come creare, manipolare o rimuovere scenari dai Fogli di Lavoro in Excel programmaticamente usando Node.js con API C++.
keywords: crea scenario foglio di lavoro node.js tramite C++, rimuovi scenario foglio di lavoro excel node.js tramite C++, manipola scenario foglio di lavoro node.js tramite C++
---

{{% alert color="primary" %}}

A volte è necessario creare, manipolare o eliminare scenari nei fogli di calcolo. Uno scenario è un modello 'cosa succederebbe se?' che include celle di input variabili collegate da una o più formule. Prima di creare uno scenario, progetta il foglio di lavoro in modo che contenga almeno una formula che dipende da celle in cui possono essere inseriti valori diversi. L'esempio seguente mostra come creare e rimuovere scenari da un foglio di lavoro in un libro tramite le API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fornisce alcune classi utili, ad esempio, classi [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection) e [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell). Fornisce anche la proprietà [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). Il codice di esempio di seguito apre un file Excel XLSX che contiene alcuni scenari e rimuove uno scenario esistente. Aggiunge anche un nuovo scenario al foglio di lavoro prima di salvare il file Excel. L'esempio utilizza un file di modello molto semplice che contiene uno scenario.

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
