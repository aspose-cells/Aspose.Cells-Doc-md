---  
title: Skapa Transparent Bild av Excel Arbetsblad med Node.js via C++  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /sv/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Lär dig hur man genererar en transparent bild av ett Excel arbetsblad med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Ibland behöver du generera bilden av ditt arbetsblad som en transparent bild. Du vill applicera transparens på alla celler som inte har fyllnadsfärger. Aspose.Cells tillhandahåller egenskapen [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) för att applicera transparens på arbetsbilden. När denna egenskap är **false**, då ritas celler utan fyllnadsfärger med vit färg och när den är **true**, ritas celler utan fyllnadsfärger transparent.  

{{% /alert %}}  

I följande arbetsbladsbild har inte transparens tillämpats. Celler utan fyllfärger är ritade vita.  

|**Utdata utan transparens: cellens bakgrund är vit**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Medan i följande arbetsbladsbild har transparens tillämpats. Cellerna utan fyllfärger är transparenta.  

|**Utdata med aktiverad transparens**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Följande exempelkod genererar en transparent bild från ett Excel-ark.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
