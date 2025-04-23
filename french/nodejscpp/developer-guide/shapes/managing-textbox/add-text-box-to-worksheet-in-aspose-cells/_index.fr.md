---
title: Comment ajouter/inserer une zone de texte dans une feuille de calcul avec Node.js via C++
linktitle: Ajouter une zone de texte à une feuille de calcul
type: docs
weight: 10
url: /fr/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Comment ajouter/inserer une zone de texte dans une feuille de calcul en Aspose.Cells for Node.js via C++.
keywords: ajouter/inserer du texte dans une zone de texte, Zone de texte, Excel, Aspose, Node.js via C++
---

## Ajouter une zone de texte à une feuille de calcul dans Excel

Dans le programme Excel (version 07 et supérieure), il y a deux endroits où vous pouvez insérer des zones de texte. L'un dans "insert-shapes", l'autre en haut à droite du menu "Insert".

### méthode un :

![1](1.png)

### méthode deux :

![2](2.png)

## Comment créer

Vous pouvez créer des zones de texte à texte horizontal ou vertical.

- Sélectionner l'option correspondant (horizontal ou vertical)
- Cliquez sur la page avec le bouton gauche de la souris
- Maintenez le bouton gauche enfoncé et faites glisser une distance sur la page
- Relâchez le bouton gauche

Maintenant, vous avez une zone de texte.

## Ajouter une zone de texte à une feuille de calcul en Aspose.Cells for Node.js via C++

Lorsque vous devez insérer en masse des zones de texte dans la feuille de calcul, la méthode d'insertion manuelle est évidemment une catastrophe. Si cela vous dérange, je pense que ce document vous aidera. [Aspose.Cells](https://products.aspose.com/cells/) fournit une API pour effectuer facilement des insertions en masse dans votre code.

Le code d'exemple suivant crée une zone de texte.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

Vous obtiendrez un fichier similaire à [fichier résultat](result.xlsx). Dans ce fichier, vous verrez ce qui suit :

![](52449.png)

