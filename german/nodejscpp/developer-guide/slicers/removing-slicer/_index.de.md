---
title: Entfernen des Slicers mit Node.js über C++
linktitle: Slicer entfernen
type: docs
weight: 30
url: /de/nodejs-cpp/removing-slicer/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer in Excel entfernen möchten, wählen Sie ihn aus und drücken Sie die *Entfernen*-Taste. Wenn Sie ihn programmatisch mit der Aspose.Cells API entfernen möchten, verwenden Sie die [**SlicerCollection.remove(Slicer)**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#remove-slicer-)-Methode. Dadurch wird der Slicer aus der Arbeitsblatt entfernt.

## **Slicer entfernen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](67338478.xlsx), die einen bestehenden Slicer enthält. Er greift auf die Slicer zu, entfernt sie und speichert die Arbeitsmappe als [Ausgabedatei Excel](67338477.xlsx). Das folgende Bild zeigt den Slicer, der nach der Ausführung des Beispielcodes entfernt wird.

![todo:image_alt_text](removing-slicer_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRemovingSlicer.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Remove slicer.
worksheet.getSlicers().remove(slicer);

// Save the workbook in output XLSX format.
workbook.save("outputRemovingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```
