---
title: Node.js ve C++ kullanarak Sayfa Ayarlarını Ölçeklendirme Faktörünü Hesapla
linktitle: Sayfa Ayarı Ölçek Faktörünü Hesaplayın
type: docs
weight: 300
url: /tr/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Bu makale, Excel çalışma sayfasının Sayfa Ayarlarını uygun sayfa genişliği ve yüksekliği seçeneklerini kullanarak programatik olarak hesaplama ve skala faktörü belirleme konusunda örnek kod sağlar.
keywords: N sayfa genişliğinde ve M sayfa yüksekliğinde Excel Node.js ve C++ ile, sayfa ayarlarını hesapla
---

{{% alert color="primary" %}}

Sayfa Ayarlarını kullanırken **N sayfa genişliğinde ve M sayfa yüksekliğinde** seçeneği, Microsoft Excel'in Sayfa Ayarlarını Hesaplama Faktörünü otomatik olarak hesaplar. Bunu [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) özelliği kullanarak da yapabilirsiniz. Bu özellik bir çift değer döndürür ve yüzde değere dönüştürülebilir. Örneğin, döndürdüğü değer 0.5 ise, ölçekleme faktörü %50 anlamına gelir.

{{% /alert %}}

Aşağıdaki örnek kod, [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) özelliğini kullanarak sayfa ayarı ölçek faktörünü hesaplamanın örneklerini göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
