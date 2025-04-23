---
title: Dateien mit Node.js via C++ zusammenführen
linktitle: Dateien zusammenführen
type: docs
weight: 20
url: /de/nodejs-cpp/merge-files/
---

## **Einführung**

Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln kann die [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-)-Methode verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-)-Methode, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, könnten sie systemintensiv sein. Um dies zu vermeiden, verwenden Sie die statische Methode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-), die effizienter ist, um mehrere Dateien zu zusammenzuführen.

## **Dateien mit Aspose.Cells for Node.js via C++ zusammenführen**

Der folgende Beispielcode zeigt, wie große Dateien mit der [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-)-Methode zusammengeführt werden. Es nimmt zwei einfache, aber große Dateien, Book1.xls und Book2.xls. Die Dateien enthalten formatierten Daten und Formeln.

{{% alert color="primary" %}}

Die Methode [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) unterstützt nur das Zusammenführen von Daten, Stilen, Formatierung und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden möglicherweise nicht mit dieser Methode zusammengeführt. Darüber hinaus wird eine Zwischenspeicherdatei verwendet, um temporäre Daten für den Prozess zu speichern.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
