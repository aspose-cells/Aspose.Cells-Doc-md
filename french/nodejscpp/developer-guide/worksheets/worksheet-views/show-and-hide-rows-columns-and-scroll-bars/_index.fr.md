---  
title: Afficher et masquer les lignes, colonnes et barres de défilement avec Node.js via C++  
linktitle: Afficher et masquer les lignes, colonnes et barres de défilement  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Cet article démontre comment afficher et masquer de manière programmatique les lignes et colonnes d une feuille Excel en utilisant Node.js via C++. Contrôlez la visibilité des barres de défilement et masquez efficacement plusieurs lignes et colonnes.  
---  

{{% alert color="primary" %}}  
Aspose.Cells offre des moyens de contrôler la visibilité des lignes, des colonnes et des barres de défilement d'une feuille de calcul.  
{{% /alert %}}  

## **Afficher et masquer les lignes et les colonnes**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet aux développeurs d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) qui représente toutes les cellules de la feuille de calcul. La collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) fournit plusieurs méthodes pour gérer les lignes ou colonnes d'une feuille. Quelques-unes de celles-ci sont abordées ci-dessous.  

### **Afficher les lignes et les colonnes**  

Les développeurs peuvent afficher toute ligne ou colonne cachée en appelant respectivement les méthodes [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) et [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ces deux méthodes prennent deux paramètres :  

- **Index de la ligne ou de la colonne** - l'index d'une ligne ou colonne utilisé pour afficher la ligne ou colonne spécifique.  
- **Hauteur de la ligne ou largeur de la colonne** - la hauteur de la ligne ou la largeur de la colonne assignée à la ligne ou colonne après démasquage.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
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
Lorsqu'une colonne cachée est rendue visible, si vous devez la restaurer à la largeur précédemment attribuée ou à sa largeur d'origine, veuillez démasquer la colonne avec une largeur négative. Par exemple : worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Masquer les lignes et les colonnes**  

Les développeurs peuvent masquer une ligne ou une colonne en appelant respectivement les méthodes [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) et [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ces deux méthodes prennent en paramètre l'indice de la ligne ou de la colonne pour masquer la ligne ou colonne spécifique.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
Il est également possible de masquer une ligne ou une colonne en définissant respectivement la hauteur de la ligne ou la largeur de la colonne à 0.  
{{% /alert %}}  

### **Masquer plusieurs lignes et colonnes**  

Les développeurs peuvent masquer plusieurs lignes ou colonnes simultanément en appelant respectivement les méthodes [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) et [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) de la collection [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ces deux méthodes prennent en paramètres l'indice de la ligne ou de la colonne de début et le nombre de lignes ou colonnes à masquer.  

```javascript
const fs = require('fs');
const path = require("path");
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Afficher et masquer les barres de défilement**  

Les barres de défilement sont utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :  

- Barres de défilement verticales  
- Barres de défilement horizontales  

Microsoft Excel propose également des barres de défilement horizontales et verticales permettant aux utilisateurs de naviguer dans le contenu de la feuille de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.  

### **Contrôler la visibilité des barres de défilement**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) offre une large gamme de propriétés et méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez les propriétés [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) et [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) et [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) sont des propriétés booléennes, ce qui signifie qu'elles ne peuvent contenir que des valeurs **true** ou **false**.  

#### **Rendre les barres de défilement visibles**  

Rendez les barres de défilement visibles en définissant la propriété [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) ou [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) à **true**.  

#### **Masquer les barres de défilement**  

Masquez les barres de défilement en définissant la propriété [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) ou [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) à **false**.  

**Code d'exemple**  

Ci-dessous se trouve un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom de output.xls.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

