---
title: Sayfa Sayısını Sınırla  Excel’den PDF’ye Dönüşüm ile Node.js kullanarak C++
linktitle: Oluşturulan Sayfa Sayısını Sınırlandır  Excel den PDF ye Dönüşüm
type: docs
weight: 180
url: /tr/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.Cells for Node.js via C++ kullanarak bir Excel tablosunun PDF’ye dönüştürülürken kaç sayfa üretileceğini sınırlandırmayı öğrenin. 
---

{{% alert color="primary" %}}

Bazen, belirli sayfa aralıklarını çıktı PDF dosyasına yazdırmak isteyebilirsiniz. Aspose.Cells for Node.js via C++, bir Excel tablosunun PDF biçimine dönüştürülürken kaç sayfa üretileceğinde sınır koyma imkanı sağlar.

{{% /alert %}}

## **Oluşturulan Sayfa Sayısını Sınırlandırmak**

Aşağıdaki örnek, bir Microsoft Excel dosyasındaki (3 ve 4) sayfa aralığını PDF olarak nasıl oluşturacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

Eğer tablo formüller içeriyorsa, PDF’ye dönmeden önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) çağrısı en iyisidir. Böylece formüle bağlı değerler yeniden hesaplanır ve doğru değerler çıktı dosyasına yansıtılır.

{{% /alert %}}
