---
title: Supprimer des lignes en double dans une feuille avec Node.js via C++
linktitle: Supprimer les lignes en double dans une feuille de calcul
type: docs
weight: 370
url: /fr/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Apprenez comment supprimer les lignes en double dans une feuille en utilisant Aspose.Cells for Node.js via C++ et sélectionner des colonnes spécifiques pour la vérification de duplication.
---


Supprimer les doublons est l'une des nombreuses fonctionnalités utiles de Microsoft Excel. Elle permet aux utilisateurs de supprimer les lignes en double dans une feuille de calcul, et vous pouvez choisir quelles colonnes vérifier pour les doublons.

Aspose.Cells for Node.js via C++ fournit la méthode `Cells.removeDuplicates()` pour cet usage. Vous pouvez également définir `startRow`, `startColumn`, `endRow`, et `endColumn` pour spécifier la plage de colonnes à vérifier pour les doublons.

Voici les fichiers d'exemple qui peuvent être téléchargés pour tester cette fonctionnalité :

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
