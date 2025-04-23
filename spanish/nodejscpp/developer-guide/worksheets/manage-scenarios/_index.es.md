---
title: Crear, Manipular o Eliminar Escenarios de las hojas de trabajo con Node.js a través de C++
linktitle: Gestionar Escenarios
type: docs
weight: 190
url: /es/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: Aprende cómo crear, manipular o eliminar escenarios de hojas de Excel de forma programática usando Node.js con API en C++.
keywords: crear escenario en hoja de trabajo con node.js vía C++, eliminar escenario en hoja de Excel con node.js vía C++, manipular escenario en hoja de trabajo con node.js vía C++
---

{{% alert color="primary" %}}

A veces, necesitas crear, manipular o eliminar escenarios en hojas de cálculo. Un escenario es un modelo de 'qué pasaría si' que incluye celdas de entrada variables vinculadas por una o más fórmulas. Antes de crear un escenario, diseña la hoja de cálculo para que contenga al menos una fórmula que dependa de celdas en las que se puedan insertar diferentes valores. El siguiente ejemplo muestra cómo crear y eliminar escenarios de una hoja de cálculo en un libro mediante las API de Aspose.Cells.

{{% /alert %}}

Aspose.Cells proporciona algunas clases útiles, por ejemplo, las clases [**ScenarioCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/nodejs-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcellcollection), y [**ScenarioInputCell**](https://reference.aspose.com/cells/nodejs-cpp/scenarioinputcell). También proporciona la propiedad [**Worksheet.getScenarios()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getScenarios--). El código de ejemplo a continuación abre un archivo de Excel XLSX que contiene algunos escenarios y elimina un escenario existente. También agrega un nuevo escenario a la hoja de cálculo antes de guardar el archivo de Excel. El ejemplo utiliza un archivo de plantilla muy simple que contiene un escenario.

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
