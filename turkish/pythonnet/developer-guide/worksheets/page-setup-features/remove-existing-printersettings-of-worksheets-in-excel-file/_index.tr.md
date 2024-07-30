---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 60
url: /tr/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Bu makalede, Aspose.Cells for Python Excel Kitaplığı kullanarak Programlı olarak Excel dosyası içindeki Çalışma Sayfasının Mevcut Yazıcı Ayarlarını nasıl kaldıracağınızı öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python çalışma sayfasının yazıcı ayarlarını kaldır, Python excel çalışma sayfasının yazıcı ayarlarını kaldır.
---

## **Olası Kullanım Senaryoları**
Bazı geliştiriciler, Excel'in kaydedilen XLSX dosyalarında *.bin* dosyalarını içermesini istemez. Yazıcı ayarları dosyaları *“[file "root"]\xl\printerSettings”* altında bulunur. Bu belge, Aspose.Cells for Python via .NET API'larını kullanarak mevcut yazıcı ayarlarını nasıl kaldıracağınızı açıklar.

## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells for Python via .NET, Excel dosyasında farklı sayfalar için belirtilen mevcut yazıcı ayarlarını kaldırmanıza olanak tanır. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için mevcut yazıcı ayarlarını kaldırmanın nasıl yapıldığını gösterir.

## **Ekran Görüntüsü**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

## **Konsol Çıktısı**
{{< highlight java >}}

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
