---  
title: Zeichnen Sie eine Timeline beim Rendern von Excel in PDF mit Node.js via C++  
linktitle: Zeitleiste beim Rendern von Excel in PDF zeichnen  
type: docs  
weight: 60  
url: /de/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Verwalten Sie Zeitleisten in Excel Dateien mit Aspose.Cells for Node.js via C++.  
keywords: Render Timeline als PDF ohne Office 2013, Office 2016, Office 2019 und Office 365 Node.js via C++  
---  

## **Zeitleiste beim Rendern von Excel in PDF zeichnen**  
Wenn Sie eine Excel-Datei haben, auf die eine Zeitleiste angewendet wurde, und diese Excel-Datei mit den Zeiteinstellungen als PDF exportieren möchten, unterstützt Aspose.Cells for Node.js via C++ dies jetzt standardmäßig. Sie exportieren einfach die Excel-Datei mit Zeitleiste als PDF und das erzeugte PDF zeigt die angewendete Zeitleiste.  

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](input.xlsx), die eine vorhandene Zeitachse enthält. Anschließend speichert er die Arbeitsmappe als [ausgegebene PDF-Datei](out.pdf). Der folgende Screenshot vergleicht die Quell-Excel-Datei und die generierte PDF-Datei.  

<img src="out.png" width="60%">  

## **Beispielcode**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

