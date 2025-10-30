---
title: Spezifische Arbeitsblätter in einer Arbeitsmappe mit Node.js über C++ laden
linktitle: Bestimmte Arbeitsblätter in einem Arbeitsbuch laden
type: docs
weight: 100
url: /de/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ bestimmte Arbeitsblätter in einer Arbeitsmappe laden. Verbessern Sie die Leistung und reduzieren Sie den Speicherverbrauch.
---

{{% alert color="primary" %}}

Standardmäßig lädt Aspose.Cells die gesamte Tabellenkalkulation in den Speicher. Es ist möglich, nur bestimmte Blätter zu laden. Dies kann die Leistung verbessern und weniger Speicher verbrauchen. Dieser Ansatz ist nützlich, wenn Sie mit einem großen Arbeitsbuch arbeiten, das aus vielen Arbeitsblättern besteht.

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

Hier ist die Implementierung der Klasse CustomLoad.

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
