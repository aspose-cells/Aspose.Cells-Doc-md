---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 40
url: /tr/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Olası Kullanım Senaryoları**
Bazı durumlarda geliştiriciler, Excel'in kaydedilen XLSX dosyalarında *“.bin*” dosyalarını dahil etmesini istemeyebilir. Yazdırma ayarları dosyaları, *“[file "root"]\xl\printerSettings”* altında bulunmaktadır. Bu belge, Aspose.Cells API'leri kullanarak mevcut yazdırma ayarlarını nasıl kaldırılacağını açıklar.
## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells, Excel dosyasındaki farklı sayfalar için belirtilen mevcut yazdırma ayarlarını kaldırmanıza olanak tanır. Aşağıdaki örnek kod, çalışılan defterdeki tüm çalışma sayfaları için mevcut yazdırma ayarlarını nasıl kaldıracağını göstermektedir. Referans için lütfen örnek Excel dosyasını göz atın, [çıktı Excel dosyasını](45056024.xlsx), konsol çıktısını ve bir ekran görüntüsünü inceleyin.
## **Ekran Görüntüsü**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Konsol Çıktısı**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
