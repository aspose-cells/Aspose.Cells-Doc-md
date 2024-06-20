---
title: Belge Dönüşüm İlerlemesini İzle
type: docs
weight: 120
url: /tr/java/track-document-conversion-progress/
---

## **Olası Kullanım Senaryoları**

Bazen büyük excel dosyalarını dönüştürmek biraz zaman alabilir. Bu süre içinde, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı değil, belge dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) arabirimini sağlayarak belge dönüşüm sürecini izlemenizi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) arabirimi, özel sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs)) ve [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs)) metodları sağlar. Ayrıca *TestPageSavingCallback* özel sınıfında gösterildiği gibi hangi sayfaların işleneceğini kontrol edebilirsiniz.

## **Belge Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği [kaynak excel dosyasını](PagesBook1.xlsx) yükle ve *TestPageSavingCallback* özel sınıfını uygulayarak dönüşüm ilerlemesini konsol üzerinde yazdır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Aşağıdaki kod *TestPageSavingCallback* özel sınıf için olan kodu içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
