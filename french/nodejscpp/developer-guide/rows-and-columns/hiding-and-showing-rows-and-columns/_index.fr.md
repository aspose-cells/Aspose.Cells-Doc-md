---
title: Masquer et afficher des lignes et colonnes avec Node.js via C++
linktitle: Masquer et afficher des lignes et des colonnes
type: docs
weight: 60
url: /fr/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Apprenez comment masquer et afficher des lignes et colonnes dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Parfois, il est judicieux de masquer certaines lignes ou colonnes dans une feuille de calcul et de les afficher plus tard. Microsoft Excel fournit cette fonctionnalité et Aspose.Cells également.

{{% /alert %}}

## **Contrôler la visibilité des lignes et des colonnes**

Aspose.Cells for Node.js via C++ offre une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) qui permet aux développeurs d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) qui représente toutes les cellules de la feuille. La collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille. Quelques-unes de ces méthodes sont expliquées ci-dessous.

### **Masquer les lignes et les colonnes**

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) et [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ces deux méthodes prennent en paramètre l'indice de la ligne ou de la colonne pour masquer la ligne ou colonne spécifique.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.

{{% /alert %}}

### **Afficher des lignes et des colonnes**

Les développeurs peuvent afficher toute ligne ou colonne cachée en appelant respectivement les méthodes [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) et [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ces deux méthodes prennent deux paramètres :

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

Lors de la rendre visible une colonne cachée, si vous devez la remettre à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez découvrir la colonne avec une largeur négative. Par exemple : worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Masquer plusieurs lignes et colonnes**

Les développeurs peuvent masquer plusieurs lignes ou colonnes simultanément en appelant respectivement les méthodes [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) et [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Ces deux méthodes prennent en paramètres l'indice de la ligne ou de la colonne de début et le nombre de lignes ou colonnes à masquer.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

Il est également possible d'utiliser les méthodes [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) et [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) de la classe [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) pour rendre plusieurs lignes et colonnes visibles.

{{% /alert %}}
