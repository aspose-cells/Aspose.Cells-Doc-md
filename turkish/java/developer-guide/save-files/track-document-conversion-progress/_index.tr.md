---
title: Belge Dönüştürme İlerlemesini İzleme
type: docs
weight: 120
url: /tr/java/track-document-conversion-progress/
---
## **Olası Kullanım Senaryoları**

Bazen büyük excel dosyalarının dönüştürülmesi biraz zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, aşağıdakileri sağlayarak izleme belgesi dönüştürme sürecini destekler:**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz. bu**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz sağlar**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**ve**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** özel sınıfınızda uygulayabileceğiniz yöntemler. Ayrıca, aşağıda gösterildiği gibi hangi sayfaların oluşturulacağını da kontrol edebilirsiniz.*TestPageSavingCallback*özel sınıf

## **Belge Dönüştürme İlerlemesini İzleme**

Aşağıdaki kod örneği,[kaynak excel dosyası](PagesBook1.xlsx)kullanarak dönüştürme ilerlemesini konsolda yazdırır.*TestPageSavingCallback*uygulayan özel sınıf**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

için kod aşağıdadır*TestPageSavingCallback*özel sınıf

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

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
