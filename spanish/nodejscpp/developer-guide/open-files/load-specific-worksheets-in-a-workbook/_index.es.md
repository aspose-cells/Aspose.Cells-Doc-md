---
title: Cargar hojas de trabajo específicas en un libro con Node.js vía C++
linktitle: Cargar hojas de cálculo específicas en un libro de Excel
type: docs
weight: 100
url: /es/nodejs-cpp/load-specific-worksheets-in-a-workbook/
description: Aprenda cómo cargar hojas de trabajo específicas en un libro usando Aspose.Cells for Node.js via C++. Mejore el rendimiento y reduzca el consumo de memoria.
---

{{% alert color="primary" %}}

De forma predeterminada, Aspose.Cells carga la hoja de cálculo completa en la memoria. Es posible cargar solo hojas específicas. Esto puede mejorar el rendimiento y consumir menos memoria. Este enfoque es útil cuando se trabaja con un libro de trabajo grande formado por muchas hojas de cálculo.

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

Aquí está la implementación de la clase CustomLoad.

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
