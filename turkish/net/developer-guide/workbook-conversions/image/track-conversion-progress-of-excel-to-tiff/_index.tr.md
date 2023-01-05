---
title: Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin
type: docs
weight: 190
url: /tr/net/track-conversion-progress-of-excel-to-tiff/
---
## **Olası Kullanım Senaryoları**

 Bazen büyük excel dosyalarının dönüştürülmesi biraz zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, aşağıdakileri sağlayarak izleme belgesi dönüştürme sürecini destekler:**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** arayüz. bu**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**arayüz sağlar**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**ve**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**özel sınıfınızda uygulayabileceğiniz yöntemler. T'de gösterildiği gibi hangi sayfaların oluşturulacağını da kontrol edebilirsiniz.*estPageSavingCallback*özel sınıf

## **Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin**

 Aşağıdaki kod örneği,[kaynak excel dosyası](95584311.xlsx) kullanarak dönüştürme ilerlemesini konsolda yazdırır.*TestPageSavingCallback* uygulayan özel sınıf**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**arayüz. Oluşturulan çıktı dosyası, referansınız için eklenmiştir.

[Çıktı dosyası](95584312.tiff)

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

için kod aşağıdadır*TestTiffPageSavingCallback*özel sınıf

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **Konsol Çıkışı**

10. sayfanın 0. sayfa dizinini kaydetmeye başla</br>
10. sayfaların sayfa dizini 0'ı kaydetmeyi sonlandır</br>
10. sayfanın 1. sayfasını kaydetmeye başla</br>
10. sayfanın 1. sayfa indeksini kaydetmeyi sonlandır</br>
10. sayfanın 2. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa indeksi 2 sayfa 10</br>
10. sayfanın 3. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa indeksi 3 sayfa 10</br>
10. sayfanın 4. sayfa dizinini kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 4 sayfa 10</br>
10. sayfanın 5. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 5 sayfa 10</br>
10. sayfanın 6. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa indeksi 6 sayfa 10</br>
10. sayfanın 7. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 7 / sayfa 10</br>
10. sayfanın 8. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 8 sayfa 10</br>

