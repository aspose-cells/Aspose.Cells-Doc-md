---  
title: Node.js ile C++ kullanarak Excel’i Yüksek Çözünürlükte Görüntüye Dönüştürme  
linktitle: Excel Dosyasını Yüksek Çözünürlüklü Görüntüye Dönüştür  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/convert-excel-to-high-resolution-image/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını yüksek çözünürlüklü resimlere nasıl dönüştüreceğinizi öğrenin.  
---  

Yüksek çözünürlüklü ekranların yaygınlaşmasıyla, varsayılan 96 DPI'da üretilen resimler genellikle bulanık ve net olmayan görünür. Yüksek çözünürlüklü ekranlarda netlik sağlamak için, daha yüksek DPI ile resim üretmek gerekir. Aspose.Cells for Node.js via C++, [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) ve [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--) ayarlarını yapmanızı sağlayan özellikler sunar, böylece yüksek çözünürlüklü ekranlarda net görünen yüksek kaliteli resimler oluşturabilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);

// Get the worksheet
const sheet = workbook.getWorksheets().get(0);

// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);

// Generate and save the image
render.toImage(0, "output.png");
```  

