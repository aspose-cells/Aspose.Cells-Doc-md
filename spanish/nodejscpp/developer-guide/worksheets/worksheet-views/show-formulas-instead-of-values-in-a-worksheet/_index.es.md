---
title: Mostrar fórmulas en lugar de valores en una hoja de trabajo con Node.js a través de C++
linktitle: Mostrar Fórmulas en lugar de Valores en una Hoja de Trabajo
type: docs
weight: 20
url: /es/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Este artículo proporciona un código de ejemplo para usar la API de Node.js a través de C++ para mostrar de forma programática fórmulas en lugar de valores en una hoja de Excel o hoja de cálculo.
---

{{% alert color="primary" %}}

Es posible mostrar fórmulas en lugar de valores calculados en Microsoft Excel usando la opción **Mostrar Fórmulas** desde la pestaña **Fórmulas**. Cuando se muestran las fórmulas, Microsoft Excel las muestra en la hoja de trabajo. Puedes lograr lo mismo usando Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells proporciona una propiedad [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Establecer esto en **true** hace que Microsoft Excel muestre fórmulas.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Load the source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Show formulas of the worksheet
worksheet.setShowFormulas(true);

// Save the workbook
workbook.save(path.join(dataDir, ".out.xlsx"));
```
