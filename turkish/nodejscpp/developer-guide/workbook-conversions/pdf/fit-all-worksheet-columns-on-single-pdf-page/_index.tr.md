---
title: Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdırın (Node.js C++) ile
linktitle: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışsayfanın tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak isteyebilirsiniz. [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) özelliği bu özelliği çok kullanışlı bir şekilde sağlar. Çıktı PDF'in yükseklik ve genişliği gibi karmaşık hesaplamalar dahili olarak işlenir ve çalışsayfadaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) tüm çalışma sayfasındaki sütunların, veri miktarına bağlı olarak satırların birkaç sayfaya yayılması olmasına rağmen, tek bir PDF sayfasında gösterilmesini sağlar.

Aşağıdaki örnek kod, 100 sütunu olan büyük bir çalışsayfayı render etmek için [**PdfSaveOptions.getAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getAllColumnsInOnePagePerSheet--) özelliğini nasıl kullanacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create and initialize an instance of Workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Create and initialize an instance of PdfSaveOptions
const saveOptions = new AsposeCells.PdfSaveOptions();
// Set AllColumnsInOnePagePerSheet to true
saveOptions.setAllColumnsInOnePagePerSheet(true);
// Save Workbook to PDF format by passing the object of PdfSaveOptions
const outputFilePath = path.join(dataDir, "output.out.pdf");
workbook.save(outputFilePath, saveOptions);
```

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
