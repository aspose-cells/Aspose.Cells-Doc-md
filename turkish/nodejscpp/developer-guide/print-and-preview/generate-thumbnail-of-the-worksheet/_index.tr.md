---
title: Node.js kullanarak Sayfa Önizlemesi Görüntüsü Oluşturma
linktitle: Çalışma Sayfasının Küçük Resmi Oluşturma
type: docs
weight: 110
url: /tr/nodejs-cpp/generate-thumbnail-of-the-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak bir sayfadan küçük resim oluşturmayı öğrenin. Belge ve sunumlarda önizleme için küçük resimler oluşturun.
---

{{% alert color="primary" %}} 

Çalışma sayfalarından küçük resimler oluşturmak faydalı olabilir. Bir küçük resim, çalışma sayfasındaki içeriğin bir ön izlemesini vermek üzere bir Word belgesine veya bir PowerPoint sunumuna yapıştırılabilir. Gerçek belgenin indirme bağlantısına bir bağlantıyla bir web sayfasına eklenebilir ve diğer birçok kullanımı bulunmaktadır.

{{% /alert %}} 

Aspose.Cells for Node.js via C++, sayfaları görüntü dosyalarına çıktı olarak verme olanağı sağlar, böylece küçük resim yapmak kolaydır. Aşağıdaki örnek kod, sayfaları görüntü dosyalarına nasıl çıktı alınacağını gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiate and open an Excel file
const filePath = path.join(sourceDir, "sampleGenerateThumbnailOfWorksheet.xlsx");
const book = new AsposeCells.Workbook(filePath);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Set the vertical and horizontal resolution
imgOptions.setVerticalResolution(200);
imgOptions.setHorizontalResolution(200);

// One page per sheet is enabled
imgOptions.setOnePagePerSheet(true);

// Set desired thumbnail dimensions
imgOptions.setDesiredSize(600, 600, true);

// Get the first worksheet
const sheet = book.getWorksheets().get(0);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the thumbnail directly
sr.toImage(0, path.join(outputDir, "outputGenerateThumbnailOfWorksheet.jpg"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
