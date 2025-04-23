---  
title: Ajuster automatiquement la hauteur des lignes et la largeur des colonnes avec Node.js via C++  
linktitle: Ajuster automatiquement les lignes et les colonnes  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/autofit-rows-and-columns/  
description: Cet article montre comment ajuster automatiquement la hauteur des lignes, la largeur des colonnes, celles des lignes de cellules fusionnées et d’une plage de cellules en utilisant Aspose.Cells for Node.js via C++.  
keywords: Auto ajustement des lignes avec Node.js via C++, auto ajustement des colonnes avec Node.js via C++, auto ajustement d’une ligne dans une plage de cellules avec Node.js via C++, auto ajustement des lignes de cellules fusionnées avec Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel permet aux utilisateurs d’ajuster automatiquement la taille des cellules en fonction de leur contenu. Cette fonctionnalité est également disponible via Aspose.Cells for Node.js via C++, pour que les développeurs puissent ajuster automatiquement les dimensions d’une cellule en temps d'exécution.  
{{% /alert %}}  

## **Ajustement automatique**  

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) permettant d’accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Cet article présente l’utilisation de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) pour ajuster automatiquement la taille des lignes ou des colonnes.  

### **Ajuster automatiquement la ligne - Simple**  

L'approche la plus simple pour ajuster automatiquement la largeur et la hauteur d'une ligne consiste à appeler la méthode [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La méthode [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) prend un indice de ligne (de la ligne à redimensionner) en paramètre.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Comment ajuster automatiquement une ligne dans une plage de cellules**  

Une ligne est composée de plusieurs colonnes. Aspose.Cells permet aux développeurs d'automatiser le réglage de la hauteur d'une ligne en fonction du contenu dans une plage de cellules de cette ligne, en appelant une version surchargée de la méthode [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-). Elle accepte les paramètres suivants :  

- **Index de la ligne**, l'index de la ligne à ajuster automatiquement.  
- **Index de la première colonne**, l'index de la première colonne de la ligne.  
- **Index de la dernière colonne**, l'index de la dernière colonne de la ligne.  

La méthode [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) vérifie le contenu de toutes les colonnes de la ligne puis ajuste automatiquement la hauteur de la ligne.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Comment ajuster automatiquement une colonne dans une plage de cellules**  

Une colonne est composée de plusieurs lignes. Il est possible d’ajuster automatiquement une colonne en fonction du contenu d’une plage de cellules dans cette colonne en appelant une version surchargée de la méthode [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) qui prend les paramètres suivants :  

- **Index de la colonne**, l'index de la colonne à ajuster automatiquement.  
- **Index de la première ligne**, l'index de la première ligne de la colonne.  
- **Index de la dernière ligne**, l'index de la dernière ligne de la colonne.  

La méthode [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) vérifie le contenu de toutes les lignes de la colonne puis ajuste automatiquement la largeur de la colonne.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Comment ajuster automatiquement les lignes pour les cellules fusionnées**  

Avec Aspose.Cells, il est possible d’ajuster automatiquement les lignes même pour les cellules fusionnées en utilisant l’API [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions). La classe [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) fournit la propriété [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) qui peut être utilisée pour ajuster automatiquement les lignes des cellules fusionnées. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) accepte un énumérable [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) avec les membres suivants.  

- None : Ignorer les cellules fusionnées.  
- FirstLine : N'agrandit la hauteur que de la première ligne.  
- LastLine : N'agrandit la hauteur que de la dernière ligne.  
- EachLine : N'agrandit la hauteur de chaque ligne.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
Vous pouvez également essayer d’utiliser les versions surchargées des méthodes [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) & [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) acceptant une plage de lignes/colonnes et une instance de [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) pour ajuster automatiquement les lignes/colonnes sélectionnées selon votre [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) souhaité.  

Les signatures des méthodes susmentionnées sont les suivantes :  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Important à savoir**  

{{% alert color="primary" %}}  
Si une cellule est fusionnée, alors les méthodes d'auto-ajustement ne s’appliqueront pas, ce qui est le même comportement que dans Microsoft Excel. Vous pouvez contourner cela en utilisant l’API autofilter. De plus, si le texte d’une cellule est enroulé, la méthode [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) ne sera pas non plus appliquée. Une autre chose à savoir est que les méthodes *autoFit* prennent beaucoup de temps. Par conséquent, vous devriez appeler ces méthodes aussi rarement que possible pour assurer l’efficacité de votre application.  
{{% /alert %}}  

## **Sujets avancés**  
- [Ajustement automatique des lignes pour les cellules fusionnées](/cells/fr/nodejs-cpp/autofit-rows-for-merged-cells/)  

