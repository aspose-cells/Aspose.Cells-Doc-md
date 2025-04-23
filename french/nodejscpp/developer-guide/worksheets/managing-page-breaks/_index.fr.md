---
title: Gestion des sauts de page avec Node.js via C++
linktitle: Gestion des sauts de page
type: docs
weight: 30
url: /fr/nodejs-cpp/managing-page-breaks/
description: Cet article fournit un code d exemple et explique comment ajouter, effacer ou supprimer des sauts de page spécifiques dans les feuilles Excel de manière programmatique en utilisant Aspose.Cells for Node.js via C++.
keywords: Sauts de page Node.js via C++, sauts de page Excel Node.js via C++, effacer saut de page Node.js via C++, supprimer un saut de page spécifique Node.js via C++
---

{{% alert color="primary" %}}

Selon la définition, un saut de page est un endroit dans un flux de texte où une page se termine et où la page suivante commence. Microsoft Excel permet aux utilisateurs d'ajouter des sauts de page dans n'importe quelle cellule sélectionnée d'une feuille de calcul.

L'emplacement de la cellule où le saut de page est ajouté, la page se termine et le reste des données après le saut de page est imprimé sur la page suivante lors de l'impression. En termes simples, les sauts de page divisent votre feuille de calcul en plusieurs pages selon vos spécifications. Vous pouvez également ajouter des sauts de page à vos feuilles de calcul à l'exécution à l'aide d'Aspose.Cells. Aspose.Cells permet aux développeurs d'ajouter deux types de sauts de page :

- Saut de page horizontal
- Saut de page vertical

Dans le reste de la discussion, nous décrirons comment ajouter des sauts de page horizontaux ou verticaux dans vos feuilles de calcul à l'aide d'Aspose.Cells.

{{% /alert %}}

## **Sauts de page**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit un large éventail de propriétés et de méthodes utilisées pour gérer une feuille de calcul.

Pour ajouter les sauts de page, utilisez les propriétés de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) et [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--).

Les propriétés [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) et [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) sont des collections qui peuvent contenir plusieurs sauts de page. Chaque collection contient plusieurs méthodes pour gérer les sauts de page horizontaux et verticaux.

### **Ajout de sauts de page**

Pour ajouter un saut de page dans une feuille de calcul, insérez des sauts de page verticaux et horizontaux à la cellule spécifiée en appelant les méthodes [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) et [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-). Chaque méthode d’ajout prend le nom de la cellule où le saut doit être ajouté.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

En mode Aperçu des sauts de page ou Aperçu avant impression, vous pouvez voir comment fonctionnent ces sauts de page.

{{% /alert %}}

### **Suppression d'un saut de page spécifique**

Pour supprimer un saut de page spécifique, appelez les méthodes [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) et [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-). Chaque méthode **removeAt** prend l'index du saut de page à supprimer.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Important à savoir**

Lorsque vous définissez les propriétés **fitToPages** (c'est-à-dire [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) et [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) dans les paramètres de mise en page, les paramètres de saut de page sont affectés, donc si vous imprimez la feuille, les sauts de page ne seront pas pris en compte même s'ils sont toujours définis.
