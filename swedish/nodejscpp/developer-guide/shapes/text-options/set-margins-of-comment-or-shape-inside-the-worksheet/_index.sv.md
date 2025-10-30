---  
title: Ställ in Marginaler för Kommentar eller Form inuti Arket med Node.js via C++  
linktitle: Ställ in marginaler för kommentar eller shape i kalkylbladet  
type: docs  
weight: 1500  
url: /sv/nodejs-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Lär dig hur du ställer in marginalerna för kommentarer eller former inom ett Excel ark med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells tillåter dig att ställa in marginalerna för vilken form eller kommentar som helst med hjälp av [**Shape.textBody.textAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/)-egenskapen. Denna egenskap returnerar objektet av [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment)-klassen som har olika egenskaper, t.ex. [**ShapeTextAlignment.getTopMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getTopMarginPt--), [**ShapeTextAlignment.getLeftMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getLeftMarginPt--), [**ShapeTextAlignment.getBottomMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getBottomMarginPt--), [**ShapeTextAlignment.getRightMarginPt()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRightMarginPt--), etc., som kan användas för att ställa in topp-, vänster-, botten- och högermarginaler.  

## **Ställ in marginaler för kommentar eller shape i kalkylbladet**  

Se nedan kodexempel. Den laddar den [provExcel-filen](61767851.xlsx) som innehåller två former. Koden har åtkomst till formerna en i taget och ställer in deras topp-, vänster-, botten- och högermarginaler. Se den [utdataExcel-filen](61767852.xlsx) genererad av koden och skärmbild som visar effekten av koden på utdataExcel-filen.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Exempelkod**  

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
