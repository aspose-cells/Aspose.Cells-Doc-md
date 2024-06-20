---
title: ResimOluşturYazdırOptions ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfaların Sıralı Olarak Görüntülenmesi
type: docs
weight: 10
url: /tr/python-java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**
Aspose.Cells ile Excel dosyanızın bir sayfa dizisini, [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) ve [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) özelliklerini kullanarak görüntülendirebilirsiniz. Bu özellikler, çalışsayıda binlerce sayfa olmasına rağmen sadece bazılarını görüntülemek istediğinizde kullanışlıdır. Bu, sadece işleme zamanını değil, aynı zamanda render işleminin bellek tüketimini de tasarruf edecektir.

Aşağıdaki örnek kod, örnek Excel dosyasını yükler ve yalnızca 4, 5, 6 ve 7 sayfalarını kullanarak [ImageOrPrintOptions.PageIndex](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageIndex) ve [ImageOrPrintOptions.PageCount](https://reference.aspose.com/cells/python/asposecells.api/imageorprintoptions#PageCount) özelliklerini kullanarak oluşturulan render sayfalarının görüntüleridir.

|![todo:image_alt_text](outputImage-4.png)|![todo:image_alt_text](outputImage-5.png)|
| :- | :- |
|![todo:image_alt_text](outputImage-6.png)|![todo:image_alt_text](outputImage-7.png)|



## **Örnek Kod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderLimitedNoOfSequentialPages.py" >}}
