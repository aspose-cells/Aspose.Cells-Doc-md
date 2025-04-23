---  
title: Gérer les feuilles de calcul des fichiers Microsoft Excel avec Node.js via C++  
linktitle: Feuilles de calcul  
type: docs  
weight: 90  
url: /fr/nodejs-cpp/manage-worksheets/  
description: Ajouter, retirer et activer des feuilles de calcul en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Les développeurs peuvent facilement créer et gérer des feuilles de calcul dans les fichiers Microsoft Excel de manière programmatique en utilisant l'API flexible d'Aspose.Cells. Ce sujet décrit les approches pour ajouter et supprimer des feuilles de calcul dans les fichiers Microsoft Excel.  
{{% /alert %}}  

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.  

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles.  

## **Ajout de feuilles de calcul à un nouveau fichier Excel**  

Pour créer un nouveau fichier Excel de manière programmatique:  

1. Créez un objet de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  
1. Appelez la méthode [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Une nouvelle feuille de calcul vide est ajoutée au fichier Excel automatiquement. Elle peut être référencée en passant l'indice de la feuille à la collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--).  
1. Obtenez une référence de feuille de calcul.  
1. Travaillez sur les feuilles de calcul.  
1. Enregistrez le nouveau fichier Excel avec ses nouvelles feuilles en appelant la méthode [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Ajout de feuilles de calcul à une feuille de calcul Designer**  

Le processus d'ajout de feuilles dans un classeur de conception est le même que celui d'ajouter une nouvelle feuille, sauf que le fichier Excel existe déjà et doit être ouvert avant d'ajouter des feuilles. Un fichier de conception peut être ouvert par la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook).  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Accéder aux feuilles de calcul en utilisant le nom de la feuille**  

Accédez à n'importe quelle feuille de calcul en spécifiant son nom ou son index.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Suppression des feuilles de calcul en utilisant le nom de la feuille**  

Pour supprimer des feuilles d'un fichier, appelez la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) de la classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection). Passez le nom de la feuille à la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) pour supprimer une feuille spécifique.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Suppression des feuilles de calcul en utilisant l'indice de la feuille**  

Supprimer des feuilles par nom fonctionne bien lorsque le nom de la feuille est connu. Si vous ne connaissez pas le nom de la feuille, utilisez une version surchargée de la méthode [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) qui prend l’indice de la feuille de calcul plutôt que son nom.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Activation des feuilles et mise en place d'une cellule active dans la feuille de calcul**  

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsque l'utilisateur ouvre un fichier Microsoft Excel dans Excel. De même, vous pourriez vouloir activer une cellule spécifique et régler les barres de défilement pour montrer cette cellule active. Aspose.Cells est capable d'effectuer toutes ces tâches.  

Une **feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.  

Une **cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.  

### **Activation des feuilles et mise en avant d'une cellule**  

Aspose.Cells fournit des appels API spécifiques pour activer une feuille et une cellule. Par exemple, la propriété [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) est utile pour définir la feuille active dans un classeur. De même, la propriété [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) est utilisée pour définir et obtenir une cellule active dans la feuille de calcul.  

Pour vous assurer que les barres de défilement horizontales ou verticales soient à la position d'index de ligne et de colonne que vous souhaitez pour afficher des données spécifiques, utilisez les propriétés [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) et [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--).  

L'exemple suivant montre comment activer une feuille de calcul et mettre en avant une cellule active. Dans la sortie générée, les barres de défilement seront scrollées pour que la 2ème ligne et la 2ème colonne soient leur première ligne et colonne visibles.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Sujets avancés**  
- [Copier et Déplacer des Feuilles de calcul](/cells/fr/nodejs-cpp/copying-and-moving-worksheets/)  
- [Compter le nombre de cellules dans la feuille de calcul](/cells/fr/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Détection des Feuilles de calcul vides](/cells/fr/nodejs-cpp/detecting-empty-worksheets/)  
- [Trouver si la Feuille de calcul est une Feuille de dialogue](/cells/fr/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Obtenir l'identifiant unique de la feuille de calcul](/cells/fr/nodejs-cpp/get-worksheet-unique-id/)  
- [Créer, Manipuler ou Supprimer des Scénarios des Feuilles de calcul](/cells/fr/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Gestion des Sauts de Page](/cells/fr/nodejs-cpp/managing-page-breaks/)  
- [Fonctionnalités de Configuration de Page](/cells/fr/nodejs-cpp/page-setup-features/)   
- [Utiliser la propriété Sheet.SheetId d'OpenXml en utilisant Aspose.Cells](/cells/fr/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Vues de Feuille de calcul](/cells/fr/nodejs-cpp/worksheet-views/)  


