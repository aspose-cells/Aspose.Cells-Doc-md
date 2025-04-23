---  
title: Slicer mit Node.js via C++ formatieren  
linktitle: Slicer formatieren  
type: docs  
weight: 20  
url: /de/nodejs-cpp/formatting-slicer/  
---  

## **Mögliche Verwendungsszenarien**  

Sie können den Slicer in Microsoft Excel formatieren, indem Sie die Anzahl der Spalten oder den Stil usw. einstellen. Aspose.Cells for Node.js via C++ ermöglicht dies auch durch die Eigenschaften [**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--) und [**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--).  

## **Formatierung Schneidwerkzeug**  

Bitte sehen Sie sich den folgenden Code an. Es lädt die [Beispiel-Excel-Datei](67338473.xlsx), die einen Slicer enthält. Es greift auf den Slicer zu und stellt die Anzahl der Spalten und den Stiltyp ein und speichert ihn als [Ausgabe-Excel-Datei](67338474.xlsx). Der Screenshot zeigt, wie der Slicer nach der Ausführung des Beispielcodes aussieht.  

![todo:image_alt_text](formatting-slicer_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

