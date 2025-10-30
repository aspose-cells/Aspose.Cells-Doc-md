---
title: Zugriff auf und Änderung der Anzeige Label des verknüpften Ole Objekts mit Node.js via C++
linktitle: Auf das Anzeigen des verknüpften Ole Objekts zugreifen und es ändern
type: docs
weight: 100
url: /de/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Lernen, wie man den Anzeige Label eines verknüpften Ole Objekts mit Aspose.Cells for Node.js via C++ zugreift und ändert. 
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel erlaubt es, das Anzeige-Label des Ole-Objekts zu ändern, wie im folgenden Screenshot gezeigt. Sie können auch das Anzeige-Label des Ole-Objekts mit Aspose.Cells APIs über die Eigenschaft [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--) zugreifen oder modifizieren.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern**

Bitte sehen Sie sich den folgenden Beispielcode an, der die <a href="64716810.xlsx">Beispieldatei für Excel</a> lädt, die das Ole-Objekt enthält. Der Code greift auf das Ole-Objekt zu und ändert sein Label von Sample APIs zu Aspose APIs. Unten sehen Sie die Konsolen-Ausgabe, die den Effekt des Beispielcodes auf die Beispieldatei zeigt.

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Konsolenausgabe**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
