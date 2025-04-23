---  
title: Exportieren eines ähnlichen Randstils, wenn der Randstil vom Webbrowser nicht unterstützt wird, mit Node.js via C++  
linktitle: Ähnlichen Rahmenstil exportieren, wenn der Rahmenstil von Webbrowsern nicht unterstützt wird  
type: docs  
weight: 70  
url: /de/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Lernen Sie, wie Sie Grenzen exportieren, die von Webbrowsern beim Konvertieren von Excel in HTML nicht unterstützt werden, mithilfe von Aspose.Cells for Node.js via C++.  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel unterstützt einige Arten von gestrichelten Rändern, die von Webbrowsern nicht unterstützt werden. Beim Konvertieren einer solchen Excel-Datei in HTML mit Aspose.Cells for Node.js via C++ werden diese Ränder entfernt. Aspose.Cells kann diese Grenzen jedoch ebenfalls mit der Eigenschaft [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--) unterstützen. Bitte setzen Sie deren Wert auf **true**, um auch diese nicht unterstützten Grenzen in die HTML-Datei zu exportieren.  

## **Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716806.xlsx), die einige nicht unterstützte Rahmen enthält, wie im folgenden Screenshot gezeigt. Der Screenshot veranschaulicht weiter die Wirkung der [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)-Eigenschaft innerhalb des [Ausgab-HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

