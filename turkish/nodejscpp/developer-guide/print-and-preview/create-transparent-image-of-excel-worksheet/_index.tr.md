---  
title: Node.js ile C++ kullanarak Excel Sayfası Transparan Görüntüsü Oluşturma  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /tr/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel sayfasının şeffaf görüntüsünü nasıl oluşturacağınızı öğrenin.  
---  

{{% alert color="primary" %}}  

Bazen çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekebilir. Dolgu renkleri olmayan tüm hücrelere şeffaflık uygulamak istersiniz. Aspose.Cells, çalışma sayfasına şeffaflık uygulamak için [**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--) özelliğini sağlar. Bu özellik **false** olduğunda, dolgu renkleri olmayan hücreler beyaz renkle çizilir ve **true** olduğunda, dolgu renkleri olmayan hücreler şeffaf şekilde çizilir.  

{{% /alert %}}  

Aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmamıştır. Dolgu rengi olmayan hücreler beyaz olarak çizilmiştir.  

|**Şeffaflık olmadan çıktı: hücre arka planı beyazdır**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

Ancak aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaf olarak çizilmiştir.  

|**Şeffaflık etkinleştirilmiş çıktı**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

Aşağıdaki örnek kod, bir Excel çalışma sayfasından şeffaf bir görüntü oluşturur.  

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
