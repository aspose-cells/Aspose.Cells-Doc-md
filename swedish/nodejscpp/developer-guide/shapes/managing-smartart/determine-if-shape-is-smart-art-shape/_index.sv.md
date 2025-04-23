---  
title: Avgör om Shape är en Smart Art form med Node.js via C++  
linktitle: Avgöra om en form är Smart Art Shape  
type: docs  
weight: 400  
url: /sv/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Lär dig hur man avgör om en form i Excel är en Smart Art form med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Smart Art-former är speciella former i Microsoft Excel som tillåter dig att skapa komplexa diagram automatiskt. Du kan ta reda på om formen är en smart art-form eller en vanlig form med hjälp av [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) egenskapen.  

## **Avgör om formen är en SmartArt-form**  

Följande exempelkod laddar den [provexemplet](55541792.xlsx) som innehåller en smart art-form som visas i denna skärmdump. Den skriver ut värdet av [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) egenskapen för den första formen. Se vänligen exempelutdata i konsolen nedan.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Konsoloutput**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

