---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 60
url: /tr/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Bu makalede, Aspose.Cells for Python Excel Kütüphanesi kullanarak Sayfa Düzeni nesnesi üzerinden Excel dosyasındaki Çalışma Sayfasının mevcut PrinterSettings ayarlarını programlı olarak nasıl kaldıracağınızı örnek kodlarla öğreneceksiniz.
keywords: Python Excel Kütüphanesi, Python ile çalışma sayfasının yazıcı ayarlarını kaldırma, Python ile Excel çalışma sayfasının yazıcı ayarlarını kaldırma.
---

## **Olası Kullanım Senaryoları**
Bazen geliştiriciler, Excel'in kaydedilen XLSX dosyalarına yazıcı ayarlarının *.bin* dosyalarını dahil etmesini engellemek ister. Yazıcı ayarları dosyaları "[file "root"]\xl\printerSettings" altındadır. Bu doküman, Aspose.Cells for Python via .NET API'leri kullanarak mevcut yazıcı ayarlarını nasıl kaldıracağınızı açıklar.

## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells for Python via .NET, Excel dosyasındaki farklı sayfalar için belirlenen mevcut yazıcı ayarlarını kaldırmanıza imkan tanır. Aşağıdaki örnek kod, çalışma kitabındaki tüm sayfalar için mevcut yazıcı ayarlarını nasıl kaldıracağınızı gösterir. Lütfen [örnek Excel dosyasına](45056020.xlsx), [çıktı Excel dosyasına](45056021.xlsx), konsol çıktısına ve ekran görüntüsüne bakınız.

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
{{< app/cells/assistant language="python-net" >}}
