---  
title: Afficher et masquer les feuilles de calcul et onglets avec Node.js via C++  
linktitle: Afficher et masquer des feuilles de calcul et des onglets  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Cet article fournit un exemple de code pour utiliser l API Node.js ou la bibliothèque Node.js afin d afficher et de masquer de manière programmatique une feuille Excel. De plus, comment afficher et masquer les onglets du classeur Excel.  
---  

{{% alert color="primary" %}}  
Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris des feuilles de calcul et des onglets.  
{{% /alert %}}  

## **Afficher et masquer une feuille de calcul**  

Un fichier Excel peut avoir une ou plusieurs feuilles de calcul. Lorsque nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Donc, **Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.  

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui donne accès à chaque feuille de calcul du fichier Excel.  

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre un large éventail de propriétés et de méthodes pour gérer les feuilles. Pour contrôler la visibilité d'une feuille, utilisez la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.  

### **Rendre une feuille de calcul visible**  

Rendez une feuille visible en définissant la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) à **true**.  

### **Masquer une feuille de calcul**  

Masquez une feuille en définissant la propriété [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) à **false**.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Afficher et masquer les onglets**  

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:  

- Onglets de feuille.  
- Boutons de défilement d'onglets.  

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.  

En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement dans les fichiers Excel.  

Aspose.Cells offre une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser la propriété [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook). [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) est une propriété Boolean, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.  

### **Rendre les onglets visibles**  

Rendez les onglets visibles avec la propriété [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) à **true**.  

### **Masquage des onglets**  

Masquez les onglets dans un fichier Excel en définissant la propriété [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) de la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) à **false**.  

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Contrôler la largeur de la barre d'onglets**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
