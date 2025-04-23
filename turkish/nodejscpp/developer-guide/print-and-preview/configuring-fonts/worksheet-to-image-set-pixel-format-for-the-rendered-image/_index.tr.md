---  
title: Çalışma sayfasını Görüntüye Dönüştürmek  Render Edilen Görüntü İçin Piksel Formatı Ayarla (Node.js ve C++ ile)  
linktitle: Resim Olarak Çalışma Sayfası  Oluşturulan Resim İçin Piksel Biçimini Ayarla  
type: docs  
weight: 200  
url: /tr/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/  
---  

{{% alert color="primary" %}}  
Bazı durumlarda çalışma sayfasını resim biçimine dönüştürürken piksel biçimini belirtmek isteyebilirsiniz. Aspose.Cells varsayılan olarak her piksel için 32 bit kullanır. Aspose.Cells, oluşturulan resmin piksel biçimini (bit derinliği) özelleştirmenize olanak tanır.  
{{% /alert %}}  

Aşağıdaki örnek kodu inceleyin, yaprakların resimlendiği sırada istenen piksel biçimini nasıl ayarlayacağınızı gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Load an Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetPixelFormatRenderedImage.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the ImageOrPrintOptions with desired color depth (24 bits per pixel) and image format type
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setTiffColorDepth(AsposeCells.ColorDepth.Format24bpp);
opts.setImageType(AsposeCells.ImageType.Tiff);

// Instantiate SheetRender object based on the first worksheet
const sheetRender = new AsposeCells.SheetRender(worksheet, opts);

// Save the image (first page of the sheet) with the specified options
sheetRender.toImage(0, path.join(outputDir, "outputSetPixelFormatRenderedImage.tiff"));
```  

