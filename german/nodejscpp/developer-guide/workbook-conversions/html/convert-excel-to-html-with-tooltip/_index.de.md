---  
title: Konvertieren von Excel zu HTML mit Tooltip unter Verwendung von Node.js über C++  
linktitle: Excel in HTML mit Tooltip konvertieren  
type: docs  
weight: 200  
url: /de/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Lernen Sie, wie Sie Excel Dateien im HTML Format mit Tooltips für die vollständige Textanzeige mithilfe von Aspose.Cells for Node.js via C++ konvertieren.  
---  

## **Excel in HTML mit Tooltip konvertieren**

 Es kann Fälle geben, in denen der Text im generierten HTML abgeschnitten ist und Sie möchten, dass der vollständige Text als Tooltip beim Hover angezeigt wird. Aspose.Cells for Node.js via C++ unterstützt dies, indem es die [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)-Eigenschaft bereitstellt. Wenn Sie die [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--)-Eigenschaft auf **true** setzen, wird der vollständige Text als Tooltip im generierten HTML hinzugefügt.

Das folgende Bild zeigt den Tooltip in der generierten HTML-Datei.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

 Das folgende Code-Beispiel lädt die [Quellexcel-Datei](98107416.xlsx) und generiert die [Ausgabe-HTML-Datei](98107417.zip) mit Tooltip.

Beispielcode

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

