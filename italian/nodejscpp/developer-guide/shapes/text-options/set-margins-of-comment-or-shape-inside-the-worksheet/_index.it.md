---  
title: Imposta i margini del commento o della forma all interno del foglio di lavoro con Node.js via C++  
linktitle: Imposta i margini del commento o della forma all interno del foglio di lavoro  
type: docs  
weight: 1500  
url: /it/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Impara come impostare i margini di commenti o forme all’interno di un foglio Excel usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells ti permette di impostare i margini di qualsiasi forma o commento usando la proprietà [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/). Questa proprietà restituisce l'oggetto della classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment) che ha diverse proprietà, ad esempio [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--), ecc., che possono essere usate per impostare i margini superiore, sinistro, inferiore e destro.  

## **Imposta i Margini del Commento o della Forma all'interno del Foglio di Lavoro**  

Si prega di vedere il seguente codice di esempio. Carica il [file di Excel di esempio](61767851.xlsx) che contiene due forme. Il codice accede alle forme una per volta e imposta i loro margini superiore, sinistro, inferiore e destro. Si prega di vedere il [file di Excel di output](61767852.xlsx) generato dal codice e la schermata che mostra l'effetto del codice sul file di Excel di output.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Codice di Esempio**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
