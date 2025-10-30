---  
title: Arbeta med bakgrund i ODS filer med Node.js via C++  
linktitle: Arbeta med bakgrund i ODS filer  
type: docs  
weight: 150  
url: /sv/nodejs-cpp/working-with-background-in-ods-files/  
description: Lär dig att hantera bakgrunder i ODS filer med Aspose.Cells for Node.js via C++.  
---  

## **Bakgrund i ODS-filer**  

Bakgrund kan läggas till i kalkylblad i ODS-filer. Bakgrunden kan antingen vara en färgad bakgrund eller en grafisk bakgrund. Bakgrunden är inte synlig när filen är öppen, men om filen skrivs ut som PDF är bakgrunden synlig i den genererade PDF:en. Bakgrunden är också synlig i utskriftsvisningen.  

Aspose.Cells for Node.js via C++ ger möjligheten att läsa bakgrundsinformation och lägga till bakgrund i ODS-filer.  

## **Läs bakgrundsinformation från ODS-fil**  

Aspose.Cells for Node.js via C++ erbjuder [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) klass genom att ladda [käll-ODS](90112030.ods) filen och läsa bakgrundsinformationen. Se gärna kodens konsolutdata för referens.  

### **Exempelkod**  

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

### **Konsoloutput**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Lägg till färgad bakgrund i ODS-fil**  

Aspose.Cells for Node.js via C++ ger [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) egenskap för att lägga till en färgbakgrund till ODS-filen. Se gärna [utgivan ODS](90112031.ods) filen som genererats av koden för referens.  

### **Exempelkod**  

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

## **Lägg till grafisk bakgrund i ODS-fil**  

Aspose.Cells for Node.js via C++ ger [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) klassen för att hantera bakgrund i ODS-filer. Följande kodexempel visar användningen av [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) egenskap för att lägga till grafisk bakgrund till ODS-filen. Se gärna [utgivan ODS](90112030.ods) filen som genererats av koden för referens.  

### **Exempelkod**  

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
