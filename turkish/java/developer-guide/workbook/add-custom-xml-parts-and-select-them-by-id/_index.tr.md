---
title: Özel XML Bölümleri Ekleyin ve Kimliğe Göre Seçin
type: docs
weight: 10
url: /tr/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgelerinin içinde depolanan ve bunlarla ilgilenen uygulamalar tarafından kullanılan XML verileridir. Şu anda Microsoft Excel kullanıcı arabirimini kullanarak bunları eklemenin doğrudan bir yolu yoktur. Ancak, bunları çeşitli şekillerde programlı olarak ekleyebilirsiniz, örneğin kullanarak*VSTO*, kullanarak*Aspose.Cells*vb. lütfen kullanın[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) yöntemi, Aspose.Cells API'i kullanarak Özel XML Parçası eklemek istiyorsanız.[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)Emlak. Benzer şekilde, kimliğe göre Özel XML Parçası'nı seçmek isterseniz,[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) yöntem.

## **Özel XML Bölümleri Ekleyin ve Kimliğe Göre Seçin**

Aşağıdaki örnek kod, önce şunu kullanarak dört Özel XML Parçası ekler:[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) yöntem. Daha sonra kullanarak kimliklerini ayarladı[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)Emlak. Son olarak, kullanarak eklenen Özel XML Parçalarından birini bulur veya seçer.[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) yöntem. Lütfen referans için aşağıda verilen kodun konsol çıktısına da bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
