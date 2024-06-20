---
title: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 10
url: /tr/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgeleri içinde depolanan ve onlarla başa çıkan uygulamalar tarafından kullanılan XML verileridir. Şu anda Microsoft Excel UI'nin bunları doğrudan eklemenin bir yolu yok. Ancak, bunları programlı olarak çeşitli yollarla ekleyebilirsiniz, örneğin *VSTO*, *Aspose.Cells* kullanarak vb. Aspose.Cells API'sını kullanarak Özel XML Parçası eklemek istiyorsanız lütfen [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) yöntemini kullanın. Aynı şekilde, ID'sini ayarlamak istiyorsanız, [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) özelliğini kullanın. Benzer şekilde, ID'ye göre Özel XML Parçasını seçmek istiyorsanız, [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) yöntemini kullanabilirsiniz.

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**

Aşağıdaki örnek kod önce [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) yöntemini kullanarak dört Özel XML Parçası ekler. Daha sonra, ID'lerini [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID) özelliğini kullanarak ayarlar. Son olarak, eklenen Özel XML Parçalarından birini bulur veya seçer [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) yöntemini kullanarak. Ayrıca aşağıdaki verilen kodun konsol çıktısını da referans için inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
