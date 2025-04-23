---
title: Aspose.Cells te Özel XML Parçalarını Kullanma
type: docs
weight: 570
url: /tr/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Özel XML Parçaları, SharePoint vb. farklı uygulamalar tarafından excel dosyası içine saklanmış XML verileridir. Bu veri, ihtiyacı olan farklı uygulamalar tarafından tüketilir. Microsoft Excel bu veriyi kullanmadığından eklemek için GUI yoktur. Bu veriye **.xlsx** uzantısını **.zip** olarak değiştirip sonra **WinRAR** kullanarak açarak erişebilirsiniz. Veri, bu resimde gösterilen gibi **customXml** klasörü içindedir.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Aspose.Cells kullanarak özel XML parçaları ekleyebilirsiniz; bunun için [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) yöntemini kullanın.

{{% /alert %}} 
## **Aspose.Cells'te Özel XML Parçalarını Kullanma**
Aşağıdaki örnek kod, [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) yöntemini kullanır ve **Book Catalog Xml** adlı yapıya ekler, adı ise **BookStore**. Bu kodun sonucunu gösteren aşağıdaki görsel, Book Catalog Xml'in bu özelliğin adı olan BookStore düğümünün içine eklendiğini gösterir.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **İlgili Makale**
{{% alert color="primary" %}} 

- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
