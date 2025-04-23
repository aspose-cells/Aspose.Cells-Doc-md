---
title: ResimOluşturYazdırOptions ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfaların Sıralı Olarak Görüntülenmesi
type: docs
weight: 110
url: /tr/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Olası Kullanım Senaryoları**

Aspose.Cells ile Excel dosyanızın sayısız sayfaları olsa da bunlardan sadece bazılarını oluşturmak istiyorsanız, ImageOrPrintOptions'ın [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) ve [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount) özelliklerini kullanarak sayısal bir dizi oluşturabilirsiniz. Bu özellikler, iş sayfanızda çok fazla örneğin binlerce sayfa olsa da sadece bazılarını oluşturmak istiyorsanız faydalıdır. Bu, sadece işleme süresini değil aynı zamanda oluşturma sürecinin bellek tüketimini de kaydedecektir.

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**

Aşağıdaki örnek kod, [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pageindex) ve [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/pagecount) özelliklerini kullanarak örnek Excel dosyasını yükler ve yalnızca 4, 5, 6 ve 7 sayfaları oluşturur. İşte kod tarafından oluşturulan sayfaların oluşturulmuş görüntüleri.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4)|

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderLimitedNoOfSequentialPages-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
