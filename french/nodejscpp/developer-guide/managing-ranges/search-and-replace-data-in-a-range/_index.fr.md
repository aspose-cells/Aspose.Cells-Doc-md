---
title: Rechercher et remplacer des données dans une plage avec Node.js via C++
linktitle: Rechercher et remplacer des données dans une plage
type: docs
weight: 170
url: /fr/nodejs-cpp/search-and-replace-data-in-a-range/
description: Cet article explique comment rechercher et remplacer des données dans une plage dans Excel en utilisant Node.js via du code C++.
keywords: node.js recherche et remplace des données dans excel, node.js recherche des données dans excel, node.js recherche et remplace des données dans une plage, node.js recherche des données dans une plage, node.js recherche des données dans une plage, node.js recherche des données dans la plage, node.js recherche des données dans excel, node.js recherche des données dans la plage, recherche et remplace des données dans excel avec node.js, recherche et remplace des données dans une plage avec node.js, recherche et remplace des données dans une plage avec node.js
---

{{% alert color="primary" %}}

Parfois, vous devez rechercher et remplacer des données spécifiques dans une plage en ignorant les valeurs de cellules en dehors de la plage souhaitée. Aspose.Cells for Node.js via C++ vous permet de limiter une recherche à une plage spécifique. Cet article explique comment.

{{% /alert %}}

Aspose.Cells for Node.js via C++ fournit la méthode [**FindOptions.setRange(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setRange-cellarea-) pour spécifier une plage lors de la recherche de données. Le code ci-dessous recherche et remplace des données dans une plage.

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
