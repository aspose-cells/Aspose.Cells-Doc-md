---
title: Chargement et gestion des fichiers Excel, OpenOffice, Json, Csv et Html
linktitle: Ouvrir des fichiers
type: docs
weight: 20
url: /fr/nodejs-cpp/loading-saving-and-managing/
description: Avec Aspose.Cells, il est simple de créer, ouvrir et gérer des fichiers Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht et XPS en utilisant Node.js via C++.
---

{{% alert color="primary" %}}

 Avec Aspose.Cells, il est simple de créer, ouvrir et gérer des fichiers Excel, par exemple pour extraire des données ou utiliser un modèle de concepteur pour accélérer le développement.

{{% /alert %}}

## **Création d'un nouveau classeur**
L'exemple suivant crée un nouveau classeur à partir de zéro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const licensePath = path.join(dataDir, "Aspose.Cells.lic");

try {
// Create a License object
const license = new AsposeCells.License();

// Set the license of Aspose.Cells to avoid the evaluation limitations
license.setLicense(licensePath);
} catch (ex) {
console.log(ex.message);
}

// Instantiate a Workbook object that represents Excel file.
const wb = new AsposeCells.Workbook();

// When you create a new workbook, a default "Sheet1" is added to the workbook.
const sheet = wb.getWorksheets().get(0);

// Access the "A1" cell in the sheet.
const cell = sheet.getCells().get("A1");

// Input the "Hello World!" text into the "A1" cell
cell.putValue("Hello World!");

// Save the Excel file.
wb.save(path.join(dataDir, "MyBook_out.xlsx"));
```

## **Ouverture et enregistrement d'un fichier**
 Avec Aspose.Cells, il est simple d’ouvrir, d’enregistrer et de gérer des fichiers Excel.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening through Path
// Creating a Workbook object and opening an Excel file using its file path
const workbook1 = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Adding new sheet
const sheet = workbook1.getWorksheets().add("MySheet");
// Setting active sheet
workbook1.getWorksheets().setActiveSheetIndex(1);
// Setting values.
const cells = sheet.getCells();
// Setting text
cells.get("A1").putValue("Hello!");
// Setting number
cells.get("A2").putValue(1000);
// Setting Date Time
const cell = cells.get("A3");
cell.putValue(new Date());
const style = cell.getStyle();
style.setNumber(14);
cell.setStyle(style);
// Setting formula
cells.get("A4").setFormula("=SUM(A1:A3)");
// Saving the workbook to disk.
workbook1.save(path.join(dataDir, "dest.xlsx"));
```

## **Sujets avancés**
- [Différentes façons d'ouvrir des fichiers](/cells/fr/nodejs-cpp/different-ways-to-open-files/)
- [Filtrer les noms définis lors du chargement du classeur](/cells/fr/nodejs-cpp/filter-defined-names-while-loading-workbook/)
- [Filtrer les objets lors du chargement du classeur ou de la feuille de calcul](/cells/fr/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrer le type de données lors du chargement du classeur à partir du fichier modèle](/cells/fr/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtenir des avertissements lors du chargement d'un fichier Excel](/cells/fr/nodejs-cpp/get-warnings-while-loading-excel-file/)
- [Charger le fichier Excel source sans graphiques](/cells/fr/nodejs-cpp/load-source-excel-file-without-charts/)
- [Charger des feuilles de calcul spécifiques dans un classeur](/cells/fr/nodejs-cpp/load-specific-worksheets-in-a-workbook/)
- [Charger le classeur avec une taille de papier d'imprimante spécifiée](/cells/fr/nodejs-cpp/load-workbook-with-specified-printer-paper-size/)
- [Ouvrir des fichiers de différentes versions de Microsoft Excel](/cells/fr/nodejs-cpp/opening-different-microsoft-excel-versions-files/)
- [Ouvrir des fichiers avec différents formats](/cells/fr/nodejs-cpp/opening-files-with-different-formats/)
- [Optimiser l'utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données](/cells/fr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lire des feuilles de calcul numériques développées par Apple Inc. à l'aide d'Aspose.Cells](/cells/fr/nodejs-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Arrêter la conversion ou le chargement à l'aide de InterruptMonitor lorsqu'il prend trop de temps](/cells/fr/nodejs-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utiliser l'API LightCells](/cells/fr/nodejs-cpp/using-lightcells-api/)
- [Convertir CSV en JSON](/cells/fr/nodejs-cpp/convert-csv-to-json/)
- [Convertir Excel en JSON](/cells/fr/nodejs-cpp/convert-excel-to-json/)
- [Convertir JSON en CSV](/cells/fr/nodejs-cpp/convert-json-to-csv/)
- [Convertir JSON en Excel](/cells/fr/nodejs-cpp/convert-json-to-excel/)
- [Convertir Excel en Html](/cells/fr/nodejs-cpp/convert-excel-to-html/)
