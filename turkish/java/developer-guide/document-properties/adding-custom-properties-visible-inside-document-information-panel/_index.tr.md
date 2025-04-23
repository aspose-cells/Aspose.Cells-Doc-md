---
title: Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek
type: docs
weight: 500
url: /tr/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells, Belge Bilgi Paneli'nde görünen çalışma kitabı nesnesi içine özel özellikler eklemek için kullanılabilir. Microsoft Excel'de Belge Bilgi Paneli'ni Aç > Bilgi > Özellikler > Belgeyi Göster menü komutlarını kullanarak açabilirsiniz.

Lütfen Belge Bilgi Panelinde görünecek özel bir özellik eklemek için [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) yöntemini kullanın

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod, herhangi bir tipe sahip olmayan ilk özellik ve ikinci özelliğin tarih ve saat türüne sahip olduğu iki özel özellik ekler. Bu kodun oluşturduğu çıktı Excel dosyasını açtığınızda, bu iki özelliği Belge Bilgi Paneli içinde göreceksiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **İlgili Makale**

{{% alert color="primary" %}}

- [Aspose.Cells'te Özel XML Parçalarının Kullanımı](/cells/tr/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
