---
title: Créer des plages nommées dépendant du classeur et de la feuille avec Node.js via C++
linktitle: Plage nommée
type: docs
weight: 40
url: /fr/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Découvrez comment créer des plages nommées dépendant du classeur et de la feuille en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells for Node.js via C++ offre la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées dépendant du classeur et de la feuille. Lors de la création d'une plage nommée dépendant d'une feuille, la référence à la feuille doit être utilisée dans la plage nommée pour la spécifier comme une plage dépendant de la feuille.

{{% /alert %}} 
## **Ajout d'une plage nommée au niveau du classeur**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Ajout d'une plage nommée avec une portée de feuille de calcul**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Sujets avancés**
- [Créer un accès et copier des plages nommées](/cells/fr/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Formater et modifier des plages nommées](/cells/fr/nodejs-cpp/format-and-modify-named-ranges/)
- [Obtenir une plage avec des liens externes](/cells/fr/nodejs-cpp/get-range-with-external-links/)
- [Mise en œuvre de plages non séquentielles](/cells/fr/nodejs-cpp/implementing-non-sequential-ranges/)


