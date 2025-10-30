---
title: Yeniden Numune Eklenmiş Resimler  Node.js kullanarak Excel den PDF ye Dönüştürme
linktitle: Yeniden Numune Eklenmiş Resimler
type: docs
weight: 150
url: /tr/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: PDF boyutunu azaltmak ve dönüştürme performansını artırmak için Excel dosyalarına eklenen resimleri nasıl sıkıştıracağınızı öğrenin Aspose.Cells for Node.js via C++ kullanarak.
---

{{% alert color="primary" %}}

 Çok sayıda resim içeren büyük Microsoft Excel dosyalarıyla çalışırken, çıktı PDF dosya boyutunu küçültmek ve genel dönüştürme performansını artırmak için eklenen resimleri sıkıştırmanız gerekebilir. Aspose.Cells for Node.js via C++, eklenen resimleri yeniden örnekleyerek çıktı PDF dosya boyutunu azaltmaya ve performansı biraz artırmaya destek sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

[**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) seçeneği kullanmak, çıktı PDF'sinin boyutunu minimize eder, ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
