---  
title: Convertir CSV, TSV et TXT en Excel avec Node.js via C++  
linktitle: Convertir CSV, TSV et TXT en Excel  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/  
---  

{{% alert color="primary" %}}  
En utilisant Aspose.Cells, vous pouvez convertir des fichiers CSV en Excel, OpenOffice, PDF, JSON, et bien d’autres formats.  
{{% /alert %}}  

## **Ouverture des fichiers CSV**  

Les fichiers au format Valeurs Séparées par des Virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et est encadrée par le caractère double quote. Si une valeur de champ contient un caractère de guillemet double, il est échappé avec une paire de caractères de guillemet double. Vous pouvez également utiliser Microsoft Excel pour exporter des données de feuille de calcul vers un fichier CSV.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);
// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(path.join(dataDir, "Book_CSV.csv"), loadOptions4);
console.log("CSV file opened successfully!");
```  

## **Ouverture des fichiers CSV et remplacement des caractères invalides**  

Dans Excel, lorsqu’un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par l’API Aspose.Cells, comme le montre l’exemple de code ci-dessous.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const options = new AsposeCells.TxtLoadOptions();
options.setSeparator(",");
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
options.setCheckExcelRestriction(false);
options.setConvertNumericData(false);
options.setConvertDateTimeData(false);
// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, options);

console.log(workbook.getWorksheets().get(0).getName()); // (20180220142533)(ASPOSE_CELLS_T
console.log(workbook.getWorksheets().get(0).getName().length); // 31
console.log("CSV file opened successfully!");
```  


### **Ouverture de fichiers texte avec un séparateur personnalisé**  

Les fichiers texte sont utilisés pour stocker des données de feuille de calcul sans mise en forme. Le fichier est une sorte de fichier texte brut qui peut avoir des délimiteurs personnalisés.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book11.csv");

// Instantiate Text File's LoadOptions
const txtLoadOptions = new AsposeCells.TxtLoadOptions();

// Specify the separator
txtLoadOptions.setSeparator(",");

// Specify the encoding type
txtLoadOptions.setEncoding(AsposeCells.EncodingType.UTF8);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, txtLoadOptions);

// Save file
wb.save(path.join(dataDir, "output.txt"));
```  

### **Ouverture des fichiers à valeurs séparées par des tabulations**  

Les fichiers délimités par des tabulations (Text) contiennent des données de feuille de calcul mais sans aucune mise en forme. Les données sont organisées en lignes et colonnes comme dans des tableaux et feuilles de calcul. En gros, un fichier délimité par une tabulation est un type particulier de fichier texte simple avec une tabulation entre chaque colonne.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Tab Delimited Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(path.join(dataDir, "Book1TabDelimited.txt"), loadOptions5);
console.log("Tab delimited file opened successfully!");
```  

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**  

Les fichiers de valeurs séparées par des tabulations (TSV) contiennent des données de feuilles de calcul mais sans mise en forme. C’est la même chose qu’un fichier délimité par des tabulations où les données sont disposées en lignes et en colonnes comme dans des tableaux et des feuilles de calcul.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Tsv);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTSVFile.tsv"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log("Cell Name: " + cell.getName() + " Value: " + cell.getStringValue());
```  

## **Sujets avancés**  
- [Charger ou importer un fichier CSV avec des formules](/cells/fr/nodejs-cpp/load-or-import-csv-file-with-formulas/)  
- [Lecture d'un fichier CSV avec des encodages multiples](/cells/fr/nodejs-cpp/reading-csv-file-with-multiple-encodings/)  


