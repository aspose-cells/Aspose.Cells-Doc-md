---
title: Comment imprimer Excel en pages adaptées, en largeur et en hauteur avec Node.js via C++
linktitle: Comment imprimer Excel en pages adaptées en largeur et en hauteur
type: docs
weight: 200
url: /fr/nodejs-cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Cet article vous montre un code expliquant comment définir FitToPagesWide et FitToPagesTall en utilisant Aspose.Cells for Node.js via C++.
keywords: Node.js via C++ Comment définir FitToPagesWide et FitToPagesTall, Comment ajouter FitToPagesWide et FitToPagesTall dans Node.js, Comment définir FitToPagesWide et FitToPagesTall dans Excel, Comment effacer FitToPagesWide et FitToPagesTall dans Excel, Comment imprimer Excel en pages ajustées en largeur et en hauteur, Comment imprimer une feuille de calcul en une seule page, Comment imprimer toutes les colonnes d une feuille dans une seule page.
---

## **Introduction**

Les réglages FitToPagesWide et FitToPagesTall sont utilisés dans les applications de tableur (comme Microsoft Excel) pour contrôler la mise à l'échelle d'une feuille lors de l'impression. Ces réglages aident à s'assurer que votre sortie imprimée rentre dans un nombre spécifié de pages, horizontalement et verticalement. Voici une explication de chaque réglage :

1. FitToPagesWide : Ce réglage spécifie le nombre de pages en largeur dans lesquelles le contenu imprimé doit tenir. Par exemple, définir FitToPagesWide à 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule largeur de page, peu importe la largeur de la feuille.
2. FitToPagesTall : Ce paramètre indique le nombre de pages en hauteur dans lesquelles le résultat imprimé doit s'adapter. Par exemple, définir FitToPagesTall sur 1 signifie que le contenu sera mis à l'échelle pour tenir dans une seule hauteur de page, indépendamment du nombre de lignes.

## **Pourquoi utiliser FitToPagesWide et FitToPagesTall**
Voici quelques raisons de définir FitToPagesWide et FitToPagesTall :
1. Contrôle de la mise en page imprimée : En spécifiant le nombre de pages en largeur et en hauteur, vous pouvez vous assurer que votre document imprimé est facile à lire et bien organisé, sans que des colonnes ou lignes soient mal réparties sur plusieurs pages.
2. Cohérence : Si vous imprimez plusieurs feuilles ou rapports, l'utilisation de ces paramètres permet de maintenir un format cohérent, facilitant la comparaison et l'analyse des documents imprimés.
3. Présentation professionnelle : La mise à l'échelle appropriée et la taille du contenu pour un nombre spécifique de pages peuvent donner une présentation plus professionnelle et soignée de vos données.

## **Comment imprimer un fichier en pages adaptées en largeur et en hauteur dans Excel**

Pour définir les paramètres FitToPagesWide et FitToPagesTall dans Microsoft Excel, suivez ces étapes :

1. Ouvrez votre classeur Excel et allez à la feuille que vous souhaitez imprimer.
2. Accédez à l'onglet Mise en page dans le ruban.
3. Dans le groupe Mise en page, cliquez sur la petite flèche en bas à droite pour ouvrir la boîte de dialogue Mise en page.
4. Dans la boîte de dialogue Mise en page, allez à l'onglet Page.
5. Sous Échelle, sélectionnez l'option "Ajuster à" puis spécifiez le nombre de pages en largeur et en hauteur souhaité : Entrez le nombre de pages en largeur dans la première case (Ajuster à x pages en largeur). Entrez le nombre de pages en hauteur dans la deuxième case (Ajuster à y pages en hauteur).
<br>
<img src="2.png" width=60% />

6. Cliquez sur OK pour appliquer les paramètres.

## **Comment imprimer Excel en pages ajustées en largeur et en hauteur avec Aspose.Cells for Node.js via C++**

Pour définir FitToPagesWide et FitToPagesTall pour une feuille spécifiée : chargez d'abord le [fichier d'exemple](input.xlsx), puis modifiez les propriétés [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) et [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--) de l'objet [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) pour la feuille souhaitée. Voici un exemple en Node.js :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the number of pages to which the length of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned
worksheet.getPageSetup().setFitToPagesWide(1);

// Save the workbook
workbook.save("out_net.pdf");
```

Le résultat en sortie :
<br>
<img src="1.png" width=60% />

## **Comment imprimer une feuille de calcul en une seule page avec Aspose.Cells for Node.js via C++**

Pour imprimer une feuille de calcul en une seule page : chargez d'abord le [fichier d'exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Voici un exemple en Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the workbook.
workbook.save("OnePagePerSheet.pdf", options);
```

Le résultat en sortie :
<br>
<img src="3.png" width=60% />

## **Comment imprimer toutes les colonnes de la feuille de calcul sur une seule page en utilisant Aspose.Cells for Node.js via C++**

Pour imprimer toutes les colonnes d'une feuille de calcul sur une seule page : Tout d'abord, chargez le [fichier d'exemple](sample.xlsx), puis vous devez définir la propriété [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) de l'objet [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/). Voici un exemple en Node.js :

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setAllColumnsInOnePagePerSheet(true);

// Save the workbook.
workbook.save("AllColumnsInOnePagePerSheet.pdf", options);
```

Le résultat en sortie :
<br>
<img src="4.png" width=60% />
