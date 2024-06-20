---
title: ResimOluşturYazdırOptions ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfaların Sıralı Olarak Görüntülenmesi
type: docs
weight: 100
url: /tr/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Olası Kullanım Senaryoları**

Belirli bir çalışma dosyasının sayfalarının sıralı olarak [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) ve [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount) özellikleri ile Aspose.Cells kullanarak resimlere dönüştürülmesi mümkündür. Bu özellikler, çalışma sayfanızda binlerce gibi çok fazla sayfa bulunsa da sadece bazılarını dönüştürmek istediğinizde kullanışlıdır. Bu sadece işleme zamanını değil, aynı zamanda dönüştürme işleminin bellek tüketimini de kaydedecektir.

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](55541812.xlsx) yükler ve sadece 4, 5, 6 ve 7 sayfaları kullanarak [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) ve [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount) özelliklerini kullanarak oluşturulan sayfaları oluşturur. İşte kod tarafından oluşturulan renderlenmiş sayfalar.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}
