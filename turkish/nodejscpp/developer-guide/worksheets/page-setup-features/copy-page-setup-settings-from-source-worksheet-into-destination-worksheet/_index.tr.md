---
title: Kaynak çalışma sayfasından Hedef çalışma sayfasına Sayfa Ayarlarını kopyala Node.js ve C++ ile
linktitle: Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala
type: docs
weight: 80
url: /tr/nodejs-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Bu makale, Node.js API veya C++ Kütüphane örnek kodunu kullanarak bir kaynak çalışma sayfasından bir hedef çalışma sayfasına Sayfa Ayarlarını programatik olarak nasıl kopyalayacağınızı açıklar.
keywords: Kopyala sayfa ayarları Node.js ve C++ aracılığıyla
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabına yeni bir sayfa eklediğinizde, varsayılan *Sayfa Kurulumu ayarları* içerir. Bazen, ([**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup)) ayarlarını bir çalışma sayfasından diğerine aktarmanız gerekebilir. Bu belge, Aspose.Cells for Node.js via C++ API'leri kullanarak bir çalışma sayfasından diğerine Sayfa Kurulumu ayarlarını nasıl kopyalayacağınızı açıklar.

## **Kaynak Çalışma Sayfasından Hedef Çalışma Sayfasına Sayfa Ayarı Ayarlarını Kopyala**

Aşağıdaki örnek kod, [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#copy-pagesetup-copyoptions-) yöntemini kullanarak bir çalışma sayfasındaki *Sayfa Ayarı ayarlarını* diğerine kopyalamanın örneklerini göstermektedir. Lütfen örnek kodu ve konsol çıktısını referans için inceleyin.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook
const wb = new AsposeCells.Workbook();

// Add two test worksheets
wb.getWorksheets().add("TestSheet1");
wb.getWorksheets().add("TestSheet2");

// Access both worksheets as TestSheet1 and TestSheet2
const TestSheet1 = wb.getWorksheets().get("TestSheet1");
const TestSheet2 = wb.getWorksheets().get("TestSheet2");

// Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
TestSheet1.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3ExtraTransverse);

// Print the Paper Size of both worksheets
console.log("Before Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("Before Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();

// Copy the PageSetup from TestSheet1 to TestSheet2
TestSheet2.getPageSetup().copy(TestSheet1.getPageSetup(), new AsposeCells.CopyOptions());

// Print the Paper Size of both worksheets
console.log("After Paper Size: " + TestSheet1.getPageSetup().getPaperSize());
console.log("After Paper Size: " + TestSheet2.getPageSetup().getPaperSize());
console.log();
```

## **Konsol Çıktısı**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
