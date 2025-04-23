---
title: Convertir JSON en Excel avec Node.js via C++
linktitle: Convertir JSON en Excel
type: docs
weight: 300
url: /fr/nodejs-cpp/convert-json-to-excel/
description: Apprenez comment convertir JSON en fichier Excel avec Aspose.Cells for Node.js via C++.
keywords: Importation JSON sans Office 2013, Office 2016, Office 2019, ni Office 365 en utilisant Node.js via C++.
---

{{% alert color="primary" %}}

 Aspose.Cells supporte la conversion d’un fichier JSON (JavaScript Object Notation) en classeur Excel.

{{% /alert %}}

## **Convertir JSON en classeur Excel**
 Pas besoin de se demander comment convertir JSON en fichier Excel, car Aspose.Cells for Node.js via C++ offre la meilleure solution. L’API Aspose.Cells prend en charge la conversion du format JSON en feuilles de calcul. Vous pouvez utiliser la classe [**JsonLoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonloadoptions) pour spécifier des paramètres supplémentaires lors de l’importation JSON dans le classeur.

L'exemple de code suivant démontre l'importation du JSON dans le Classeur Excel. Veuillez consulter le code pour convertir le [fichier source](sample.json) en fichier xlsx généré par le code à titre de référence.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");
// create a Workbook object
const wb = new AsposeCells.Workbook(filePath);

// save file to xlsx format
wb.save("sample_out.xlsx");
```

L’exemple de code suivant, utilisant la classe JsonLoadOptions pour spécifier des paramètres supplémentaires, montre comment importer JSON dans un classeur Excel. Veuillez consulter le code pour convertir le [fichier source](sample.json) en fichier xlsx généré par le code à titre de référence.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.json");

// Create an options of loading the file.
const options = new AsposeCells.JsonLoadOptions();
options.setMultipleWorksheets(true);

// Loads the workbook from JSON file
const book = new AsposeCells.Workbook(filePath, options);

// Save file to xlsx format
book.save("sample_out.xlsx");
```

 L’exemple de code suivant montre comment importer une chaîne JSON dans un classeur Excel. Vous pouvez également spécifier l’emplacement de la mise en page lors de l’importation du JSON. Veuillez consulter le code pour convertir une chaîne JSON en fichier xlsx généré par le code à titre de référence.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputJson = JSON.stringify([
{ BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
{ BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
]);
const sheetName = "Sheet1";
const row = 3;
const column = 2;

// create a Workbook object
const book = new AsposeCells.Workbook();
const worksheet = book.getWorksheets().get(sheetName);

// set JsonLayoutOptions to treat Arrays as Table
const jsonLayoutOptions = new AsposeCells.JsonLayoutOptions();
jsonLayoutOptions.setArrayAsTable(true);

AsposeCells.JsonUtility.importData(inputJson, worksheet.getCells(), row, column, jsonLayoutOptions);

// save file to xlsx format
book.save("out.xlsx");
```
