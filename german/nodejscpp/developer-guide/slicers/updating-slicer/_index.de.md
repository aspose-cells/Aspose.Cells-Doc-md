---
title: Aktualisierung des Slicers mit Node.js über C++
linktitle: Slicer aktualisieren
type: docs
weight: 50
url: /de/nodejs-cpp/updating-slicer/
description: Dieser Artikel zeigt, wie man verbundene Pivot Tabellen aktualisiert, indem man den Slicer mit Aspose.Cells for Node.js via C++ aktualisiert.
keywords: Aspose.Cells Node.js über C++, Slicer aktualisieren Node.js, wie man den Slicer in Node.js ändert, wie man den Slicer in Node.js anpasst, wie man die Slicer Artikel in Node.js auswählt oder abwählt über C++.
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Slicer in Microsoft Excel aktualisieren möchten, wählen oder abwählen Sie die Artikel, und der Slicer-Tabellen oder Pivot-Tabellen werden entsprechend aktualisiert. Bitte verwenden Sie [**Slicer.getSlicerCacheItems()**](https://reference.aspose.com/cells/nodejs-cpp/slicercache/#getSlicerCacheItems--), um Slicer-Artikel mit Aspose.Cells auszuwählen oder abzuwählen, und rufen dann die Methode [**Slicer.refresh()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#refresh--) auf, um den Slicer-Tabellen oder Pivot-Tabellen zu aktualisieren.

## **Wie man den Slicer aktualisiert**

Der folgende Beispielscode lädt die [Beispiel-Excel-Datei](67338475.xlsx), die einen vorhandenen Slicer enthält. Es entwählt die 2. und 3. Elemente des Slicers und aktualisiert den Slicer. Anschließend speichert es die Arbeitsmappe unter [Ausgabe-Excel-Datei](67338476.xlsx). Der folgende Screenshot zeigt die Auswirkung des Beispielscodes auf die Beispiel-Excel-Datei. Wie Sie auf dem Screenshot sehen können, wurde durch das Aktualisieren des Slicers mit ausgewählten Elementen auch die Pivot-Tabelle entsprechend aktualisiert.

![todo:image_alt_text](updating-slicer_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleUpdatingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Access the slicer items.
const scItems = slicer.getSlicerCache().getSlicerCacheItems();

const items = slicer.getSlicerCache().getSlicerCacheItems();

for (let i = 0; i < items.getCount(); i++) {
const item = items.get(i);
if (item.getValue() === "Pink" || item.getValue() === "Green") {
item.setSelected(false);
}
}
slicer.refresh();
wb.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
