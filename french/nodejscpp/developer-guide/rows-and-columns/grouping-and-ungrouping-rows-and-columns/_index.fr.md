---
title: Groupement et dégroupement des lignes et des colonnes avec Node.js via C++
linktitle: Regroupement et dégroupement des lignes et des colonnes
type: docs
weight: 50
url: /fr/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Découvrez comment grouper et dégrouper les lignes et colonnes dans Excel en utilisant Aspose.Cells for Node.js via C++.
--- 

## **Introduction**

Dans un fichier Microsoft Excel, vous pouvez créer un plan pour les données afin de vous permettre d'afficher et de masquer les niveaux de détail d'un simple clic de souris.

Cliquez sur les **symboles de plan**, 1,2,3, + et - pour afficher rapidement uniquement les lignes ou colonnes fournissant des résumés ou des en-têtes de sections dans une feuille de calcul, ou vous pouvez utiliser les symboles pour voir les détails sous un résumé ou une en-tête individuelle comme le montre la figure ci-dessous:

|**Regroupement des lignes et des colonnes.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestion des groupes de lignes et de colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une méthode [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) qui permet d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) qui représente toutes les cellules de la feuille de calcul.

La collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille de calcul; quelques-unes de ces méthodes sont décrites ci-dessous plus en détail.

### **Regrouper des lignes et des colonnes**

Il est possible de grouper des lignes ou des colonnes en appelant les méthodes [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) et [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Les deux méthodes prennent les paramètres suivants :

- Indice de la première ligne/colonne, la première ligne ou colonne du groupe.
- Indice de la dernière ligne/colonne, la dernière ligne ou colonne du groupe.
- Est caché, un paramètre booléen qui spécifie s'il faut masquer ou non les lignes/colonnes après le regroupement.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Paramètres de regroupement**

Microsoft Excel vous permet de configurer les paramètres de regroupement pour l'affichage :

- Lignes de récapitulatif en dessous des détails.
- Colonnes de récapitulatif à droite des détails.

Les développeurs peuvent configurer ces paramètres de groupe en utilisant la propriété [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

### **Lignes de résumé en dessous des détails**

Il est possible de contrôler si les lignes de résumé sont affichées en dessous des détails en réglant la propriété [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) de la classe [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) à **true** ou **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Colonnes récapitulatives à droite du détail**

Les développeurs peuvent également contrôler l'affichage des colonnes de résumé à droite des détails en réglant la propriété [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) de la classe [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) à **true** ou **false**.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Désagréger les lignes et les colonnes**

Pour désépingler des lignes ou colonnes groupées, appelez les méthodes [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) et [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Les deux méthodes prennent deux paramètres :

- Indice de la première ligne ou colonne, la première ligne/colonne à dissocier.
- Indice de la dernière ligne ou colonne, la dernière ligne/colonne à dissocier.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) possède une surcharge qui accepte un troisième paramètre Booléen. En le réglant à **true**, toutes les informations de groupe sont supprimées. Sinon, seule la information de groupe externe est supprimée.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
