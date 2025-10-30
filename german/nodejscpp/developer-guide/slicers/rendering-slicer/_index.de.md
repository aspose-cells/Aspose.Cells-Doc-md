---  
title: Rendering des Slicers mit Node.js über C++  
linktitle: Slicer rendern  
type: docs  
weight: 40  
url: /de/nodejs-cpp/rendering-slicer/  
---  

## **Mögliche Verwendungsszenarien**  
Aspose.Cells for Node.js via C++ unterstützt das Rendern von Slicer-Formen. Wenn Sie Ihr Arbeitsblatt in ein Bild konvertieren oder Ihre Arbeitsmappe in PDF- oder HTML-Formate speichern, werden die Slicer korrekt gerendert.  

## **Slicer rendern**  
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338479.xlsx), die einen bestehenden Slicer enthält. Er wandelt das Arbeitsblatt in ein Bild um, indem er den Druckbereich festlegt, der nur den Slicer abdeckt. Das resultierende Bild ist das [Ausgabebild](67338480.png), das den gerenderten Slicer zeigt. Wie Sie sehen können, wurde der Slicer richtig gerendert und sieht genauso aus wie in der Beispiel-Excel-Datei.  

![todo:image_alt_text](rendering-slicer_1)  
## **Beispielcode**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderingSlicer.xlsx");

// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Set the print area because we want to render slicer only.
ws.getPageSetup().setPrintArea("B15:E25");

// Specify image or print options, set one page per sheet and only area to true.
const imgOpts = new AsposeCells.ImageOrPrintOptions();
imgOpts.setHorizontalResolution(200);
imgOpts.setVerticalResolution(200);
imgOpts.setImageType(AsposeCells.ImageType.Png);
imgOpts.setOnePagePerSheet(true);
imgOpts.setOnlyArea(true);

// Create sheet render object and render worksheet to image.
const sr = new AsposeCells.SheetRender(ws, imgOpts);
sr.toImage(0, "outputRenderingSlicer.png");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
