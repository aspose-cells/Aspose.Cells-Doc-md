---
title: Copier et déplacer des feuilles de calcul avec Node.js via C++
linktitle: Copier et Déplacer des Feuilles de calcul
type: docs
weight: 10
url: /fr/nodejs-cpp/copying-and-moving-worksheets/
description: Cet article comprend un exemple de code et décrit comment copier et déplacer des feuilles de calcul de manière programmatique, à la fois dans un classeur Excel et entre des classeurs Excel en utilisant l API Node.js avec C++.
keywords: copier feuille Node.js, déplacer feuille Node.js
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'un certain nombre de feuilles de calcul avec une mise en forme et des données communes. Par exemple, si vous travaillez avec des budgets trimestriels, vous voudrez peut-être créer un classeur avec des feuilles contenant les mêmes en-têtes de colonne, en-têtes de ligne et formules. Il y a un moyen de le faire : en créant une feuille, puis en la copiant.

Aspose.Cells for Node.js via C++ prend en charge la copie et le déplacement de feuilles de calcul dans ou entre les classeurs. Les feuilles de calcul, complètes avec données, mise en forme, tableaux, matrices, graphiques, images et autres objets, sont copiées avec le plus grand degré de précision.

{{% /alert %}}

## **Déplacement ou Copie de feuilles à l'aide de Microsoft Excel**

Voici les étapes à suivre pour copier et déplacer des feuilles de calcul à l'intérieur ou entre des classeurs dans Microsoft Excel.

1. Pour déplacer ou copier des feuilles vers un autre classeur, ouvrez le classeur qui recevra les feuilles.
1. Basculez vers le classeur contenant les feuilles que vous souhaitez déplacer ou copier, puis sélectionnez les feuilles.
1. Dans le menu **Édition**, cliquez sur **Déplacer ou copier la feuille**.
1. Dans la boîte de dialogue **Vers le classeur**, cliquez sur le classeur qui recevra les feuilles.
1. Pour déplacer ou copier les feuilles sélectionnées vers un nouveau classeur, cliquez sur **Nouveau Classeur**.
1. Dans la zone **Avant la feuille**, cliquez sur la feuille avant laquelle vous souhaitez insérer les feuilles déplacées ou copiées.
1. Pour copier les feuilles au lieu de les déplacer, sélectionnez la case à cocher **Créer une copie**.

### **Copier des feuilles de calcul dans un classeur avec Aspose.Cells for Node.js via C++**

Aspose.Cells fournit une méthode surchargée, [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#addCopy-number-), qui est utilisée pour ajouter une feuille de calcul à la collection et copier les données à partir d'une feuille de calcul existante. Une version de la méthode prend l'index de la feuille source comme paramètre. L'autre version prend le nom de la feuille de calcul source.

L'exemple suivant montre comment copier une feuille existante dans un classeur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Open an existing Excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to
// the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Copy data to a new sheet from an existing
// sheet within the Workbook.
sheets.addCopy("Sheet1");

// Save the Excel file.
wb.save(path.join(dataDir, "CopyWithinWorkbook_out.xls"));
```

### **Copier des feuilles de calcul entre des classeurs**

Aspose.Cells fournit une méthode, [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-), utilisée pour copier les données et la mise en forme d'une feuille source vers une autre feuille dans ou entre des classeurs. La méthode prend l'objet feuille source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur à un autre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xls");

// Create a Workbook.
// Open a file into the first book.
const excelWorkbook0 = new AsposeCells.Workbook(inputPath);

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Copy the first sheet of the first book into second book.
excelWorkbook1.getWorksheets().get(0).copy(excelWorkbook0.getWorksheets().get(0));

// Save the file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetsBetweenWorkbooks_out.xls"));
```

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook.
const excelWorkbook0 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws0 = excelWorkbook0.getWorksheets().get(0);

// Put some data into header rows (A1:A4)
for (let i = 0; i < 5; i++) {
ws0.getCells().get(i, 0).putValue(`Header Row ${i}`);
}

// Put some detail data (A5:A999)
for (let i = 5; i < 1000; i++) {
ws0.getCells().get(i, 0).putValue(`Detail Row ${i}`);
}

// Define a pagesetup object based on the first worksheet.
const pagesetup = ws0.getPageSetup();

// The first five rows are repeated in each page...
// It can be seen in print preview.
pagesetup.setPrintTitleRows("$1:$5");

// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook();

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Name the worksheet.
ws1.setName("MySheet");

// Copy data from the first worksheet of the first workbook into the
// first worksheet of the second workbook.
ws1.copy(ws0);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "CopyWorksheetFromWorkbookToOther_out.xls"));
```

### **Déplacer des feuilles de calcul dans un classeur**

Aspose.Cells fournit une méthode [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#moveto-number-) qui permet de déplacer une feuille vers un autre emplacement dans la même feuille de calcul. La méthode prend l'indice de la feuille cible comme paramètre.

L'exemple suivant montre comment déplacer une feuille de calcul vers un autre emplacement dans le classeur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "sample1.xlsx");

// Open an existing excel file.
const wb = new AsposeCells.Workbook(inputPath);

// Create a Worksheets object with reference to the sheets of the Workbook.
const sheets = wb.getWorksheets();

// Get the first worksheet.
const worksheet = sheets.get(0);

// Move the first sheet to the third position in the workbook.
worksheet.moveTo(2);

// Save the excel file.
wb.save(path.join(dataDir, "MoveWorksheet_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
