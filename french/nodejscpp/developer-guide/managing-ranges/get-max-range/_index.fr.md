---  
title: Obtenir la plage maximale dans une feuille de calcul avec Node.js via C++  
linktitle: Obtenir la plage maximale dans une feuille de calcul  
type: docs  
weight: 360  
url: /fr/nodejs-cpp/get-max-range-in-a-worksheet/  
description: Cet article décrit comment obtenir la plage maximale, la plage de données maximale, et la plage d affichage maximale des fichiers Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.  

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.  

Lors de l'exportation d'une zone spécifiée en HTML et PDF, nous devons connaître la zone maximale.  

Aspose.Cells for Node.js via C++ propose différentes méthodes pour trouver la plage maximale dans une feuille de calcul.  

{{% /alert %}}  

## **Obtenir la plage maximale**  
Dans Aspose.Cells, si les objets [**row**](https://reference.aspose.com/cells/nodejs-cpp/row/) et [**column**](https://reference.aspose.com/cells/nodejs-cpp/column/) sont initialisés, ces lignes et colonnes seront comptabilisées jusqu'à la zone maximale, même s'il n'y a aucune donnée dans les lignes ou colonnes vides.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Obtenir la plage de données maximale**  
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.  
Et les paramètre concernant les formes, les tableaux et les tableaux croisés dynamiques seront ignorés.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **Obtenir la plage d'affichage maximale**  
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.  
Les codes suivants montrent comment rendre la plage d'affichage maximale en HTML :  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

Voici le [fichier excel source](Book1.xlsx).  

{{< app/cells/assistant language="nodejs-cpp" >}}
