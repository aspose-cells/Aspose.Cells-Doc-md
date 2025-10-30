---
title: Skapa, manipulera eller ta bort scenarier från arbetsblad med Node.js via C++
linktitle: Hantera scenarier
type: docs
weight: 190
url: /sv/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Lär dig hur du skapar, manipulerar eller tar bort scenarier från Excel arbetsblad programmässigt med Node.js och C++ API.
keywords: skapa scenario arbetsblad node.js via C++, ta bort scenario excel arbetsblad node.js via C++, manipulera scenario arbetsblad node.js via C++
---

{{% alert color="primary" %}}

Ibland behöver du skapa, manipulera eller radera scenarier i kalkylblad. Ett scenario är en namngiven 'vad om?'-modell som inkluderar variabelindataceller kopplade av en eller flera formler. Innan scenariot skapas, utforma kalkylbladet så att det innehåller minst en formel som beror på celler där olika värden kan sättas in. Följande exempel visar hur man skapar och tar bort scenarier från ett kalkylblad i en arbetsbok via Aspose.Cells-API:  

{{% /alert %}}

Aspose.Cells tillhandahåller några användbara klasser, till exempel [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection), och [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell) klasser. Det tillhandahåller också egenskapen [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). Exempelkoden nedan öppnar en XLSX Excel-fil som innehåller några scenarier och tar bort ett befintligt scenario. Det lägger också till ett nytt scenario i kalkylbladet före att spara Excel-filen. Exemplet använder en mycket enkel mallfil som innehåller ett scenario.

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
