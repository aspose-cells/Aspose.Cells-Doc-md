---
title: Fusionner et défusionner des cellules avec Node.js via C++
linktitle: Fusionner et séparer des cellules
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de feuilles de calcul, qui supporte la fusion et la défusion des cellules. Cet article présente comment fusionner et défusionner des cellules en utilisant la bibliothèque Aspose.Cells, avec des options pour personnaliser le style des cellules fusionnées.
keywords: Aspose.Cells, bibliothèque Node.js, feuille de calcul, fusionner des cellules, défusionner des cellules, paramètres de style, styles personnalisés
type: docs
weight: 190
url: /fr/nodejs-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge cette fonctionnalité et peut également fusionner des cellules dans une feuille de calcul. Vous pouvez également séparer, ou diviser, les cellules fusionnées. La référence de cellule d'une cellule fusionnée est la référence de la cellule en haut à gauche de la plage sélectionnée d'origine.

{{% /alert %}} 
## **Introduction**
Vous ne souhaitez pas toujours le même nombre de cellules dans chaque ligne ou colonne. Par exemple, vous pouvez vouloir mettre un titre dans une cellule qui s'étend sur plusieurs colonnes. Ou, si vous créez une facture, vous souhaitez peut-être moins de colonnes pour le total. Pour fusionner deux cellules ou plus en une seule cellule, utilisez la fusion. Microsoft Excel permet aux utilisateurs de sélectionner des fichiers et de les fusionner pour structurer le tableur à leur convenance.

{{% alert color="primary" %}} 

Notez que lorsque des cellules sont fusionnées, seules les données de la cellule en haut à gauche sont conservées. S'il y a des données dans les autres cellules de la plage, ces données sont supprimées. La mise en forme, de même, est basée sur la cellule de référence, de sorte que lorsque vous fusionnez des cellules, les paramètres de mise en forme de la cellule en haut à gauche de la plage sont appliqués à la cellule fusionnée. Lorsque la cellule est divisée, les nouvelles cellules conservent leurs paramètres de mise en forme d'origine.

{{% /alert %}} 
## **Fusion de cellules dans une feuille de calcul**
### **Fusionner des cellules dans Microsoft Excel**
Les étapes suivantes décrivent comment fusionner des cellules dans la feuille de calcul à l'aide de MS Excel.

1. Copiez les données que vous souhaitez dans la cellule en haut à gauche dans la plage.
1. Sélectionnez les cellules que vous souhaitez fusionner.
1. Pour fusionner des cellules dans une ligne ou une colonne et centrer le contenu de la cellule, cliquez sur l'icône **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Fusion de cellules avec Aspose.Cells**
La classe Aspose.Cells.Cells possède des méthodes utiles pour cette tâche. Par exemple, la méthode `merge()` fusionne les cellules en une seule dans une plage spécifiée.

L'exemple suivant montre comment fusionner des cellules (C6:E7) dans une feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
const wbk = new AsposeCells.Workbook();

// Create a Worksheet and get the first sheet.
const worksheet = wbk.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Merge some Cells (C6:E7) into a single C6 Cell.
cells.merge(5, 2, 2, 3);

// Input data into C6 Cell.
cells.get(5, 2).putValue("This is my value");

// Create a Style object to fetch the Style of C6 Cell.
const style = cells.get(5, 2).getStyle();

// Create a Font object
const font = style.getFont();

// Set the name.
font.setName("Times New Roman");

// Set the font size.
font.setSize(18);

// Set the font color
font.setColor(AsposeCells.Color.Blue);

// Bold the text
font.setIsBold(true);

// Make it italic
font.setIsItalic(true);

// Set the background color of C6 Cell to Red
style.setForegroundColor(AsposeCells.Color.Red);
style.setPattern(AsposeCells.BackgroundType.Solid);

// Apply the Style to C6 Cell.
cells.get(5, 2).setStyle(style);

// Save the Workbook.
wbk.save(path.join(dataDir, "mergingcells.out.xls"));
```

## **Dissocier (diviser) les cellules fusionnées**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment diviser les cellules fusionnées à l'aide de Microsoft Excel.

1. Sélectionnez la cellule fusionnée.
   Lorsque les cellules ont été combinées, **Fusionner et centrer** est sélectionné dans la barre d'outils **Mise en forme**.
1. Cliquez sur **Fusionner et centrer** dans la barre d'outils **Mise en forme**.

### **Utilisation d'Aspose.Cells**
La classe Aspose.Cells.Cells possède une méthode appelée `unmerge()` qui divise les cellules dans leur état d'origine. La méthode désfusionne les cellules en utilisant la référence de la cellule dans la plage fusionnée.

L'exemple suivant montre comment diviser les cellules fusionnées (C6). L'exemple utilise le fichier créé dans l'exemple précédent et divise les cellules fusionnées.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a Workbook.
// Open the excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "mergingcells.xls"));

// Create a Worksheet and get the first sheet.
const worksheet = workbook.getWorksheets().get(0);

// Create a Cells object to fetch all the cells.
const cells = worksheet.getCells();

// Unmerge the cells.
cells.unMerge(5, 2, 2, 3);

// Save the file.
workbook.save(path.join(dataDir, "unmergingcells.out.xls"));
```

## **Sujets avancés**
- [Détecter les cellules fusionnées dans une feuille de calcul](/cells/fr/nodejs-cpp/detect-merged-cells-in-a-worksheet/)
{{< app/cells/assistant language="nodejs-cpp" >}}
