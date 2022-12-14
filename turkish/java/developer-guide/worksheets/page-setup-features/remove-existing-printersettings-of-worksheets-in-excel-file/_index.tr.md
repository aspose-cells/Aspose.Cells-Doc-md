---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 40
url: /tr/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Olası Kullanım Senaryoları**
Bazen geliştiriciler, Excel'in dahil edilmesini engellemek ister.*.çöp Kutusu* kaydedilen XLSX dosyalarındaki yazıcı ayarları dosyaları. Yazıcı ayarları dosyaları altında bulunur*“[dosya "root"]\xl\printerSettings”*. Bu belge, Aspose.Cells API'leri kullanılarak mevcut yazıcı ayarlarının nasıl kaldırılacağını açıklar.
## **Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır**
Aspose.Cells, Excel dosyasındaki farklı sayfalar için belirtilen mevcut yazıcı ayarlarını kaldırmanıza olanak tanır. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için varolan yazıcı ayarlarının nasıl kaldırılacağını gösterir. Lütfen bakın[örnek excel dosyası](45056023.xlsx), [çıktı excel dosyası](45056024.xlsx)konsol çıktısının yanı sıra referans için bir ekran görüntüsü.
## **Ekran görüntüsü**
![yapılacaklar:resim_alternatif_Metin](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Konsol Çıkışı**
{{< highlight "java" >}}

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
