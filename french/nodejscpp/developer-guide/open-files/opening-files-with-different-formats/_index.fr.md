---
title: Ouverture de fichiers avec différents formats via Node.js en C++
linktitle: Ouverture de fichiers avec différents formats
type: docs
weight: 30
url: /fr/nodejs-cpp/opening-files-with-different-formats/
description: L API Aspose.Cells for Node.js via C++ permet d ouvrir/lire différents formats comme XLSX, HTML, CSV, ODS, TSV, SXC, FODS, etc.
keywords: ouvrir des fichiers xlsx, ouvrir des fichiers html, lire des fichiers fods, lire des fichiers ods, lire des fichiers sxc, ouvrir des fichiers csv, valeurs tabulées, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Avec Aspose.Cells, vous pouvez ouvrir des fichiers avec différents formats. **Aspose.Cells** peut ouvrir une gamme de formats de fichiers tels que les feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valeurs séparées par des virgules (CSV), fichiers séparés par des tabulations ou valeurs séparées par des tabulations (TSV), etc.

Si vous avez besoin de connaître tous les formats de fichier pris en charge, veuillez vous référer aux pages suivantes:
[Formats de fichiers pris en charge](https://docs.aspose.com/cells/nodejs-cpp/supported-file-formats/)

{{% /alert %}}

## **Ouvrir des fichiers avec différents formats**

Aspose.Cells permet aux développeurs d'ouvrir des fichiers de feuille de calcul avec différents formats tels que SpreadsheetML, valeurs séparées par des virgules (CSV), valeurs séparées par des tabulations (TSV), fichiers ODS. Pour ouvrir de tels fichiers, les développeurs peuvent utiliser la même méthodologie que celle utilisée pour ouvrir des fichiers de différentes versions de Microsoft Excel.

### **Ouverture de fichiers SpreadsheetML**

Les fichiers SpreadsheetML sont des représentations XML de feuilles de calcul comprenant toutes les informations à leur sujet, telles que la mise en forme, les formules, etc. Depuis Microsoft Excel XP, une option d’export XML a été ajoutée à Microsoft Excel qui exporte vos feuilles de calcul vers des fichiers SpreadsheetML.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening SpreadsheetML Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions3 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.SpreadsheetML);

// Create a Workbook object and opening the file from its path
const wbSpreadSheetML = new AsposeCells.Workbook(path.join(dataDir, "Book3.xml"), loadOptions3);
console.log("SpreadSheetML file opened successfully!");
```

### **Ouverture de fichiers HTML**

Aspose.Cells permet d'ouvrir un fichier HTML dans un objet Workbook. Le fichier HTML doit être orienté Microsoft Excel, c’est-à-dire que MS-Excel doit pouvoir l’ouvrir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.html");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath, loadOptions);

// Save the MHT file
wb.save(`${filePath}output.xlsx`);
```

### **Ouverture des fichiers CSV**

Les fichiers valeurs séparées par des virgules (CSV) contiennent des enregistrements où les valeurs sont séparées par des virgules. Les données sont stockées sous forme de tableau où chaque colonne est séparée par le caractère virgule et entourée de guillemets doubles. Si une valeur de champ contient un caractère de guillemet double, elle est échappée avec une paire de guillemets doubles. Vous pouvez également utiliser Microsoft Excel pour exporter les données de feuilles de calcul en CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_CSV.csv");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions4 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Csv);

// Create a Workbook object and opening the file from its path
const wbCSV = new AsposeCells.Workbook(filePath, loadOptions4);
console.log("CSV file opened successfully!");
```

#### **Ouverture des fichiers CSV et remplacement des caractères invalides**

Dans Excel, lorsqu’un fichier CSV avec des caractères spéciaux est ouvert, les caractères sont automatiquement remplacés. La même chose est faite par l’API Aspose.Cells, comme le montre l’exemple de code ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "[20180220142533][ASPOSE_CELLS_TEST].csv");

const loadOptions = new AsposeCells.TxtLoadOptions();
loadOptions.setSeparator(';');
loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.CellData));
loadOptions.setCheckExcelRestriction(false);
loadOptions.setConvertNumericData(false);
loadOptions.setConvertDateTimeData(false);

// Load CSV file
const workbook = new AsposeCells.Workbook(filePath, loadOptions);


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
const filePath = path.join(dataDir, "Book1TabDelimited.txt");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions5 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.TabDelimited);

// Create a Workbook object and opening the file from its path
const wbTabDelimited = new AsposeCells.Workbook(filePath, loadOptions5);
console.log("Tab delimited file opened successfully!");
```

### **Ouverture des fichiers à valeurs séparées par des tabulations (TSV)**

Le fichier de valeurs séparées par des tabulations (TSV) contient des données de feuille de calcul mais sans mise en forme. C’est la même chose qu’un fichier délimité par des tabulations, où les données sont organisées en lignes et colonnes comme dans des tableaux et feuilles de calcul.

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

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Ouverture de fichiers SXC**

StarOffice Calc est similaire à Microsoft Excel et supporte les formules, graphiques, fonctions et macros. Les feuilles de calcul créées avec ce logiciel sont enregistrées avec l’extension SXC. Le fichier SXC est aussi utilisé pour les fichiers de feuilles de calcul OpenOffice.org Calc. Aspose.Cells peut lire les fichiers SXC comme démontré dans l’extrait de code suivant.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Sxc);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleSXC.sxc"), loadOptions);

// Using the Sheet 1 in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Accessing a cell using its name
const cell = worksheet.getCells().get("C3");

console.log(`Cell Name: ${cell.getName()} Value: ${cell.getStringValue()}`);
```

### **Ouverture de fichiers FODS**

Le fichier FODS est une feuille de calcul enregistrée en XML du OpenDocument sans compression. Aspose.Cells peut lire les fichiers FODS, comme illustré dans l’exemple de code ci-dessous.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Fods);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleFods.fods"), loadOptions);

console.log("FODS file opened successfully!");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
