---
title: Obtenir l ID unique de la feuille de calcul avec Node.js via C++
linktitle: Obtenir l identifiant unique de la feuille de calcul
type: docs
weight: 190
url: /fr/nodejs-cpp/get-worksheet-unique-id/
description: Cet article montre comment obtenir l ID unique d une feuille de calcul Excel en utilisant la bibliothèque Node.js et l API C++ de manière programmatique.
keywords: ID unique de la feuille de calcul Excel Node.js via C++, ID unique de la feuille de calcul Node.js via C++
---

## **Obtenir l'identifiant unique de la feuille de calcul**

 Aspose.Cells for Node.js via C++ offre la possibilité d'obtenir l'ID unique d'une feuille de calcul en utilisant la propriété [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--). Le code suivant démontre l'utilisation de la propriété [**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--) pour afficher l'ID unique d'une feuille. Le code utilise ce [fichier Excel d'exemple](105480213.xlsx).

### Code source

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
{{< app/cells/assistant language="nodejs-cpp" >}}
