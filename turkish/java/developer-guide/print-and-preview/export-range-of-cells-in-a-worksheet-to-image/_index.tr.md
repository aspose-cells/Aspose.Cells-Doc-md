---
title: Çalışma Sayfasındaki Cells Aralığını Görüntüye Dışa Aktar
type: docs
weight: 130
url: /tr/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells'i kullanarak bir çalışma sayfasının görüntüsünü oluşturabilirsiniz. Ancak, bazen bir çalışma sayfasındaki yalnızca bir hücre aralığını bir görüntüye aktarmanız gerekir. Bu makalede, bunun nasıl başarılacağı açıklanmaktadır.

{{% /alert %}}

 Bir aralığın görüntüsünü çekmek için, baskı alanını istenen aralığa ayarlayın ve ardından tüm kenar boşluklarını 0 olarak ayarlayın.[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) ile**doğru**.

Aşağıdaki kod, E8:H10 aralığının bir görüntüsünü alır. Aşağıda, kodda kullanılan kaynak çalışma kitabının ekran görüntüsü verilmiştir. Kodu herhangi bir çalışma kitabıyla deneyebilirsiniz.

**Giriş dosyası**

![yapılacaklar:resim_alternatif_metin](export-range-of-cells-in-a-worksheet-to-image_1.png)

Kodun çalıştırılması, yalnızca E8:H10 aralığının bir görüntüsünü oluşturur.

**Çıktı görüntüsü**

![yapılacaklar:resim_alternatif_metin](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 yazısını da bulabilirsiniz[Çalışma Sayfasını Farklı Görüntü Formatlarına Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/) yardımsever.
