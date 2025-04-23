---  
title: Randabstände von Kommentar oder Form innerhalb des Arbeitsblatts mit Node.js über C++ einstellen  
linktitle: Abstände von Kommentaren oder Formen im Arbeitsblatt festlegen  
type: docs  
weight: 1500  
url: /de/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Lernen Sie, wie man die Randabstände von Kommentaren oder Formen innerhalb eines Excel Arbeitsblatts mit Aspose.Cells for Node.js via C++ festlegt.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells erlaubt es, die Ränder jeder Form oder Kommentar mit der [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/)-Eigenschaft festzulegen. Diese Eigenschaft gibt das Objekt der Klasse [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) zurück, das verschiedene Eigenschaften wie [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--) usw. hat, die verwendet werden können, um die oberen, linken, unteren und rechten Ränder festzulegen.  

## **Ränder des Kommentars oder der Form innerhalb des Arbeitsblatts festlegen**  

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](61767851.xlsx), die zwei Formen enthält. Der Code greift nacheinander auf die Formen zu und stellt ihre oberen, linken, unteren und rechten Ränder ein. Bitte sehen Sie sich die durch den Code generierte [Ausgabedatei](61767852.xlsx) und den Screenshot an, der die Wirkung des Codes auf die Ausgabedatei zeigt.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

const shapes = ws.getShapes();
for (let i = 0; i < shapes.getCount(); i++) {
const sh = shapes.get(i);
// Access the text alignment
const txtAlign = sh.getTextBody().getTextAlignment();

// Set auto margin false
txtAlign.setIsAutoMargin(false);

// Set the top, left, bottom and right margins
txtAlign.setTopMarginPt(10);
txtAlign.setLeftMarginPt(10);
txtAlign.setBottomMarginPt(10);
txtAlign.setRightMarginPt(10);
}

// Save the output Excel file
workbook.save("outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");
```  

