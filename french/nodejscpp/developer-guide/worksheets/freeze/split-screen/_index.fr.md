---
title: Division de l écran de la feuille Excel avec Node.js via C++
linktitle: Écran scindé
type: docs
weight: 190
url: /fr/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: Dans cet article, vous apprendrez comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties de manière programmatique en utilisant Node.js C++ Addon.
keywords: Figer les premières lignes, Figer la première ligne.
---

## **Introduction**

Dans cet article, nous apprendrons comment afficher certaines lignes et/ou colonnes dans des volets séparés en divisant la feuille de calcul en deux ou quatre parties. Lorsqu'on travaille avec de grands ensembles de données, il est nécessaire de voir quelques zones de la même feuille à la fois pour comparer différents sous-ensembles de données. La fonction de division d’écran peut répondre à vos besoins.

## **Comment scinder l'écran dans Excel**
Pour diviser une feuille de calcul en deux ou quatre parties, procédez comme suit :

1. Sélectionnez la ligne/colonne/cellule avant laquelle vous souhaitez placer la division.
2. Sur l'onglet Affichage, dans le groupe Fenêtres, cliquez sur le bouton Fractionner.

**![Écran partagé](Split-Screen.png)**

## **Fractionner la feuille de calcul verticalement sur les colonnes**

Pour séparer deux zones de la feuille de calcul verticalement, sélectionnez la colonne à droite de la colonne où vous souhaitez afficher la division et cliquez sur le bouton Fractionner dans Excel.

Il est facile de diviser verticalement une feuille de calcul en colonnes de manière programmatique avec Aspose.Cells for Node.js via C++, il suffit de sélectionner une cellule dans la ligne supérieure comme cellule active, puis de diviser avec la méthode [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **Fractionner la feuille de calcul horizontalement sur les lignes**
Pour séparer votre fenêtre Excel horizontalement, sélectionnez la ligne en dessous de la ligne où vous souhaitez que la division se produise dans Excel.

Il est facile de diviser horizontalement une feuille de calcul en lignes de manière programmatique avec Aspose.Cells for Node.js via C++, il suffit de sélectionner une cellule dans la colonne de gauche comme cellule active, puis de diviser avec la méthode [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **Fractionner la feuille de calcul en quatre parties**
Pour afficher quatre sections différentes de la même feuille de calcul simultanément, divisez votre écran à la fois verticalement et horizontalement dans Excel.

Il est facile de diviser une feuille de calcul verticalement par colonnes de manière programmatique avec Aspose.Cells for Node.js via C++, il suffit de sélectionner une cellule qui n'est pas dans la première ligne et la première colonne comme cellule active, puis de diviser avec la méthode [**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **Comment supprimer la division**
Pour supprimer la division de la feuille de calcul, il suffit de cliquer à nouveau sur le bouton Fractionner.

Aspose.Cells for Node.js via C++ fournit une méthode [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) pour supprimer le paramètre de division.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

{{< app/cells/assistant language="nodejs-cpp" >}}
