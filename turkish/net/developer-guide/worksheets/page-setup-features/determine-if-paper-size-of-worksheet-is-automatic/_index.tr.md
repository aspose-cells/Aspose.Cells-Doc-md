---
title: Çalışma Sayfasının Kağıt Boyutunun Otomatik Olup Olmadığını Belirleyin
type: docs
weight: 90
url: /tr/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Bu makale, C# API veya .NET Kütüphanesi örnek kodunu kullanarak çalışma sayfasının kağıt boyutunun programlı olarak otomatik olup olmadığını belirlemenin nasıl yapıldığını açıklar.
keywords: c# ile sayfa boyutunu otomatikmi c# belirle, çalışma sayfasının kağıt boyutu otomatik mi c#
---

## **Olası Kullanım Senaryoları**

Çoğu zaman çalışma sayfasının kağıt boyutu otomatiktir. Otomatik olduğunda genellikle *Mektup* olarak ayarlanır. Kullanıcı bazen kağıt boyutunu gereksinimlerine göre ayarlar. Bu durumda kağıt boyutu otomatik değildir. Çalışma sayfasının kağıt boyutunun otomatik olup olmadığını [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize) özelliğini kullanarak bulabilirsiniz.

## **Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını bulur. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını Sayfa Ayarı penceresinden kontrol edebilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Konsol Çıktısı**

Verilen örnek Excel dosyaları ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı işte böyle olur.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
