---
title: Créer, manipuler ou supprimer des scénarios à partir de feuilles de calcul avec Node.js via C++
linktitle: Gérer des scénarios
type: docs
weight: 190
url: /fr/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Apprenez comment créer, manipuler ou supprimer des scénarios dans des feuilles de calcul Excel de manière programmatique en utilisant Node.js avec l API C++.
keywords: créer un scénario de feuille de calcul node.js via C++, supprimer un scénario de feuille de calcul excel node.js via C++, manipuler un scénario de feuille de calcul node.js via C++
---

{{% alert color="primary" %}}

Parfois, vous devez créer, manipuler ou supprimer des scénarios dans des feuilles de calcul. Un scénario est un modèle nommé de 'et si ?' qui inclut des cellules d'entrée variables liées par une ou plusieurs formules. Avant de créer un scénario, concevez la feuille de calcul de manière à ce qu'elle contienne au moins une formule dépendant de cellules dans lesquelles différentes valeurs peuvent être insérées. L'exemple suivant montre comment créer et supprimer des scénarios à partir d'une feuille de calcul dans un classeur via les API Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit quelques classes utiles, par exemple les classes [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection), et [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell). Il fournit également la propriété [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). Le code d'exemple ci-dessous ouvre un fichier Excel XLSX contenant des scénarios et supprime un scénario existant. Il ajoute également un nouveau scénario à la feuille de calcul avant d'enregistrer le fichier Excel. L'exemple utilise un fichier modèle très simple contenant un scénario.

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
