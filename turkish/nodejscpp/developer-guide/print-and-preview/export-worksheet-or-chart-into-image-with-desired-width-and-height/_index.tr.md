---  
title: Node.js kullanarak Sayfa veya Grafik Dışa Aktarımı ve İstenilen Genişlik ve Yükseklik ile Görüntü Oluşturma  
linktitle: İstenen Genişlik ve Yükseklikte Çalışma Sayfasını veya Şekli Görüntüye Dışa Aktar  
type: docs  
weight: 290  
url: /tr/nodejs-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/  
description: Aspose.Cells for Node.js via C++ kullanarak belirli genişlik ve yükseklikte bir sayfa veya grafiği dışa aktarmayı öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells for Node.js via C++ kullanarak, sayfa veya grafiğinizi istenilen genişlik ve yükseklikte bir görüntüye dışa aktarabilirsiniz. [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) yöntemi, dışa aktarılan görüntünün istenen genişlik ve yüksekliğini ayarlamanıza olanak tanır. Genişlik ve yükseklik piksel cinsindendir.  
{{% /alert %}}  

Aşağıdaki kod çalışma sayfasını 400x400 boyutunda bir görüntüye dışa aktarır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);

// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
