---  
title: Copier des lignes et des colonnes avec Node.js via C++  
linktitle: Copier des lignes et des colonnes  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/copying-rows-and-columns/  
description: Cet article montre comment copier des lignes et des colonnes à travers l’API Aspose.Cells for Node.js via C++.  
keywords: Node.js via C++, comment copier des lignes et des colonnes, copier des lignes dans Node.js, copier des colonnes avec Node.js, comment coller des lignes et des colonnes en utilisant Aspose.Cells for Node.js via C++, coller plusieurs lignes et colonnes, comment copier et coller une seule ligne ou colonne.  
---  

## **Introduction**  

Parfois, vous devez copier des lignes et des colonnes dans une feuille de calcul sans copier toute la feuille de calcul. Avec Aspose.Cells, il est possible de copier des lignes et des colonnes à l'intérieur ou entre les classeurs.  
Lorsqu'une ligne (ou une colonne) est copiée, les données qu'elle contient, y compris les formules - avec des références mises à jour - et les valeurs, les commentaires, la mise en forme, les cellules masquées, les images et autres objets graphiques sont également copiés.  

## **Comment copier des lignes et des colonnes avec Microsoft Excel**  

1. Sélectionnez la ligne ou la colonne que vous souhaitez copier.  
1. Pour copier des lignes ou des colonnes, cliquez sur **Copier** dans la barre d'outils **Standard**, ou appuyez sur **CTRL**+**C**.  
1. Sélectionnez une ligne ou une colonne en dessous ou à droite de l'endroit où vous souhaitez copier votre sélection.  
1. Lorsque vous copiez des lignes ou des colonnes, cliquez sur **Cellules copiées** dans le menu **Insérer**.  

{{% alert color="primary" %}}  
Si vous cliquez sur **Coller** dans la barre d'outils **Standard** ou appuyez sur **CTRL**+**V** au lieu de cliquer sur une commande dans le menu **Insérer**, tout contenu des cellules de destination est remplacé.  
{{% /alert %}}  

## **Comment coller des lignes et des colonnes en utilisant les options de collage avec Microsoft Excel**  

1. Sélectionnez les cellules contenant les données ou autres attributs que vous souhaitez copier.  
1. Sur l'onglet Accueil, cliquez sur **Copier**.  
1. Cliquez sur la première cellule dans la zone où vous souhaitez **coller** ce que vous avez copié.  
1. Sur l'onglet Accueil, cliquez sur la flèche à côté de **Coller**, puis sélectionnez **Collage** spécial.  
1. Sélectionnez les **options** que vous souhaitez.  

## **Comment copier des lignes et des colonnes en utilisant Aspose.Cells for Node.js via C++**  

## **Comment copier des lignes uniques**  

Aspose.Cells fournit la méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Cette méthode copie tous types de données, y compris formules, valeurs, commentaires, formats de cellules, cellules cachées, images et autres objets de dessin de la ligne source vers la ligne de destination.  

La méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) prend les paramètres suivants :  

- l’objet [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) source,  
- l'indice de ligne source, et  
- l'indice de ligne de destination.  

Utilisez cette méthode pour copier une ligne au sein d’une feuille ou vers une autre feuille. La méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) fonctionne de manière similaire à Microsoft Excel. Par exemple, vous n'avez pas besoin de définir explicitement la hauteur de la ligne de destination, cette valeur est également copiée.  

L'exemple suivant montre comment copier une ligne dans une feuille de calcul. Il utilise un fichier Excel Microsoft de modèle et copie la deuxième ligne (avec ses données, son formatage, ses commentaires, ses images, etc.) et la colle à la 12e ligne de la même feuille.  

Vous pouvez sauter l’étape consistant à obtenir la hauteur de la ligne source en utilisant la méthode [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) puis définir la hauteur de la ligne de destination avec la méthode [**Cells.setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-), car la méthode [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) s’occupe automatiquement de la hauteur de la ligne.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Lors de la copie de lignes, il est important de noter les images, les graphiques ou autres objets de dessin associés, car c'est la même chose avec Microsoft Excel :  

1. Si l'indice de la ligne source est 5, l'image, le graphique, etc., est copié s'il est contenu dans les trois lignes (l'indice de début de la ligne est 4 et l'indice de fin de la ligne est 6).  
1. Les images existantes, les graphiques, etc. dans la ligne de destination ne seront pas supprimés.  
{{% /alert %}}  

## **Comment copier plusieurs lignes**  

Vous pouvez également copier plusieurs lignes vers une nouvelle destination en utilisant la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) qui prend un paramètre supplémentaire de type entier pour préciser le nombre de lignes sources à copier.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Comment copier des colonnes**  

Aspose.Cells fournit la méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), cette méthode copie tous types de données, y compris les formules - avec références mises à jour - et les valeurs, commentaires, formats de cellules, cellules cachées, images et autres objets de dessin de la colonne source vers la colonne de destination.  

La méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) prend les paramètres suivants :  

- l’objet [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) source,  
- indice de la colonne source, et  
- indice de la colonne de destination.  

Utilisez la méthode [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) pour copier une colonne au sein d’une feuille ou vers une autre feuille.  

Cet exemple copie une colonne d'une feuille de calcul et la colle dans une feuille de calcul d'un autre classeur.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Comment copier plusieurs colonnes**  

Semblable à la méthode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-), les API Aspose.Cells proposent également la méthode [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) afin de copier plusieurs colonnes source vers un nouvel emplacement.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Comment coller des lignes et des colonnes avec des options de collage**  

Aspose.Cells fournit maintenant [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) tout en utilisant les fonctions [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) et [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-). Il permet de définir une option de collage appropriée similaire à Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


