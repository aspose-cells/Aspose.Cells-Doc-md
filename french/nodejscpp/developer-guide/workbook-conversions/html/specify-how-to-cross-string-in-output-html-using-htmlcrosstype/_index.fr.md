---
title: Spécifiez comment gérer la coupure de chaîne dans le HTML de sortie en utilisant HtmlCrossType avec Node.js via C++
linktitle: Définir comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType
type: docs
weight: 140
url: /fr/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Apprenez à contrôler le débordement de chaîne dans le HTML en spécifiant HtmlCrossType en Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu’elle dépasse la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez contrôler ce débordement en spécifiant le type de croisement à l’aide de l’énumération [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Elle possède les valeurs suivantes :

- **HtmlCrossType.Default** : Affichage comme MS Excel ; dépend de la prochaine cellule. Si la cellule suivante est nulle, la chaîne passera ou sera tronquée.

- **HtmlCrossType.MSExport** : Affiche la chaîne comme dans MS Excel exportant HTML.

- **HtmlCrossType.Cross**: Afficher la chaîne HTML croisée; la performance pour la création de grands fichiers HTML sera plus de dix fois plus rapide que de définir la valeur sur Default ou FitToCell.

- **HtmlCrossType.FitToCell** : affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType**

 Le code exemple suivant charge le [fichier Excel d'exemple](51740732.xlsx) et le sauvegarde au format HTML en spécifiant différents [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Veuillez télécharger les [HTMLs de sortie](51740734.zip) générés avec ce code. Le fichier Excel exemple contient une image bordée en rouge comme montré dans cette capture d'écran, illustrant l'effet des valeurs [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) sur le HTML de sortie.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
