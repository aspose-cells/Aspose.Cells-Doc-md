---
title: Excel den TIFF e Dönüşüm İlerleme Takibi, Golang ve C++ ile
linktitle: Excel den TIFF e Dönüşüm İlerlemesini İzle
type: docs
weight: 190
url: /tr/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for C++ kullanarak Excel dosyalarının TIFF formatına dönüşüm ilerlemesini nasıl takip edeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

 Bazen büyük Excel dosyalarını dönüştürmek zaman alabilir. Bu süre boyunca, uygulamanızın kullanılabilirliğini artırmak için yalnızca yükleme ekranı yerine döküman dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzünü sağlayarak belge dönüşüm ilerlemesini takip etmeyi destekler. [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzü, sizin özelleştirilmiş sınıfınızda uygulayabileceğiniz [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) ve [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/) metodlarını sağlar. Ayrıca, hangi sayfaların render edileceğini kontrol edebilirsiniz, bu da *TestPageSavingCallback* özel sınıfında gösterilmiştir.

## **Excel'den TIFF'e Dönüşüm İlerlemesini İzle**

 Aşağıdaki kod örneği, [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/) arayüzünü uygulayan *TestPageSavingCallback* özel sınıfını kullanarak kaydettiğiniz kaynak Excel dosyasını (95584311.xlsx) yükler ve konsolda dönüşüm ilerlemesini gösterir. Oluşturulan çıktı dosyası örneğinize eklenmiştir.

[Output File](95584312.tiff)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Aşağıdaki kod *TestTiffPageSavingCallback* özel sınıf için olan kodu içerir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
