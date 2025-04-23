---
title: Çalışma Sayfasının Kağıt Boyutunun Otomatik Olup Olmadığını Belirleyin
type: docs
weight: 20
url: /tr/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Olası Kullanım Senaryoları**

Çoğu zaman, çalışma sayfasının kağıt boyutu otomatiktir. Otomatik olduğunda genellikle *Letter* olarak ayarlanır. Kullanıcı bazen kağıt boyutunu kendi gereksinimlerine göre ayarlar. Bu durumda, kağıt boyutu otomatik olmaz. Çalışma sayfasının kağıt boyutunun otomatik olup olmadığını [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) yöntemini kullanarak kontrol edebilirsiniz.

## **Çalışma Sayfasının Kağıt Boyutunu Otomatik Olup Olmadığını Belirleme**

Aşağıda verilen örnek kod, aşağıdaki iki Excel dosyasını yükler

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

ve ilk çalışma sayfasının kağıt boyutunun otomatik olup olmadığını bulur. Microsoft Excel'de, kağıt boyutunun otomatik olup olmadığını Sayfa Ayarı penceresinden kontrol edebilirsiniz, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsol Çıktısı**

Verilen örnek Excel dosyaları ile çalıştırıldığında yukarıdaki örnek kodun konsol çıktısı işte böyle olur.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
