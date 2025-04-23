---
title: Ouvrir des fichiers Microsoft Excel de versions différentes avec Node.js via C++
linktitle: Ouvrir des fichiers de différentes versions de Microsoft Excel
type: docs
weight: 20
url: /fr/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Cet article explique comment ouvrir des fichiers de différentes versions d’Excel en utilisant Aspose.Cells for Node.js via C++.
keywords: Node.js Ouvrir un fichier Microsoft Excel différent via C++, Comment ouvrir des fichiers Excel cryptés via Node.js en C++
---

{{% alert color="primary" %}}

Aspose.Cells peut ouvrir une gamme de fichiers de différentes versions de Microsoft Excel, tels que Microsoft Excel 95/97 - 2003, SpreadsheetML, ouverture de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365 XLSX ou des fichiers Excel chiffrés.

{{% /alert %}}

## **Comment ouvrir des fichiers de différentes versions de Microsoft Excel**

Une application doit souvent pouvoir ouvrir des fichiers Microsoft Excel créés dans différentes versions, par exemple Microsoft Excel 95, 97, ou Microsoft Excel 2007/2010/2013/2016/2019 et Office 365. Vous devrez peut-être charger un fichier dans l'un des plusieurs formats, y compris XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited ou TSV, CSV, ODS, etc. Utilisez le constructeur, ou spécifiez l'attribut de type [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui indique le format en utilisant l'énumération [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype).

L'énumération [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) contient plusieurs formats de fichiers prédéfinis, dont certains sont donnés ci-dessous.

|**Types de formats de fichier**|**Description**|
| :- | :- |
|Csv|Représente un fichier CSV|
|Excel97To2003|Représente un fichier Excel 97 - 2003|
|Xlsx|Représente un fichier XLSX Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsm|Représente un fichier XLSM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xltx|Représente un modèle de fichier XLTX Excel 2007/2010/2013/2016/2019 et Office 365
|Xltm|Représente un fichier activé par macro XLTM Excel 2007/2010/2013/2016/2019 et Office 365|
|Xlsb|Représente un fichier binaire XLSB Excel 2007/2010/2013/2016/2019 et Office 365|
|SpreadsheetML|Représente un fichier SpreadsheetML|
|Tsv|Représente un fichier de valeurs séparées par des tabulations|
|TabDelimited|Représente un fichier de texte à onglets|
|Ods|Représente un fichier ODS|
|Html|Représente un fichier HTML|
|Mhtml|Représente un fichier MHTML|

### **Ouvrir les fichiers Microsoft Excel 95/5.0**

Pour ouvrir un fichier Microsoft Excel 95/5.0, utilisez [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et définissez l'attribut correspondant pour la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) pour le fichier modèle à charger. Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant :

[Fichier Excel95](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Ouvrir les fichiers Microsoft Excel 97-2003**

Pour ouvrir un fichier Microsoft Excel 97 - 2003, utilisez [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et définissez l'attribut correspondant pour la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) pour le fichier modèle à charger.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Ouvrir les fichiers XLSX de Microsoft Excel 2007/2010/2013/2016/2019 et Office 365**

Pour ouvrir un format Microsoft Excel 2007/2010/2013/2016/2019 et Office 365, c'est-à-dire XLSX ou XLSB, indiquez le chemin du fichier. Vous pouvez également utiliser [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et définir l'attribut/les options pertinents de la classe [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) pour le fichier modèle à charger.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **Ouvrir des fichiers Excel chiffrés**

Il est possible de créer des fichiers Excel cryptés en utilisant Microsoft Excel. Pour ouvrir un fichier crypté, utilisez [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) et définissez ses attributs et options (par exemple, donnez un mot de passe) pour le fichier modèle à charger.
Un fichier d'exemple pour tester cette fonctionnalité peut être téléchargé à partir du lien suivant:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells prend également en charge l'ouverture de fichiers Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protégés par mot de passe.


