---
title: Visa formler istället för värden i ett kalkylblad med Node.js via C++
linktitle: Visa formler istället för värden i ett kalkylblad
type: docs
weight: 20
url: /sv/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Den här artikeln ger exempel på kod för att använda Node.js API et via C++ för att programmässigt visa formler istället för värden i ett Excel kalkylblad eller kalkylblad.
---

{{% alert color="primary" %}}

Det är möjligt att visa formler istället för beräknade värden i Microsoft Excel med hjälp av alternativet **Visa formler** från fliken **Formler**. När formler visas visar Microsoft Excel formler i kalkylbladet. Du kan uppnå samma sak med Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells tillhandahåller en egenskap [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Sätt den till **true** för att göra Microsoft Excel att visa formler.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
