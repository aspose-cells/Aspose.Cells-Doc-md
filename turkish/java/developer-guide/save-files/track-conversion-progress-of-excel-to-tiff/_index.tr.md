---
title: Excel den TIFF e Dönüşüm İlerlemesini İzle
type: docs
weight: 140
url: /tr/java/track-conversion-progress-of-excel-to-tiff/
---

## **Olası Kullanım Senaryoları**

Bazen büyük excel dosyalarını dönüştürmek biraz zaman alabilir. Bu süre içinde, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı değil, belge dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) arabirimini sağlayarak belge dönüşüm sürecini izlemenizi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) arabirimi, özel sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) ve [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) metodları sağlar. Ayrıca *TestTiffPageSavingCallback* özel sınıfında gösterildiği gibi hangi sayfaların işleneceğini kontrol edebilirsiniz.

## **Excel'den TIFF'e Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak excel dosyasını](sampleUseWorkbookRenderForImageConversion.xlsx) yükler ve *TestTiffPageSavingCallback* özel sınıfını uygulayarak dönüşüm ilerlemesini konsol üzerinde yazdırır. Oluşturulan çıktı dosyası referans için eklenmiştir.

[Çıktı Dosyası](DocumentConversionProgressForTiff_out.tiff)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Aşağıdaki kod *TestTiffPageSavingCallback* özel sınıf için olan kodu içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}
Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
