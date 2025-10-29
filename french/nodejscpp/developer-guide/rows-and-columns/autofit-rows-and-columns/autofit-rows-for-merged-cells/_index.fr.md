---
title: Ajuster automatiquement les lignes pour les cellules fusionnées avec Node.js via C++
linktitle: Ajuster les lignes pour les cellules fusionnées
type: docs
weight: 120
url: /fr/nodejs-cpp/autofit-rows-for-merged-cells/
description: Apprenez comment ajuster automatiquement les lignes pour les cellules fusionnées en utilisant Aspose.Cells for Node.js via C++. Implémentez la fonctionnalité d ajustement automatique pour les cellules fusionnées dans les feuilles de calcul.
---

{{% alert color="primary" %}}

Microsoft Excel fournit une fonctionnalité qui vous permet de redimensionner automatiquement la hauteur d'une cellule en fonction de son contenu. La fonctionnalité s'appelle ajustement automatique des lignes. Microsoft Excel ne définit pas automatiquement l'opération d'ajustement automatique sur les cellules fusionnées nativement. Parfois, la fonctionnalité devient vitale pour un utilisateur qui doit vraiment implémenter l'ajustement automatique des lignes sur les cellules fusionnées également.

{{% /alert %}}

## **Comment utiliser AutoFitMergedCellsType pour ajuster automatiquement les lignes**
Aspose.Cells for Node.js via C++ supporte cette fonctionnalité via l'API [**AutoFitterOptions.autoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype/). En utilisant cette API, il est possible d'ajuster automatiquement les lignes d'une feuille de calcul y compris celles avec des cellules fusionnées. Voici une liste de tous les types possibles de fusion automatique des cellules:

- Aucun
- Première ligne
- Dernière ligne
- Chaque ligne

## **Ajustement automatique des lignes pour les cellules fusionnées**

Veuillez voir le code suivant, il crée un objet classeur et ajoute plusieurs feuilles de calcul. Utilisez différentes méthodes pour les opérations d'ajustement automatique dans chaque feuille de calcul. La capture d'écran montre les résultats après l'exécution du code d'exemple.

<br>
<img src="result.png" width=80% />

## **Code d'exemple Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
// Obtaining the reference of the newly added worksheet
const sheet1 = workbook.getWorksheets().get(0);

// Create a range A1:B2
const range = sheet1.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
sheet1.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = sheet1.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
sheet1.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Only expands the height of the first row.
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.FirstLine);

// Autofit rows in the sheet (including the merged cells)
sheet1.autoFitRows(options);

let index = workbook.getWorksheets().add();
const sheet2 = workbook.getWorksheets().get(index);
sheet2.setName("Sheet2");
// Create a range A1:B2
const range2 = sheet2.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range2.merge();

// Insert value to the merged cell A1
sheet2.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style2 = sheet2.getCells().get(0, 0).getStyle();

// Set wrapping text on
style2.setIsTextWrapped(true);

// Apply the style to the cell
sheet2.getCells().get(0, 0).setStyle(style2);

// Create an object for AutoFitterOptions
const options2 = new AsposeCells.AutoFitterOptions();

// Only expands the height of the last row.
options2.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.LastLine);

// Autofit rows in the sheet (including the merged cells)
sheet2.autoFitRows(options2);

index = workbook.getWorksheets().add();
const sheet3 = workbook.getWorksheets().get(index);
sheet3.setName("Sheet3");
// Create a range A1:B2
const range3 = sheet3.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range3.merge();

// Insert value to the merged cell A1
sheet3.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style3 = sheet3.getCells().get(0, 0).getStyle();

// Set wrapping text on
style3.setIsTextWrapped(true);

// Apply the style to the cell
sheet3.getCells().get(0, 0).setStyle(style3);

// Create an object for AutoFitterOptions
const options3 = new AsposeCells.AutoFitterOptions();

// Only expands the height of each row.
options3.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
sheet3.autoFitRows(options3);

index = workbook.getWorksheets().add();
const sheet4 = workbook.getWorksheets().get(index);
sheet4.setName("Sheet4");
// Create a range A1:B2
const range4 = sheet4.getCells().createRange(0, 0, 2, 2);

// Merge the cells
range4.merge();

// Insert value to the merged cell A1
sheet4.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style4 = sheet4.getCells().get(0, 0).getStyle();

// Set wrapping text on
style4.setIsTextWrapped(true);

// Apply the style to the cell
sheet4.getCells().get(0, 0).setStyle(style4);

// Create an object for AutoFitterOptions
const options4 = new AsposeCells.AutoFitterOptions();

// Ignore merged cells.
options4.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.None);

// Autofit rows in the sheet (not including the merged cells)
sheet4.autoFitRows(options4);

// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
