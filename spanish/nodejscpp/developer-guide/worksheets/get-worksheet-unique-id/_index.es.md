---
title: Obtener id único de la hoja de trabajo con Node.js a través de C++
linktitle: Obtener el identificador único de la hoja de trabajo
type: docs
weight: 190
url: /es/nodejs-cpp/get-worksheet-unique-id/
description: Este artículo muestra cómo obtener el id único de la hoja de trabajo de Excel usando la biblioteca Node.js y la API en C++ de forma programática.
keywords: id único de la hoja de cálculo de Excel Node.js a través de C++, id único de hoja de trabajo Node.js a través de C++
---

## **Obtener el ID único de la hoja de trabajo**

Aspose.Cells for Node.js via C++ proporciona la capacidad de obtener el id único de una hoja de trabajo usando la propiedad [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--). El siguiente fragmento de código demuestra el uso de la propiedad [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) para imprimir el id único de una hoja de trabajo. El siguiente fragmento de código usa este [archivo de ejemplo de Excel](105480213.xlsx).

### Código Fuente

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
