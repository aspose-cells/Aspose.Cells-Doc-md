---  
title: Arbeit mit Hintergrund in ODS Dateien mit Node.js via C++  
linktitle: Arbeiten mit Hintergrund in ODS Dateien  
type: docs  
weight: 150  
url: /de/nodejs-cpp/working-with-background-in-ods-files/  
description: Lernen Sie, wie Sie Hintergründe in ODS Dateien mit Aspose.Cells for Node.js via C++ verwalten.  
---  

## **Hintergrund in ODS-Dateien**  

Hintergrund kann zu Blättern in ODS-Dateien hinzugefügt werden. Der Hintergrund kann entweder ein farbiger Hintergrund oder ein grafischer Hintergrund sein. Der Hintergrund ist nicht sichtbar, wenn die Datei geöffnet ist, aber wenn die Datei als PDF gedruckt wird, ist der Hintergrund im generierten PDF sichtbar. Der Hintergrund ist auch in der Druckvorschau sichtbar.  

Aspose.Cells for Node.js via C++ bietet die Fähigkeit, Hintergrundinformationen zu lesen und den Hintergrund in ODS-Dateien hinzuzufügen.  

## **Hintergrundinformationen aus ODS-Datei lesen**  

Aspose.Cells for Node.js via C++ stellt die [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)-Klasse bereit, um Hintergründe in ODS-Dateien zu verwalten. Das folgende Code-Beispiel zeigt die Verwendung der [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)-Klasse durch Laden der [Quell-ODS](90112030.ods) Datei und Lesen der Hintergrundinformationen. Bitte sehen Sie die vom Code generierte Konsolenausgabe zur Referenz an.  

### **Beispielcode**  

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

### **Konsolenausgabe**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Farbigen Hintergrund zu ODS-Datei hinzufügen**  

Aspose.Cells for Node.js via C++ bietet die [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)-Klasse zur Verwaltung des Hintergrunds in ODS-Dateien. Das folgende Code-Beispiel demonstriert die Verwendung der [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--)-Eigenschaft, um einen Farbhintergrund zur ODS-Datei hinzuzufügen. Bitte sehen Sie die [Ausgabedatei ODS](90112031.ods) des Codes zur Referenz.  

### **Beispielcode**  

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

## **Grafischen Hintergrund zu ODS-Datei hinzufügen**  

Aspose.Cells for Node.js via C++ bietet die [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground)-Klasse zur Verwaltung des Hintergrunds in ODS-Dateien. Das folgende Code-Beispiel demonstriert die Verwendung der [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--)-Eigenschaft, um einen grafischen Hintergrund zur ODS-Datei hinzuzufügen. Bitte sehen Sie die [Ausgabedatei ODS](90112030.ods), die vom Code generiert wurde, zur Referenz.  

### **Beispielcode**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
