---
title: Node.js ve C++ kullanarak Çalışma Sayfasının Sayfa Kurulumu nun Genişlik ve Yüksekliğini Alma
linktitle: Çalışma Sayfası Sayfa Ayarları Kağıt Genişliğini ve Yüksekliğini Alma
type: docs
weight: 50
url: /tr/nodejs-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Node.js ve C++ kullanarak Excel Çalışma Sayfası Sayfa Kurulumu nun Kağıt Genişi ve Yüksekliğini programlı olarak nasıl alacağınızı keşfedin.
keywords: excel sayfa kurulumu kağıt genişliği Node.js ve C++ ile, excel sayfa kurulumu kağıt yüksekliği Node.js ve C++ ile
---

## **Olası Kullanım Senaryoları**

Bazen, çalışma sayfasının sayfa kurulumu içinde ayarlanmış olan kağıt boyutunun genişliğini ve yüksekliğini bilmeniz gerekir. Bu amaçla [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) ve [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) özelliklerini kullanın.

## **Çalışma Sayfası Sayfa Ayarları Kağıt Genişliği ve Yüksekliğini Alma**

Aşağıdaki örnek kod, [**PageSetup.getPaperWidth()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperWidth--) ve [**PageSetup.getPaperHeight()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPaperHeight--) özelliklerinin kullanımını açıklar. Önce kağıt boyutunu *A2* olarak değiştirir, ardından kağıdın genişlik ve yüksekliğini bulur, sonra sırasıyla *A3*, *A4*, *Letter* yapar ve kağıdın genişlik ve yüksekliğini bulur.

### **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create an instance of Workbook class
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Set paper size to A2 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA2);
console.log("PaperA2: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A3 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA3);
console.log("PaperA3: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to A4 and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
console.log("PaperA4: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());

// Set paper size to Letter and print paper width and height in inches
sheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperLetter);
console.log("PaperLetter: " + sheet.getPageSetup().getPaperWidth() + "x" + sheet.getPageSetup().getPaperHeight());
```

### **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
