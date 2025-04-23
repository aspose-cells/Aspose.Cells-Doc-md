---  
title: Lavorare con lo sfondo nei file ODS con Node.js tramite C++  
linktitle: Lavorare con lo sfondo nei file ODS  
type: docs  
weight: 150  
url: /it/nodejs-cpp/working-with-background-in-ods-files/  
description: Scopri come gestire gli sfondi nei file ODS usando Aspose.Cells for Node.js via C++.  
---  

## **Sfondo nei file ODS**  

Lo sfondo può essere aggiunto ai fogli dei file ODS. Lo sfondo può essere di colore o grafico. Lo sfondo non è visibile quando il file è aperto ma se il file viene stampato come PDF, lo sfondo è visibile nel PDF generato. Lo sfondo è anche visibile nella visualizzazione anteprima di stampa.  

Aspose.Cells for Node.js via C++ permette di leggere le informazioni di sfondo e di aggiungere sfondi nei file ODS.  

## **Leggi informazioni di sfondo dal file ODS**  

Aspose.Cells for Node.js via C++ fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice mostra l'uso della classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) caricando il file [source ODS](90112030.ods) e leggendo le informazioni di sfondo. Si prega di consultare l'output della console generato dal codice come riferimento.  

### **Codice di Esempio**  

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

### **Output della console**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **Aggiungere uno sfondo colorato al file ODS**  

Aspose.Cells for Node.js via C++ fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) per aggiungere uno sfondo colorato al file ODS. Si prega di consultare il file [output ODS](90112031.ods) generato dal codice come riferimento.  

### **Codice di Esempio**  

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

## **Aggiungere uno sfondo grafico al file ODS**  

Aspose.Cells for Node.js via C++ fornisce la classe [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) per gestire lo sfondo nei file ODS. Il seguente esempio di codice dimostra l'uso della proprietà [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) per aggiungere uno sfondo grafico al file ODS. Si prega di consultare il file [output ODS](90112030.ods) generato dal codice come riferimento.  

### **Codice di Esempio**  

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

