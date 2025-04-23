---
title: Excel den TIFF e Dönüşüm İlerlemesini İzle
type: docs
weight: 190
url: /tr/net/track-conversion-progress-of-excel-to-tiff/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda büyük excel dosyalarını dönüştürmek biraz zaman alabilir. Bu süre zarfında, sadece bir yükleme ekranı yerine doküman dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) arayüzünü sağlayarak döküman dönüşüm sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) arayüzü, özel sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) ve [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) metotlarını sağlar. Ayrıca hangi sayfaların nasıl işlendiğini kontrol edebilirsiniz, T*estPageSavingCallback* özel sınıfında gösterildiği gibi.

## **Excel'den TIFF'e Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak excel dosyasını](95584311.xlsx) yükler ve dönüşüm ilerlemesini konsolda *TestPageSavingCallback* özel sınıfını kullanarak yazdırır. Oluşturulan çıktı dosyası referans için eklenmiştir.

[Output File](95584312.tiff)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Aşağıdaki kod *TestTiffPageSavingCallback* özel sınıf için olan kodu içerir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
End saving page index 8 of pages 10</br>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
