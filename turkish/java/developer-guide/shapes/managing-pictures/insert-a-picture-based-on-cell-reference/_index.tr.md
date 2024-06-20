---
title: Hücre Referansına Göre Resim Ekle
type: docs
weight: 90
url: /tr/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Bazen boş bir resminiz vardır ve resimde verileri veya içeriği bir hücre referansı belirleyerek göstermek istersiniz. Aspose.Cells bu özelliği destekler (Microsoft Excel 2010).

{{% /alert %}}

## Hücre Referansına Dayalı Bir Resim Eklemek

Aspose.Cells, bir çalışma sayfası hücresinin içeriğini bir resim şeklinde görüntülemeyi destekler. Görsel nesneye bağlı olan hücreyi, göstermek istediğiniz veriyi içeren hücreye bağlayabilirsiniz. Hücre veya hücre aralığı, grafik nesnesine bağlandığından, veriye yapılan değişiklikler otomatik olarak grafik nesnesinde görünür hale gelir. Bir resmi çalışma sayfasına eklemek için [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) koleksiyonunun [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream)) yöntemini ( [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesine kapsüllenen) çağırarak yapabilirsiniz. Hücre aralığını, [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) nesnesinin [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) yöntemini kullanarak belirtin.

Aşağıda, aşağıdaki kodun oluşturduğu dosyanın ekran görüntüsü bulunmaktadır.

**Hücre başvurusuna dayalı bir resim ekleme**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
