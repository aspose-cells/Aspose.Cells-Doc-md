---
title: Insertion et suppression de lignes et colonnes dans un fichier Excel
linktitle: Insertion et suppression de lignes et de colonnes
type: docs
weight: 70
url: /fr/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Cet article montre comment insérer et supprimer des lignes et des colonnes via l API Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells Node.js via C++ gère les lignes et colonnes, insère des lignes et colonnes, supprime des lignes et colonnes
---

## **Introduction**

Que vous créiez une nouvelle feuille de calcul à partir de zéro ou travailliez sur une feuille de calcul existante, vous pouvez avoir besoin d'ajouter des lignes ou des colonnes supplémentaires pour accueillir plus de données. Inversement, vous pouvez également avoir besoin de supprimer des lignes ou des colonnes à partir de positions spécifiées dans la feuille de calcul. 
Pour répondre à ces besoins, Aspose.Cells for Node.js via C++ propose un ensemble très simple de classes et méthodes, décrites ci-dessous.

### **Gérer les lignes et les colonnes**

Aspose.Cells for Node.js via C++ fournit une classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) qui représente toutes les cellules dans la feuille.

La collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) offre plusieurs méthodes pour gérer les lignes et colonnes dans une feuille. Certaines d'entre elles sont expliquées ci-dessous.

{{% alert color="primary" %}}

Lorsque des lignes ou des colonnes sont ajoutées, le contenu de la feuille est décalé vers le bas ou vers la droite, et si des lignes ou colonnes sont supprimées, le contenu est décalé vers le haut ou vers la gauche.

{{% /alert %}}


## **Insérer des lignes et des colonnes**

### **Comment Insérer une Ligne**

Insérez une ligne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) prend l'index de la ligne où la nouvelle ligne sera insérée.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Comment Insérer Plusieurs Lignes**

Pour insérer plusieurs lignes dans une feuille de calcul, appelez la méthode [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les nouvelles lignes seront insérées.
- Nombre de lignes, le nombre total de lignes à insérer.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Comment insérer une ligne avec mise en forme**

Pour insérer une ligne avec des options de mise en forme, utilisez la surcharge [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) qui prend [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) en paramètre. Définissez la propriété [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) de la classe [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) avec l'énumération [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/). L'énumération [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) a trois membres comme indiqué ci-dessous.

- SameAsAbove: Formate la ligne de la même façon que la ligne ci-dessus.
- SameAsBelow: Formate la ligne de la même façon que la ligne ci-dessous.
- Clear: Efface la mise en forme.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Comment insérer une colonne**

Les développeurs peuvent également insérer une colonne dans la feuille de calcul à n'importe quel emplacement en appelant la méthode [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) prend l'index de la colonne où la nouvelle colonne sera insérée.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Supprimer des lignes et des colonnes**

### **Comment supprimer plusieurs lignes**

Pour supprimer plusieurs lignes d'une feuille de calcul, appelez la méthode [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) prend deux paramètres :

- Index de la ligne, l'index de la ligne à partir de laquelle les lignes seront supprimées.
- Nombre de lignes, le nombre total de lignes à supprimer.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Comment supprimer une colonne**

Pour supprimer une colonne de la feuille de calcul à n'importe quel emplacement, appelez la méthode [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La méthode [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) prend l'index de la colonne à supprimer.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
