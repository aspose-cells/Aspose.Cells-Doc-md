---  
title: Détection de feuilles vides avec Node.js via C++  
linktitle: Détection de feuilles de calcul vides  
type: docs  
weight: 410  
url: /fr/nodejs-cpp/detecting-empty-worksheets/  
description: Cet article vous montre un code expliquant comment détecter automatiquement les feuilles vides des classeurs Excel en utilisant l’API Node.js avec la bibliothèque C++.  
keywords: détecter la feuille vide Node.js via C++, trouver la feuille Excel vide Node.js via C++  
---  

## **Vérifier les cellules peuplées**

Les feuilles de calcul peuvent comporter une ou plusieurs cellules remplies de valeurs où une valeur peut être simple (texte, numérique, date/heure) ou une formule ou une valeur basée sur une formule. Dans un tel cas, il est facile de détecter si une feuille donnée est vide ou non. Tout ce que nous devons vérifier, ce sont les propriétés [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) ou [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--). Si ces propriétés retournent zéro ou des valeurs positives, cela signifie qu'une ou plusieurs cellules ont été remplies; cependant, si l'une de ces propriétés retourne -1, cela indique qu'aucune cellule n'a été remplie dans la feuille donnée.

{{% alert color="primary" %}}

Les collections de lignes et de colonnes ont des indices basés sur zéro; donc, une cellule à la ligne 0 et la colonne 0 correspond à la première cellule de la feuille, qui est A1.

{{% /alert %}}

## **Vérifier les cellules initialisées vides**

Toutes les cellules ayant des valeurs sont automatiquement initialisées; cependant, il est possible qu'une feuille de calcul ait des cellules uniquement avec une mise en forme appliquée. Dans ce cas, les propriétés [**Cells.getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--) ou [**Cells.getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) retourneront -1 pour indiquer l'absence de valeurs remplies, mais les cellules initialisées en raison de la mise en forme ne peuvent pas être détectées avec cette approche. Pour vérifier si une feuille de calcul possède des cellules initialisées vides, il est conseillé d'utiliser la méthode `Enumerator.MoveNext` sur l'énumérateur obtenu à partir de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Si la méthode `Enumerator.MoveNext` retourne **true**, cela signifie qu'il y a une ou plusieurs cellules initialisées dans la feuille donnée.

## **Vérifier les formes**

Il est possible qu'une feuille donnée n'ait aucune cellule remplie; cependant, elle peut contenir des formes et objets tels que des contrôles, graphiques, images, etc. Si nous devons vérifier si une feuille contient une forme, nous pouvons le faire en inspectant la propriété [**ShapeCollection.getCount()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#getCount--). Une valeur positive indique la présence de(s) forme(s) dans la feuille.

## **Exemple de programmation**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);

// Loop over all worksheets in the workbook
for (let i = 0; i < book.getWorksheets().getCount(); i++) {
const sheet = book.getWorksheets().get(i);
// Check if worksheet has populated cells
if (sheet.getCells().getMaxDataRow() !== -1) {
console.log(`${sheet.getName()} is not empty because one or more cells are populated`);
}
// Check if worksheet has shapes
else if (sheet.getShapes().getCount() > 0) {
console.log(`${sheet.getName()} is not empty because there are one or more shapes`);
}
// Check if worksheet has empty initialized cells
else {
const range = sheet.getCells().getMaxDisplayRange();
const rangeIterator = range.getEnumerator();
if (rangeIterator.moveNext()) {
console.log(`${sheet.getName()} is not empty because one or more cells are initialized`);
}
}
}
```  

