---  
title: Mettre en forme les lignes et colonnes avec Node.js via C++  
linktitle: Lignes et colonnes  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++ peut supporter le changement de la hauteur des lignes ou de la largeur des colonnes, ainsi que l application de formats sur des lignes ou des colonnes.  
keywords: Définir la hauteur de ligne et la largeur de colonne, ajuster la hauteur de ligne et la largeur de colonne, changer la hauteur de ligne ou la largeur de colonne, formater les lignes et les colonnes, comment définir la hauteur de ligne et la largeur de colonne.  
---  

{{% alert color="primary" %}}  
Lors de la manipulation de feuilles de calcul et de l'ajout de données dans des lignes ou colonnes, il peut être nécessaire de modifier la hauteur des lignes ou la largeur des colonnes. Parfois, appliquer un format sur des lignes ou colonnes implique que la hauteur ou la largeur actuelles doivent changer pour afficher les données. En général, les utilisateurs ajustent la hauteur des lignes et la largeur des colonnes dans un environnement WYSIWYG en utilisant Microsoft Excel. Mais, avec Aspose.Cells, les développeurs peuvent effectuer ces opérations à l'exécution.  
{{% /alert %}}  

## **Travailler avec des lignes**  

### **Comment ajuster la hauteur de ligne**  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) qui représente toutes les cellules de la feuille.  

La collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) offre plusieurs méthodes pour gérer les lignes ou colonnes dans une feuille. Certaines de ces méthodes sont décrites ci-dessous plus en détail.  

### **Comment définir la hauteur d'une ligne**  

Il est possible de définir la hauteur d'une seule ligne en appelant la méthode [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). La méthode [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) prend les paramètres suivants :

- **Index de ligne**, l'index de la ligne pour laquelle vous modifiez la hauteur.  
- **Hauteur de la ligne**, la hauteur de la ligne à appliquer sur la ligne.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Comment définir la hauteur de toutes les lignes dans une feuille de calcul**  

Si les développeurs ont besoin de définir la même hauteur de ligne pour toutes les lignes de la feuille, ils peuvent utiliser la propriété [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

**Exemple :**  

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

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Travailler avec les colonnes**  

### **Comment définir la largeur d'une colonne**  

Définissez la largeur d'une colonne en appelant la méthode [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). La méthode [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) prend les paramètres suivants :  

- Index de la colonne, l'index de la colonne dont vous changez la largeur.  
- Largeur de colonne, la largeur de colonne souhaitée.  

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

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Comment définir la largeur de colonne en pixels**  

Définissez la largeur d'une colonne en appelant la méthode [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). La méthode [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) prend les paramètres suivants :  

- Index de la colonne, l'index de la colonne dont vous changez la largeur.  
- Largeur de colonne, la largeur de colonne souhaitée en pixels.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Comment définir la largeur de toutes les colonnes dans une feuille de calcul**  

Pour définir la même largeur de colonne pour toutes les colonnes dans la feuille de calcul, utilisez la propriété [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells).  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Sujets avancés**  
- [Ajuster automatiquement les lignes et les colonnes](/cells/fr/nodejs-cpp/autofit-rows-and-columns/)  
- [Convertir du texte en colonnes à l'aide de Aspose.Cells](/cells/fr/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Copier des lignes et des colonnes](/cells/fr/nodejs-cpp/copying-rows-and-columns/)  
- [Supprimer les lignes et les colonnes vides dans une feuille de calcul](/cells/fr/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Regrouper et dégrouper les lignes et les colonnes](/cells/fr/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Masquer et afficher des lignes et des colonnes](/cells/fr/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Insérer ou supprimer des lignes dans une feuille de calcul Excel](/cells/fr/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Insérer et supprimer des lignes et des colonnes d'un fichier Excel](/cells/fr/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Supprimer les lignes en double dans une feuille de calcul](/cells/fr/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul](/cells/fr/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
