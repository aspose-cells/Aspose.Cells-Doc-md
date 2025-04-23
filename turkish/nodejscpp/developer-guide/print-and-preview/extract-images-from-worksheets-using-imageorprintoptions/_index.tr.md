---
title: ImageOrPrintOptions kullanarak Sayfalardan Resim Çekme ve Node.js ile C++ kullanımı
linktitle: ImageOrPrintOptions kullanarak Çalışma Sayfalarından Görüntüleri Çıkarma
type: docs
weight: 140
url: /tr/nodejs-cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Excel sayfalarından görselleri nasıl çıkaracağınızı ve bunları Aspose.Cells for Node.js via C++ kullanarak nasıl kaydedeceğinizi öğrenin.
---

{{% alert color="primary" %}} 

Microsoft Excel kullanıcıları, elektronik tablolara resim ekleyebilir. Aspose.Cells for Node.js via C++ kullanarak, Microsoft Excel dosyalarından resimleri okuyabilir ve yerel diske kaydedebilirsiniz. Bu makale nasıl yapılacağını gösterir.

{{% /alert %}} 

Aşağıdaki örnek kod, Excel dosyasından resimleri çıkarmayı ve kaydetmeyi gösterir.



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExtractImagesFromWorksheets.xlsx"));

// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the first Picture in the first worksheet
const pic = worksheet.getPictures().get(0);

// Set the output image file path
const picformat = pic.getImageType().toString();

// Note: you may evaluate the image format before specifying the image path
// Define ImageOrPrintOptions
const printoption = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
printoption.setImageType(AsposeCells.ImageType.Jpeg);

// Save the image
pic.toImage(path.join(outputDir, "outputExtractImagesFromWorksheets.jpg"), printoption);
```
