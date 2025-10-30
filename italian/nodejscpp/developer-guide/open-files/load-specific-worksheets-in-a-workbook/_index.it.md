---
title: Carica fogli di lavoro specifici in un workbook con Node.js tramite C++
linktitle: Carica specifici fogli di lavoro in un libro di lavoro
type: docs
weight: 100
url: /it/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Impara come caricare fogli di lavoro specifici in un workbook usando Aspose.Cells for Node.js via C++. Migliora le prestazioni e riduci il consumo di memoria.
---

{{% alert color="primary" %}}

Per impostazione predefinita, Aspose.Cells carica l'intero foglio di calcolo in memoria. È possibile caricare solo fogli specifici. Questo può migliorare le prestazioni e consumare meno memoria. Questo approccio è utile quando si lavora con un ampio libro di lavoro composto da molti fogli di lavoro.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Define a new Workbook.
let workbook;

// Load the workbook with the specified worksheet only.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
loadOptions.setLoadFilter(new CustomLoad());

// Create the workbook.
workbook = new AsposeCells.Workbook(path.join(dataDir, "TestData.xlsx"), loadOptions);

// Perform your desired task.

// Save the workbook.
workbook.save(path.join(dataDir, "outputFile.out.xlsx"));
```

Ecco l’implementazione della classe CustomLoad.

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoad extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "Sheet2") {
// Load everything from worksheet "Sheet2"
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.All);
} else {
// Load nothing
this.setLoadDataFilterOptions(AsposeCells.LoadDataFilterOptions.Structure);
}
}
}
```


{{< app/cells/assistant language="nodejs-cpp" >}}
