---
title: ResimOluşturYazdırOptions ın PageIndex ve PageCount Özelliklerini Kullanarak Sayfaların Sıralı Olarak Görüntülenmesi
type: docs
weight: 110
url: /tr/python-net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/

---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET ile [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) ve [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count) özelliklerini kullanarak Excel dosyanızın bir sayfa dizisini görselleştirebilirsiniz. Bu özellikler, çalışma sayfanızda binlerce sayfa olsa bile sadece bazılarını render etmek istediğinizde kullanışlıdır. Bu, işlem süresini ve render işleminin bellek tüketimini tasarruf edecektir.

## **Görüntü veya Yazdırma Seçenekleri Kullanılarak Sayfa Dizisi Oluşturma**

Aşağıdaki örnek kod, [**ImageOrPrintOptions.page_index**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_index) ve [**ImageOrPrintOptions.page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/page_count) özelliklerini kullanarak örnek Excel dosyasını yükler ve yalnızca 4, 5, 6 ve 7 sayfaları oluşturur. İşte kod tarafından oluşturulan sayfaların oluşturulmuş görüntüleri.

|![todo:image_alt_text](1)|![todo:image_alt_text](2)|
| :- | :- |
|![todo:image_alt_text](3)|![todo:image_alt_text](4)|

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RenderLimitedNoOfSequentialPages-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
