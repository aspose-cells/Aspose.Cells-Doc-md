---  
title: Transparentes Excel Arbeitsblatt Bild mit Node.js via C++ erstellen  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /de/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Erfahren Sie, wie Sie ein transparentes Bild eines Excel Arbeitsblatts mit Aspose.Cells for Node.js via C++ generieren.  
---  

{{% alert color="primary" %}}  

Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--)-Eigenschaft, um Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft **false** ist, werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet, und wenn sie **true** ist, werden Zellen ohne Füllfarben transparent gezeichnet.  

{{% /alert %}}  

In der folgenden Arbeitsblattansicht wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben sind weiß gezeichnet.  

|**Ausgabe ohne Transparenz: Der Zellenhintergrund ist weiß**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Während in der folgenden Arbeitsblattansicht Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.  

|**Ausgabe mit aktivierter Transparenz**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Der folgende Beispielscode generiert ein transparentes Bild aus einem Excel-Arbeitsblatt.  

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

