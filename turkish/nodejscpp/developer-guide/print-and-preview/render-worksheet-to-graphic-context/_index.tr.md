---
title: Node.js kullanarak C++ ile Çalışma Sayfasını Grafik Bağlamına Render etme
linktitle: Grafiksel Ortama Çalışsayısı Renderleme
type: docs
weight: 300
url: /tr/nodejs-cpp/render-worksheet-to-graphic-context/
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfasını grafik bağlamına nasıl render edeceğinizi öğrenin. Bu, görüntü dosyalarına, ekranlara ve yazıcılara render etmeyi içerir.
---

{{% alert color="primary" %}}

Aspose.Cells artık çalışma sayfalarını grafik bağlamına render edebilir. Grafik bağlamı, bir görüntü dosyası, ekran veya yazıcı gibi herhangi bir şey olabilir. Lütfen çalışma sayfasını grafik bağlamına render etmek için aşağıdaki iki yöntemden birini kullanın.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Aşağıdaki kod, Aspose.Cells kullanarak çalışma sayfasını grafik bağlamına nasıl render edeceğinizi gösterir. Kod çalıştırıldığında, çalışma sayfasını tamamıyla yazdırır ve kalan boş alanı mavi renk ile doldurur. Ayrıca resmi **OutputImage_out_.png** dosyası olarak kaydeder. Bu kodu denemek için herhangi bir Excel dosyasını kullanabilirsiniz. Ayrıca kod içindeki yorumları daha iyi anlamak için okuyunuz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
