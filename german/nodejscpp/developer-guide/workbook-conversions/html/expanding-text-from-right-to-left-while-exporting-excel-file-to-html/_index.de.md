---  
title: Text beim Exportieren der Excel Datei nach HTML nach rechts zu erweitern mit Node.js über C++  
linktitle: Text von rechts nach links erweitern, während Excel Datei in HTML exportiert wird  
type: docs  
weight: 60  
url: /de/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells unterstützt jetzt das Erweitern von Text von rechts nach links beim Exportieren von Excel-Dateien in HTML. Diese Funktion wurde seit der Version v8.9.0.0 implementiert. Wenn Ihre Quell-Excel-Datei also einen Text enthält, der von rechts nach links erweitert, exportiert Aspose.Cells dies korrekt in HTML.  

{{% /alert %}}  
## **Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird**  
Der folgende Beispielscode konvertiert die [Beispiel-Excel-Datei](5115502.xlsx) in HTML. Dieser Screenshot zeigt, wie das Beispiel-Excel in Microsoft Excel 2013 aussieht.  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

Dieser Screenshot zeigt die [ausgegebene HTML mit älterer Version](5115509).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

Dieser Screenshot zeigt die [ausgegebene HTML mit neuerer Version](5115508).  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

Wie Sie in den Screenshots sehen können, erweitert die neuere Version den rechtsbündigen Text genau wie Microsoft Excel korrekt nach links.  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

