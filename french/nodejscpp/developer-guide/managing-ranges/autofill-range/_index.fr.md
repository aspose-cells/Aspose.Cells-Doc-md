---
title: Remplissage automatique d une plage de fichier Excel avec Node.js via C++
linktitle: Plage de remplissage automatique
type: docs
weight: 105
url: /fr/nodejs-cpp/autofill-ranges/
description: Apprenez comment effectuer une opération de remplissage automatique dans une plage spécifiée d un fichier Excel en utilisant Aspose.Cells for Node.js via C++.
---

##  **Effectuer un remplissage automatique dans la plage spécifiée dans Excel**

Dans Excel, sélectionnez une plage, déplacez la souris vers le coin inférieur droit, et faites glisser le "plus" pour remplir automatiquement les données.

## **Remplir automatiquement les plages avec Aspose.Cells for Node.js via C++**

L'exemple suivant montre comment effectuer une opération de remplissage automatique sur une plage, et voici le fichier d'exemple pouvant être téléchargé pour tester cette fonctionnalité :

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
