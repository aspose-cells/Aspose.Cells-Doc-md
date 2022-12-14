---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 60
url: /tr/net/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Olası Kullanım Senaryoları**
Bazen geliştiriciler, Excel'in dahil edilmesini engellemek ister.*.çöp Kutusu* kaydedilen XLSX dosyalarındaki yazıcı ayarları dosyaları. Yazıcı ayarları dosyaları altında bulunur*“[dosya "root"]\xl\printerSettings”.* Bu belge, Aspose.Cells API'leri kullanılarak mevcut yazıcı ayarlarının nasıl kaldırılacağını açıklar.
## **Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır**
Aspose.Cells, Excel dosyasındaki farklı sayfalar için belirtilen mevcut yazıcı ayarlarını kaldırmanıza olanak tanır. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için varolan yazıcı ayarlarının nasıl kaldırılacağını gösterir. Lütfen bakın[örnek excel dosyası](45056020.xlsx), [çıktı excel dosyası](45056021.xlsx), konsol çıktısı ve referans için ekran görüntüsü.
## **Ekran görüntüsü**
![yapılacaklar:resim_alternatif_Metin](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Konsol Çıkışı**
{{< highlight "java" >}}

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
