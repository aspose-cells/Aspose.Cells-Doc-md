---
title: Sök och ersätt data i ett område med Node.js via C++
linktitle: Sök och ersätt data i ett intervall
type: docs
weight: 170
url: /sv/nodejs-cpp/search-and-replace-data-in-a-range/
description: Denna artikel visar hur man söker och ersätter data i ett område i Excel med hjälp av Node.js via C++ kod.
keywords: node.js sök och ersätt data i excel, node.js sök data i excel, node.js sök och ersätt data i ett område, node.js sök data i ett område, node.js sökar data i ett område, node.js sökar data i område, node.js sökar data i excel, node.js sök data i område, sök och ersätt data i excel med node.js, sök och ersätt data i ett område med node.js, sök och ersätt data i område med node.js
---

{{% alert color="primary" %}}

Ibland behöver du söka efter och ersätta specifik data i ett område utan att ta hänsyn till cellvärden utanför det önskade området. Aspose.Cells for Node.js via C++ gör det möjligt att begränsa en sökning till ett specifikt område. Denna artikel förklarar hur.

{{% /alert %}}

Aspose.Cells for Node.js via C++ tillhandahåller metoden [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) för att specificera ett område vid sökning efter data. Nedan visas ett kodexempel som söker och byter ut data i ett område.

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
