---
title: Çalışma Sayfasındaki Hücre Aralığını Bir Görüntüye Aktarma
type: docs
weight: 130
url: /tr/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak bir çalışma sayfasının görüntüsünü alabilirsiniz. Ancak bazen, bir çalışma sayfasındaki yalnızca belirli bir hücre aralığını bir görüntüye aktarmanız gerekebilir. Bu makalede, bu işlemi nasıl gerçekleştireceğiniz açıklanmaktadır.

{{% /alert %}}

Bir aralığın görüntüsünü almak için, yazdırma alanını istenen aralık olarak ayarlayın ve ardından tüm kenar boşluklarını 0 olarak ayarlayın. Ayrıca, [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) özelliğini **true** olarak ayarlayın.

Aşağıdaki kod, E8:H10 aralığının bir görüntüsünü alır. Kodda kullanılan kaynak çalışma kitabının ekran görüntüsü aşağıda verilmiştir. Kodu istediğiniz çalışma kitabıyla deneyebilirsiniz.

**Giriş dosyası**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Kod çalıştırıldığında, yalnızca E8:H10 aralığının bir görüntüsü oluşturulur.

**Çıktı görüntüsü**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Ayrıca, [Farklı Görüntü Biçimlerine Çalışma Sayfasını Dönüştürme](/cells/tr/java/converting-worksheet-to-different-image-formats/) başlıklı makaleyi de faydalı bulabilirsiniz.
