---
title: Golang ile C++ üzerinden Belge İşlem Takibi
linktitle: Belge Dönüşüm İlerlemesini İzle
type: docs
weight: 970
url: /tr/go-cpp/track-document-conversion-progress/
description: Aspose.Cells kullanarak C++ ta belge dönüşüm sürecini nasıl takip edeceğinizi öğrenin ve uygulama kullanılabilirliğini artırın.
---

## **Olası Kullanım Senaryoları**

Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre boyunca, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleniyor ekranı yerine belge dönüşüm ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzü sağlayarak belge dönüşüm sürecini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzü, uygulayacağınız [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) ve [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) metodlarını sunar. Ayrıca, `TestPageSavingCallback` özel sınıfında gösterildiği gibi, hangi sayfaların gösterileceğini de kontrol edebilirsiniz.

## **Belge Dönüşüm İlerlemesini İzle**

Aşağıdaki kod örneği, [kaynak Excel dosyasını](94896151.xlsx) yükler ve `TestPageSavingCallback` özel sınıfını kullanarak dönüşüm ilerlemesini konsolda yazdırır ve [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzünü uygular.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Aşağıdaki, `TestPageSavingCallback` özel sınıfının kodudur.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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
