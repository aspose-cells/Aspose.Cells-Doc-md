---
title: Copier les paramètres de mise en page de la feuille source dans la feuille de destination avec Node.js via C++
linktitle: Copier les paramètres de mise en page de la feuille de calcul source dans la feuille de calcul de destination
type: docs
weight: 80
url: /fr/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Cet article explique comment utiliser l’API Node.js ou le code d’échantillon de la bibliothèque C++ pour copier les paramètres de mise en page d’une feuille source vers une feuille de destination de manière programmatique.
keywords: copier les paramètres de mise en page Node.js via C++, copier les paramètres de mise en page vers la feuille cible Node.js via C++
---

## **Scénarios d'utilisation possibles**

Lorsqu’on ajoute une nouvelle feuille à un classeur, elle contient les paramètres par défaut de *Mise en page*. Il peut arriver que vous deviez transférer ces paramètres ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) d’une feuille à une autre. Ce document explique comment copier les paramètres de mise en page d’une feuille à une autre en utilisant les API Aspose.Cells for Node.js via C++.

## **Copier les paramètres de configuration de la page de la feuille source dans la feuille de destination**

Le code d'exemple suivant illustre comment copier les *paramètres de configuration de la page* d'une feuille à une autre en utilisant la méthode [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-). Veuillez consulter le code d'exemple suivant et sa sortie console pour référence.

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Sortie console**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
