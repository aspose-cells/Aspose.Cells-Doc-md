---
title: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist, Node.js über C++
linktitle: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Dieser Artikel enthält Anweisungen und Beispielcode, um programmgesteuert festzustellen, ob ein Excel Arbeitsblatt ein Dialogblatt ist, mit Aspose.Cells for Node.js via C++.
keywords: Excel Dialogblatt Typ mit Node.js über C++ finden, Dialogblatt Arbeitsblatt Node.js über C++
---

## **Mögliche Verwendungsszenarien**

Dialogblatt ist ein altes Format eines Blatts, das eine Dialogbox enthält. Ein solches Blatt kann von einer älteren Version von Microsoft Excel, z. B. 2003, eingefügt werden, wie in diesem Screenshot gezeigt. Es kann auch in neueren Versionen, z. B. Microsoft Excel 2016, mit VBA eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt oder eine andere Art von Blatt ist, indem Sie die Eigenschaft [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) verwenden, die von Aspose.Cells for Node.js via C++ bereitgestellt wird. Wenn sie den Enumerationswert [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) zurückgibt, bedeutet dies, dass es sich um ein Dialogblatt handelt.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716820.xlsx), die ein Dialogblatt enthält. Er prüft die Eigenschaft [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--), vergleicht sie mit [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) und gibt dann die Nachricht aus. Für weitere Hilfe siehe die Konsolenausgabe des Beispielcodes unten.

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Konsolenausgabe**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
