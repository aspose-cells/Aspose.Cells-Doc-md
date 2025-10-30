---
title: Çalışma Sayfasının Kağıt Boyutunun Otomatik Olup Olmadığını Belirleyin
type: docs
weight: 90
url: /tr/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: Bu makale, Aspose.Cells for Python via .NET örnek kodunu kullanarak, Sayfa Boyutunun Otomatik olup olmadığını programatik olarak belirlemenin yollarını anlatır.
keywords: Python Excel Kütüphanesi, Python ile sayfa boyutunun otomatik olup olmadığını belirle.
---

## **Olası Kullanım Senaryoları**

Çoğu zaman çalışma sayfasının kağıt boyutu otomatiktir. Otomatik olduğunda genellikle *Mektup* olarak ayarlanır. Kullanıcı bazen kağıt boyutunu gereksinimlerine göre ayarlar. Bu durumda kağıt boyutu otomatik değildir. Çalışma sayfasının kağıt boyutunun otomatik olup olmadığını [**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/) özelliğini kullanarak bulabilirsiniz.

## **Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını bulur. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını Sayfa Ayarı penceresinden kontrol edebilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **Konsol Çıktısı**

Verilen örnek Excel dosyaları ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı işte böyle olur.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
