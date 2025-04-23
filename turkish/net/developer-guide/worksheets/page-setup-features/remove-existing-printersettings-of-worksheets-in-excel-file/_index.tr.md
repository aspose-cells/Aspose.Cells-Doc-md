---
title: Excel dosyasındaki Çalışma Sayfalarının Mevcut Yazıcı Ayarlarını Kaldır
type: docs
weight: 60
url: /tr/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: Bu makalede, C# API veya .NET Kütüphanesi kullanarak sayfa ayar nesnesi ile programlı olarak Excel dosyası içindeki Çalışma Sayfasının mevcut Yazıcı Ayarlarını nasıl kaldıracağınızı öğreneceksiniz.
keywords: c# ile çalışma sayfası yazıcı ayarlarını kaldırma, excel çalışma sayfası yazıcı ayarlarını kaldırma
---

## **Olası Kullanım Senaryoları**
Bazı geliştiriciler, Excel'in kaydedilen XLSX dosyalarında yazıcı ayarlarındaki *.bin* dosyalarını önlemek isteyebilir. Yazıcı ayarları dosyaları, *“[file "root"]\xl\printerSettings”* altında bulunur. Bu belge, Aspose.Cells API'lerini kullanarak mevcut yazıcı ayarlarını nasıl kaldıracağınızı açıklar.
## **Excel dosyasındaki Mevcut Çalışma Sayfası Yazıcı Ayarlarını Kaldırma**
Aspose.Cells, Excel dosyasındaki farklı sayfalarda belirtilen mevcut yazıcı ayarlarını kaldırmanıza izin verir. Aşağıdaki örnek kod, çalışma kitabındaki tüm çalışma sayfaları için mevcut yazıcı ayarlarını kaldırmanın nasıl yapıldığını göstermektedir. Lütfen [örnek Excel dosyasını](45056020.xlsx), [çıktı Excel dosyasını](45056021.xlsx), konsol çıktısını ve referans için ekran görüntüsünü görün.
## **Ekran Görüntüsü**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
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
{{< app/cells/assistant language="csharp" >}}
