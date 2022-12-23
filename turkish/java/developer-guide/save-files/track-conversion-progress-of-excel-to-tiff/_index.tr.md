---
title: Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin
type: docs
weight: 140
url: /tr/java/track-conversion-progress-of-excel-to-tiff/
---
## **Olası Kullanım Senaryoları**

Bazen büyük excel dosyalarının dönüştürülmesi biraz zaman alabilir. Bu süre zarfında, uygulamanızın kullanılabilirliğini artırmak için yalnızca bir yükleme ekranı yerine belge dönüştürme ilerlemesini göstermek isteyebilirsiniz. Aspose.Cells, aşağıdakileri sağlayarak izleme belgesi dönüştürme sürecini destekler:**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz. bu**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz sağlar**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**ve**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** özel sınıfınızda uygulayabileceğiniz yöntemler. Ayrıca, aşağıda gösterildiği gibi hangi sayfaların oluşturulacağını da kontrol edebilirsiniz.*TestTiffPageSavingCallback*özel sınıf

## **Excel'in TIFF'e Dönüştürme İlerlemesini İzleyin**

Aşağıdaki kod örneği,[kaynak excel dosyası](sampleUseWorkbookRenderForImageConversion.xlsx) kullanarak dönüştürme ilerlemesini konsolda yazdırır.*TestTiffPageSavingCallback*uygulayan özel sınıf**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**arayüz. Oluşturulan çıktı dosyası, referansınız için eklenmiştir.

[Çıktı dosyası](DocumentConversionProgressForTiff_out.tiff)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

için kod aşağıdadır*TestTiffPageSavingCallback*özel sınıf

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

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
Kaydetmeyi sonlandır sayfa dizini 8 sayfa 10
