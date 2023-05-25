---
title: Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme
type: docs
weight: 90
url: /tr/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Bu makalede, Çalışma Sayfasının Kağıt Boyutunun otomatik olup olmadığını belirlemek için C# API veya .NET Kitaplık örnek kodunun nasıl kullanılacağı açıklanmaktadır.
keywords: determine if paper size of worksheet automatic c#
---
##  **Olası Kullanım Senaryoları**

 Çoğu zaman, çalışma sayfasının kağıt boyutu otomatiktir. Otomatik olduğunda, genellikle *Harf* olarak ayarlanır. Bazen kullanıcı, çalışma sayfasının kağıt boyutunu gereksinimlerine göre ayarlar. Bu durumda, kağıt boyutu otomatik değildir. Çalışma sayfası kağıt boyutunun otomatik olup olmadığını veya[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)mülk.

##  **Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını öğrenin. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını bu ekran görüntüsünde gösterildiği gibi Sayfa Yapısı penceresinden kontrol edebilirsiniz.

![yapılacaklar:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

##  **Konsol Çıkışı**

Verilen örnek Excel dosyalarıyla çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
