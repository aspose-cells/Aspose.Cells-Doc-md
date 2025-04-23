---
title: Var olan PrinterSettings leri Excel çalıştırma dosyasından kaldırmak için Node.js ve C++ kullanımı
linktitle: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 60
url: /tr/nodejs-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak, Excel dosyasındaki çalışma sayfasının mevcut PrinterSettings lerini programlı olarak nasıl kaldıracağınızı açıklar.
keywords: Node.js ve C++ kullanarak çalışma sayfasının yazıcı ayarlarını kaldırma
---

## **Olası Kullanım Senaryoları**
Bazı geliştiriciler, Excel'in kaydedilen XLSX dosyalarında yazıcı ayarlarındaki *.bin* dosyalarını önlemek isteyebilir. Yazıcı ayarları dosyaları, *“[file "root"]\xl\printerSettings”* altında bulunur. Bu belge, Aspose.Cells API'lerini kullanarak mevcut yazıcı ayarlarını nasıl kaldıracağınızı açıklar.

## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells, Excel dosyasındaki farklı sayfalarda belirtilen mevcut yazıcı ayarlarını kaldırmanıza izin verir. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için mevcut yazıcı ayarlarını kaldırmanın nasıl yapıldığını göstermektedir. Lütfen [örnek Excel dosyasını](45056020.xlsx), [çıktı Excel dosyasını](45056021.xlsx), konsol çıktısını ve referans için ekran görüntüsünü görün.

## **Ekran Görüntüsü**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Örnek Kod**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "sampleRemoveExistingPrinterSettingsOfWorksheets.xlsx");
const wb = new AsposeCells.Workbook(filePath);

// Get the sheet counts of the workbook
const sheetCount = wb.getWorksheets().getCount();

// Iterate all sheets
for (let i = 0; i < sheetCount; i++) {
// Access the i-th worksheet
const ws = wb.getWorksheets().get(i);

// Access worksheet page setup
const ps = ws.getPageSetup();

// Check if printer settings for this worksheet exist
if (ps.getPrinterSettings() != null) {
// Print the following message
console.log("PrinterSettings of this worksheet exist.");

// Print sheet name and its paper size
console.log("Sheet Name: " + ws.getName());
console.log("Paper Size: " + ps.getPaperSize());

// Remove the printer settings by setting them null
ps.setPrinterSettings(null);
console.log("Printer settings of this worksheet are now removed by setting it null.");
console.log("");
} // if
} // for

// Save the workbook
wb.save(path.join(outputDir, "outputRemoveExistingPrinterSettingsOfWorksheets.xlsx"));
```

## **Konsol Çıktısı**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
