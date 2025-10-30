---
title: Kommentare beim Speichern von Excel Dateien als HTML mit Node.js über C++ exportieren
linktitle: Export von Kommentaren beim Speichern von Excel Datei in HTML
type: docs
weight: 40
url: /de/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie Ihre Excel-Datei in HTML speichern, werden Kommentare nicht exportiert. Aspose.Cells for Node.js via C++ bietet diese Funktion jedoch mit der Eigenschaft [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Wenn Sie diese auf **true** setzen, werden Kommentare im HTML ebenfalls angezeigt.

## **Kommentare beim Speichern einer Excel-Datei in HTML exportieren**

Der folgende Beispielscode erläutert die Verwendung der [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)-Eigenschaft. Der Screenshot zeigt die Auswirkung des Codes auf das HTML, wenn es auf **true** gesetzt ist. Bitte laden Sie die [Beispiel-Excel-Datei](50528260.xlsx) und das [generierte HTML](5052826.txt) für eine Referenz herunter.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
