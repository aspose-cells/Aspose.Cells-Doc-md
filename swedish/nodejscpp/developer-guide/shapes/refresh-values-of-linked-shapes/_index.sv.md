---  
title: Uppdatera värden för länkade former med Node.js via C++  
linktitle: Uppdatera värdena för länkade former  
type: docs  
weight: 3200  
url: /sv/nodejs-cpp/refresh-values-of-linked-shapes/  
description: Lär dig hur du uppdaterar värdena för länkade former i Excel med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Ibland har du en länkad form i din Excel-fil som är kopplad till en cell. I Microsoft Excel ändras värdet i den länkar cellen även i den länkade formen. Detta fungerar också utmärkt med Aspose.Cells for Node.js via C++ om du vill spara din arbetsbok i XLS- eller XLSX-format. Men om du vill spara i PDF- eller HTML-format måste du anropa [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)-metoden för att uppdatera värdet på den länkade formen.  

{{% /alert %}}  

## Exempel  

Följande skärmdump visar käll-Excel-filen som används i exempelnumret nedan. Den har en länkad bild kopplad till cellerna A1 till E4. Vi kommer att ändra värdet i cell B4 med Aspose.Cells och sedan anropa [**ShapeCollection.updateSelectedValue()**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#updateSelectedValue--)-metoden för att uppdatera värdet på bilden och spara den i PDF-format.  

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)  

Du kan ladda ner [källa-Excelfilen](95584291.xlsx) och [utdata-PDF](95584292.pdf) från angivna länkar.  

### Node.js-kod för att uppdatera värdena för länkade former  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleRefreshValueOfLinkedShapes.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Change the value of cell B4
const cell = worksheet.getCells().get("B4");
cell.putValue(100);

// Update the value of the Linked Picture which is linked to cell B4
worksheet.getShapes().updateSelectedValue();

// Save the workbook in PDF format
workbook.save(path.join(outputDir, "outputRefreshValueOfLinkedShapes.pdf"), AsposeCells.SaveFormat.Pdf);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
