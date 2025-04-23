---  
title: Crea immagine trasparente di un foglio di lavoro Excel con Node.js tramite C++  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /it/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Scopri come generare un immagine trasparente di un foglio di lavoro Excel usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A volte è necessario generare l'immagine del tuo foglio di lavoro come un'immagine trasparente. Desideri applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce la proprietà [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è **false**, le celle senza colori di riempimento vengono disegnate con il colore bianco e quando è **true**, le celle senza colori di riempimento vengono disegnate in modo trasparente.  

{{% /alert %}}  

Nell'immagine del foglio di lavoro seguente, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate di bianco.  

|**Output senza trasparenza: lo sfondo della cella è bianco**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Mentre, nell'immagine del foglio di lavoro seguente, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.  

|**Output con trasparenza abilitata**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Il seguente codice di esempio genera un'immagine trasparente da un foglio di lavoro di Excel.  

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

