---  
title: Travail avec l’arrière plan dans les fichiers ODS avec Node.js via C++  
linktitle: Travailler avec l arrière plan dans les fichiers ODS  
type: docs  
weight: 150  
url: /fr/nodejs-cpp/working-with-background-in-ods-files/  
description: Apprenez comment gérer les arrière plans dans les fichiers ODS en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Arrière-plan dans les fichiers ODS**  

Un arrière-plan peut être ajouté aux feuilles dans les fichiers ODS. L'arrière-plan peut être soit un arrière-plan coloré, soit un arrière-plan graphique. L'arrière-plan n'est pas visible lorsque le fichier est ouvert, mais s'il est imprimé en PDF, l'arrière-plan est visible dans le PDF généré. L'arrière-plan est également visible dans la boîte de dialogue d'aperçu avant impression.  

Aspose.Cells for Node.js via C++ offre la capacité de lire les informations d’arrière-plan et d’ajouter l’arrière-plan dans les fichiers ODS.  

## **Lire les informations d'arrière-plan à partir du fichier ODS**  

Aspose.Cells for Node.js via C++ fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) pour gérer l’arrière-plan dans les fichiers ODS. Le code suivant montre comment utiliser la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) en chargeant le fichier [source ODS](90112030.ods) et en lisant les informations d’arrière-plan. Veuillez voir la sortie console générée par le code à titre de référence.  

### **Code d'exemple**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **Sortie console**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Ajouter un arrière-plan coloré au fichier ODS**  

Aspose.Cells for Node.js via C++ fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) pour gérer l’arrière-plan dans les fichiers ODS. Le code suivant montre comment utiliser la propriété [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) pour ajouter un arrière-plan coloré dans le fichier ODS. Veuillez voir le fichier [output ODS](90112031.ods) généré par le code à titre de référence.  

### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **Ajouter un arrière-plan graphique au fichier ODS**  

Aspose.Cells for Node.js via C++ fournit la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) pour gérer l'arrière-plan dans les fichiers ODS. L'exemple de code suivant démontre l'utilisation de la propriété [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) pour ajouter un arrière-plan graphique au fichier ODS. Veuillez voir le fichier [output ODS](90112030.ods) généré par le code pour référence.  

### **Code d'exemple**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

