---
title: Çıktı PDF sinde Yazdırılacak Bir Şey Yoksa Boş Sayfa Oluşmasını Önleme ile Node.js ve C++
linktitle: Boş sayfa olmadığında Çıktı PDF de Boş Sayfa İşlemi
type: docs
weight: 30
url: /tr/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Aspose.Cells for Node.js via C++ kullanarak, yazdırılacak bir şey olmadığında çıktı PDF sinde boş sayfaların oluşmasını nasıl önleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyası boşsa ve kullanıcı bunu Aspose.Cells for Node.js via C++ kullanarak PDF'ye kaydederse, çıktı PDF'sinde boş bir sayfa gösterilir. Bazen bu varsayılan davranış istenmeyebilir. Aspose.Cells, bu sorunla başa çıkmak için `[**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--)` özelliği sağlar. Bunu **false** yaparsanız, hiçbir şey yazdırılmadığında istisna oluşur.

## **Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur ve [**PdfSaveOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOutputBlankPageWhenNothingToPrint--) özelliğini **false** olarak ayarladıktan sonra PDF olarak kaydeder. Çıktı PDF'sinde yazdırılacak bir şey olmadığından, aşağıdaki gibi istisna oluşur.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Create Pdf save options.
const opts = new AsposeCells.PdfSaveOptions();

// Default value of OutputBlankPageWhenNothingToPrint is true.
// Setting false means - Do not output blank page when there is nothing to print.
opts.setOutputBlankPageWhenNothingToPrint(false);

// Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
const ms = new Uint8Array();

try {
// Save to Pdf format. It will throw exception.
wb.save(ms, opts);
} catch (ex) {
console.error("Exception Message: " + ex.message + "\r\n");
}
```

## **İstisna**

{{< highlight javascript >}}

 exception was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
