---
title: Belge Dönüştürme İlerlemesini İzleme
type: docs
weight: 970
url: /tr/net/track-document-conversion-progress/
---
## **Olası Kullanım Senaryoları**

 Bazen büyük excel dosyalarının dönüştürülmesi biraz zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, aşağıdakileri sağlayarak izleme belgesi dönüştürme sürecini destekler:**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** arayüz. bu**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**arayüz sağlar**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**ve**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**özel sınıfınızda uygulayabileceğiniz yöntemler. T'de gösterildiği gibi hangi sayfaların oluşturulacağını da kontrol edebilirsiniz.*estPageSavingCallback*özel sınıf

## **Belge Dönüştürme İlerlemesini İzleme**

 Aşağıdaki kod örneği,[kaynak excel dosyası](94896151.xlsx) kullanarak dönüştürme ilerlemesini konsolda yazdırır.*TestPageSavingCallback* uygulayan özel sınıf**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**arayüz.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

için kod aşağıdadır*TestPageSavingCallback*özel sınıf

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

## **Konsol Çıkışı**

11. sayfaların 0. sayfa dizinini kaydetmeye başlayın</br>
11. sayfaların sayfa dizini 0'ı kaydetmeyi sonlandır</br>
11. sayfanın 1. sayfasını kaydetmeye başla</br>
11. sayfaların 1. sayfa indeksini kaydetmeyi sonlandır</br>
11. sayfanın 2. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa indeksi 2 sayfa 11</br>
Sayfa 11'in sayfa dizini 3'ü kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa indeksi 3 sayfa 11</br>
11. sayfanın 4. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 4 sayfa 11</br>
11. sayfanın 5. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 5 sayfa 11</br>
11. sayfanın 6. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 6 sayfa 11</br>
11. sayfanın 7. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 7 / sayfalar 11</br>
11. sayfanın 8. sayfasını kaydetmeye başla</br>
Kaydetmeyi sonlandır sayfa dizini 8 sayfa 11
