---
title: Supprimer les plages nommées avec Node.js via C++
linktitle: Supprimer les plages nommées
type: docs
weight: 90
url: /fr/nodejs-cpp/Delete-named-ranges/
description: Vous pouvez apprendre comment supprimer des noms définis ou plages nommées à partir de fichiers Excel ou OpenOffice avec Aspose.Cells for Node.js via C++.
---

## **Introduction**
S'il y a trop de noms définis ou de plages nommées dans les fichiers Excel, nous devons en effacer certains car ils ne sont plus référencés.

## **Supprimer une plage nommée dans MS Excel**

Pour supprimer une plage nommée dans Excel, suivez les étapes suivantes :
1. Ouvrez Microsoft Excel et ouvrez le classeur contenant la plage nommée.
2. Allez à l'onglet "Formules" dans le ruban Excel.
3. Cliquez sur le bouton "Gestionnaire de noms" dans le groupe "Noms définis". Cela ouvrira la boîte de dialogue Gestionnaire de noms.
4. Dans la boîte de dialogue Gestionnaire de noms, sélectionnez la plage nommée que vous souhaitez supprimer.
5. Cliquez sur le bouton "Supprimer". Confirmez la suppression lorsqu'on vous le demande.
6. Cliquez sur le bouton "Fermer" pour fermer la boîte de dialogue Gestionnaire de noms.
7. Enregistrez le classeur pour conserver les modifications.

## **Supprimer une plage nommée avec Aspose.Cells for Node.js via C++**
Avec Aspose.Cells for Node.js via C++, vous pouvez supprimer des plages nommées ou des noms définis par [texte](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) ou [index](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) dans la liste.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Remarque : si le nom défini est référencé par des formules, il ne peut pas être supprimé. Nous pouvons uniquement supprimer la formule du nom défini.

## **Supprime certaines plages nommées**
Lorsque nous supprimons un nom défini, nous devons vérifier s'il est référencé par toutes les formules du fichier.
Pour améliorer les performances de suppression des plages nommées, nous pouvons en supprimer plusieurs en même temps.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Supprimer les noms définis en double**
Certains fichiers Excel se corrompent car certains noms définis sont en double. Nous pouvons donc supprimer ces doublons pour réparer le fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



