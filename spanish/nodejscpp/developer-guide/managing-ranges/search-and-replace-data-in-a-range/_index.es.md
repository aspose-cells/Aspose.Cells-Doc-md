---
title: Buscar y reemplazar datos en un rango con Node.js a través de C++
linktitle: Buscar y Reemplazar Datos en un Rango
type: docs
weight: 170
url: /es/nodejs-cpp/search-and-replace-data-in-a-range/
description: Este artículo muestra cómo buscar y reemplazar datos en un rango en Excel usando Node.js a través de código en C++.
keywords: buscar y reemplazar datos en Excel con Node.js, buscar datos en Excel con Node.js, buscar y reemplazar datos en un rango con Node.js, buscar datos en un rango con Node.js, buscar datos en un rango, buscar datos en Excel con Node.js, buscar datos en un rango, buscar y reemplazar datos en Excel con Node.js, buscar y reemplazar datos en un rango con Node.js, buscar y reemplazar datos en un rango con Node.js
---

{{% alert color="primary" %}}

A veces necesitas buscar y reemplazar datos específicos en un rango ignorando cualquier valor de celda fuera del rango deseado. Aspose.Cells for Node.js via C++ te permite limitar una búsqueda a un rango específico. Este artículo explica cómo.

{{% /alert %}}

Aspose.Cells for Node.js via C++ proporciona el método [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) para especificar un rango al buscar datos. El siguiente ejemplo de código busca y reemplaza datos en un rango.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

const area = AsposeCells.CellArea.createCellArea("E9", "H15");

const opts = new AsposeCells.FindOptions();
opts.setLookInType(AsposeCells.LookInType.Values);
opts.setLookAtType(AsposeCells.LookAtType.EntireContent);
opts.setRange(area);

let cell = null;

do {
cell = worksheet.getCells().find("search", cell, opts);
if (cell === null || cell.isNull()) {
break;
}
cell.putValue("replace");
} while (true);

workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
