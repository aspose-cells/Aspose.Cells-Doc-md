---
title: Cell Referansına göre bir Resim Ekleme
type: docs
weight: 90
url: /tr/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Bazen boş bir resminiz olur ve formül çubuğunda bir hücre referansı ayarlayarak resimdeki verileri veya içeriği göstermeniz gerekir. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).

{{% /alert %}}

## Cell Referansına Göre Resim Ekleme

Aspose.Cells, bir çalışma sayfası hücresinin içeriğinin görüntü şeklinde görüntülenmesini destekler. Resmi, görüntülemek istediğiniz verileri içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı grafik nesnesine bağlı olduğundan, verilerde yapılan değişiklikler otomatik olarak grafik nesnesinde görünür. çağırarak çalışma sayfasına bir resim ekleyin.[**resim Ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) yöntemi[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) koleksiyon (kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesne). kullanarak hücre aralığını belirtin.[**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) yöntemi[**Resim**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)nesne.

Aşağıda, aşağıdaki kodun oluşturduğu dosyanın ekran görüntüsü verilmiştir.

**Hücre referansına dayalı bir resim ekleme**

![yapılacaklar:resim_alternatif_Metin](insert-a-picture-based-on-cell-reference_1.png)

## Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
