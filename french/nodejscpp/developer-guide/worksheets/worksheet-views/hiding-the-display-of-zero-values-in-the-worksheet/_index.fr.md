---
title: Cacher l affichage des valeurs zéro dans la feuille de calcul avec Node.js via C++
linktitle: Masquer l affichage des valeurs zéro dans la feuille de calcul
type: docs
weight: 50
url: /fr/nodejs-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Cet article vous montrera un code d exemple expliquant comment masquer de manière programmatique les valeurs zéro dans une feuille Excel en utilisant la bibliothèque Node.js via C++.
keywords: Cacher les valeurs zéro dans la feuille Excel en Node.js via C++
---

{{% alert color="primary" %}} 

Parfois, vous devez masquer les valeurs zéro dans une feuille de calcul. Cela peut être une préférence personnelle ou une norme de formatage.

{{% /alert %}} 

Pour masquer les valeurs zéro dans une feuille de calcul dans Microsoft Excel (par exemple Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**, puis sélectionnez l'onglet **Affichage**.
1. Désélectionnez l'option **Zéro**.
1. Cliquez sur **OK**.

Veuillez voir le code d'exemple suivant qui montre comment masquer les zéros en utilisant Aspose.Cells for Node.js via C++.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Create a new Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Get First worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Hide the zero values in the sheet
sheet.setDisplayZeros(false);

// Save the workbook
workbook.save(path.join(dataDir, "outputfile.out.xlsx"));
```
