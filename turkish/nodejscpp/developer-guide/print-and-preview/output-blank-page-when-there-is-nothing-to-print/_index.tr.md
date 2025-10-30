---
title: Yazdırılacak hiçbir şey yoksa, Node.js ile C++ kullanarak boş sayfa çıktı verir
linktitle: Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı
type: docs
weight: 90
url: /tr/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Olası Kullanım Senaryoları**

Sayfa boşsa, Aspose.Cells herhangi bir içerik iletmeyebilir. Bu davranışı [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) özelliğini kullanarak değiştirebilirsiniz. Bu özelliği **true** olarak ayarladığınızda, boş sayfa yazdırılır.

## **Hiçbir şey Yazdırılacak Değilken Boş Sayfa Çıktısı**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve içinde boş bir sayfa bulunur, [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) özelliği **true** olarak ayarlandıktan sonra, boş sayfa oluşturarak aşağıdaki resimde görebileceğiniz gibi çıktı alır.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
