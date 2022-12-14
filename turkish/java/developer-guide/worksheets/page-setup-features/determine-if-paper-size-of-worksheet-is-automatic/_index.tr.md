---
title: Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme
type: docs
weight: 20
url: /tr/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Olası Kullanım Senaryoları**

 Çoğu zaman, çalışma sayfasının kağıt boyutu otomatiktir. Otomatik olduğunda, genellikle şu şekilde ayarlanır:*Mektup* . Bazen kullanıcı, çalışma sayfasının kağıt boyutunu gereksinimlerine göre ayarlar. Bu durumda, kağıt boyutu otomatik değildir. Çalışma sayfası kağıt boyutunun otomatik olup olmadığını veya[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)yöntem.

## **Çalışma Sayfasının Kağıt Boyutunun Otomatik olup olmadığını belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını öğrenin. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını bu ekran görüntüsünde gösterildiği gibi Sayfa Yapısı penceresinden kontrol edebilirsiniz.

![yapılacaklar:resim_alternatif_Metin](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsol Çıkışı**

Verilen örnek Excel dosyalarıyla çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı aşağıdadır.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
