---
title: Afficher les formules au lieu des valeurs dans une feuille de calcul avec Node.js via C++
linktitle: Afficher les formules au lieu des valeurs dans une feuille de calcul
type: docs
weight: 20
url: /fr/nodejs-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Cet article fournit un exemple de code pour utiliser l API Node.js via C++ afin d afficher de manière programmatique les formules plutôt que les valeurs dans une feuille de calcul ou un classeur Excel.
---

{{% alert color="primary" %}}

Il est possible d'afficher les formules au lieu des valeurs calculées dans Microsoft Excel en utilisant l'option **Afficher les formules** du ruban **Formules**. Lorsque les formules sont affichées, Microsoft Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir le même résultat en utilisant Aspose.Cells for Node.js via C++.

{{% /alert %}}

Aspose.Cells fournit une propriété [**Worksheet.getShowFormulas()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getShowFormulas--). Définissez-la sur **true** pour que Microsoft Excel affiche les formules.

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
