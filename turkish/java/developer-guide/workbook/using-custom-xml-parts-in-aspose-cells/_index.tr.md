---
title: Aspose.Cells'de Özel XML Parçalarını Kullanma
type: docs
weight: 570
url: /tr/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Özel XML Parçaları, excel dosyası içinde SharePoint vb. farklı uygulamalar tarafından depolanan XML verileridir. Bu veriler, ona ihtiyaç duyan farklı uygulamalar tarafından tüketilir. Microsoft Excel bu verileri kullanmaz, bu nedenle eklenecek GUI yoktur. Uzantısını değiştirerek bu verileri görüntüleyebilirsiniz.**.xlsx** içine**.zip** ve sonra kullanarak açarak**WinRAR** . Veriler içinde mevcut**özelXml** Bu resimde gösterildiği gibi klasör.

![yapılacaklar:resim_alternatif_metin](using-custom-xml-parts-in-aspose-cells_1.png)

 Aspose.Cells'i kullanarak özel XML parçaları ekleyebilirsiniz.[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) yöntem.

{{% /alert %}} 
## **Aspose.Cells'de Özel Xml Parçalarını Kullanma**
 Aşağıdaki örnek kod,[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) yöntemi ve ekler**Kitap Kataloğu Xml** ve onun adı**Kitapçı**Aşağıdaki resimde bu kodun sonucu gösterilmektedir. Gördüğünüz gibi Book Catalog Xml, bu özelliğin adı olan BookStore düğümünün içine eklenir.

![yapılacaklar:resim_alternatif_metin](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **İlgili Makale**
{{% alert color="primary" %}} 

- [Belge Bilgileri Panelinde görünen Özel Özellikler ekleme](/cells/tr/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
