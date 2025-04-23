---
title: Node.js ile C++ kullanarak PDF ye Filigran Ekle
linktitle: PDF ye Filigran Ekleme
type: docs
weight: 9
url: /tr/nodejs-cpp/add-watermark-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak Excel den PDF ye dönüştürürken PDF ye metin ve resim filigranları nasıl eklenir öğrenin.
---

Excel dosyasını PDF'ye dönüştürürken, PDF'ye filigran ekleme gereksiniminiz olabilir. Aşağıdaki örnekler, PDF'ye metin ve resim filigranları eklemenin nasıl yapılacağını gösterir.

## **Metin filigranı PDF'ye ekleme**

PDF'ye kolayca metin filigranı ekleyebilir, metni ve uygun fontu belirtebilirsiniz. Ayrıca, hizalama, kaydırma, döndürme, opaklık, ön plan/arka plan ve ölçek ayarlarını [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/) sayfasında yapabilirsiniz.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// prepare a workbook with 3 pages.
const wb = new AsposeCells.Workbook();
wb.getWorksheets().get(0).getCells().get("A1").putValue("Page1");
let index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page2");
index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page3");
wb.getWorksheets().get(index).getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);

// create a font for watermark, and specify bold, italic, color.
const font = new AsposeCells.RenderingFont("Calibri", 68);
font.setItalic(true);
font.setBold(true);
font.setColor(AsposeCells.Color.Blue);

// create a watermark from text and the specified font.
const watermark = new AsposeCells.RenderingWatermark("Watermark", font);

// specify horizontal and vertical alignment
watermark.setHAlignment(AsposeCells.TextAlignmentType.Center);
watermark.setVAlignment(AsposeCells.TextAlignmentType.Center);

// specify rotation
watermark.setRotation(30);

// specify opacity
watermark.setOpacity(0.6);

// specify the scale to page(e.g. 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// specify watermark for rendering to pdf.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_text_watermark.pdf", options);
```

## **Görüntü filigranı PDF'ye ekleme**

Bir PDF'ye görüntü filigranı eklemek için sadece resim baytlarını belirtmeniz yeterlidir. Ayrıca, hizalama, kaydırma, döndürme, opaklık, ön plan/arka plan ve sayfa ölçek ayarlarını [RenderingWatermark](https://reference.aspose.com/cells/nodejs-cpp/renderingwatermark/) sayfasında yapabilirsiniz.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
const fs = require("fs");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Prepare a workbook with 3 pages.
const wb = new AsposeCells.Workbook();
wb.getWorksheets().get(0).getCells().get("A1").putValue("Page1");
let index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page2");
index = wb.getWorksheets().add();
wb.getWorksheets().get(index).getCells().get("A1").putValue("Page3");
wb.getWorksheets().get(index).getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);

// Create a watermark from image (you need to prepare image bytes).
const imageBytes = fs.readFileSync(path.join(dataDir, "icon.svg"));
const watermark = new AsposeCells.RenderingWatermark(imageBytes);

// Specify offset to alignment.
watermark.setOffsetX(100);
watermark.setOffsetY(200);

// Specify rotation.
watermark.setRotation(30);

// Specify watermark to background.
watermark.setIsBackground(true);

// Specify opacity.
watermark.setOpacity(0.6);

// Specify the scale to page (e.g. 100, 50) in percent.
watermark.setScaleToPagePercent(50);

// Specify watermark for rendering to pdf.
const options = new AsposeCells.PdfSaveOptions();
options.setWatermark(watermark);

wb.save("output_image_watermark.pdf", options);
```

