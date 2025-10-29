---
title: Fusionner ou désfusionner une plage de cellules avec Node.js via C++
linktitle: Fusionner ou séparer une plage de cellules
type: docs
weight: 190
url: /fr/nodejs-cpp/merge-or-unmerge-range-of-cells/
description: Fusionner et désfusionner des cellules dans une plage dans Excel avec du code Node.js via C++.
keywords: Fusionner et désfusionner des cellules dans une plage avec Node.js, fusionner et désfusionner des cellules en utilisant Node.js, fusionner et désfusionner des cellules dans une plage avec Node.js, utiliser Node.js pour fusionner et désfusionner des cellules dans Excel.
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour fusionner ou diviser une plage de cellules. Aspose.Cells fournit les méthodes [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) et [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--) à cette fin. Cet article explique comment fusionner une plage de cellules dans une cellule unique.

{{% /alert %}}

## **Exemple**

Le code d'échantillon suivant crée d'abord une plage - A1:D4 - puis fusionne les cellules de la plage en une seule cellule en utilisant la méthode [**Range.merge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--). De même, vous pouvez diviser des cellules en créant une plage et en appelant la méthode [**Range.unMerge()**](https://reference.aspose.com/cells/nodejs-cpp/range/#unMerge--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a range
const range = worksheet.getCells().createRange("A1:D4");

// Merge range into a single cell
range.merge();

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
