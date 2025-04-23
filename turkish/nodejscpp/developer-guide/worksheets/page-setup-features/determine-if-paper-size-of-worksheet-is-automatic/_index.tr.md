---
title: Node.js ile C++ kullanarak Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme
linktitle: Çalışma Sayfasının Kağıt Boyutunun Otomatik Olup Olmadığını Belirleyin
type: docs
weight: 90
url: /tr/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Bu makale, C++ eklentileri ile Node.js API sini kullanarak bir çalışma sayfasının kağıt boyutunun otomatik olarak ayarlandığını programlı olarak nasıl belirleyeceğinizi açıklar.
keywords: çalışma sayfasının kağıt boyutunun otomatik olup olmadığını Node.js ve C++ kullanarak belirleme
---

## **Olası Kullanım Senaryoları**

Çoğu zaman, çalışma sayfasının kağıt boyutu otomatik olur. Otomatik olduğunda, genellikle *Letter* olarak ayarlanır. Bazen kullanıcı, gereksinimlerine göre çalışma sayfasının kağıt boyutunu ayarlar. Bu durumda, kağıt boyutu otomatik değildir. Çalışma sayfası kağıt boyutunun otomatik olup olmadığını [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--) özelliği ile bulabilirsiniz.

## **Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını bulur. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını Sayfa Ayarı penceresinden kontrol edebilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Konsol Çıktısı**

Verilen örnek Excel dosyaları ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı işte böyle olur.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
