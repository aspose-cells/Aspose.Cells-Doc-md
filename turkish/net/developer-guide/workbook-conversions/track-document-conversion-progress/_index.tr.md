---
title: Belge Dönüşüm İlerlemesini İzle
type: docs
weight: 970
url: /tr/net/track-document-conversion-progress/
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda büyük excel dosyalarını dönüştürmek biraz zaman alabilir. Bu süre zarfında, sadece bir yükleme ekranı yerine doküman dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) arayüzünü sağlayarak döküman dönüşüm sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback) arayüzü, özel sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving) ve [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving) metotlarını sağlar. Ayrıca hangi sayfaların nasıl işlendiğini kontrol edebilirsiniz, T*estPageSavingCallback* özel sınıfında gösterildiği gibi.

## **Belge Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak excel dosyasını](94896151.xlsx) yükler ve *TestPageSavingCallback* özel sınıfını kullanarak konsolda dönüşüm ilerlemesini yazdırır.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

Aşağıdaki kod *TestPageSavingCallback* özel sınıf için olan kodu içerir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
