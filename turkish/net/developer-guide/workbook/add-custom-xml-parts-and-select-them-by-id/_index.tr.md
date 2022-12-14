---
title: Özel XML Bölümleri Ekleyin ve Kimliğe Göre Seçin
type: docs
weight: 70
url: /tr/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgelerinin içinde depolanan ve bunlarla ilgilenen uygulamalar tarafından kullanılan XML verileridir. Şu anda Microsoft Excel kullanıcı arabirimini kullanarak bunları eklemenin doğrudan bir yolu yoktur. Ancak, bunları VSTO kullanarak, Aspose.Cells kullanarak vb. gibi çeşitli şekillerde programlı olarak ekleyebilirsiniz.[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)yöntemini kullanarak Özel XML Parçası eklemek istiyorsanız Aspose.Cells API'i kullanın.[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)Emlak. Benzer şekilde, kimliğe göre Özel XML Parçası'nı seçmek isterseniz,[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)yöntem.

## **Özel XML Bölümleri Ekleyin ve Kimliğe Göre Seçin**

Aşağıdaki örnek kod, önce şunu kullanarak dört Özel XML Parçası ekler:[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)yöntem. Daha sonra kullanarak kimliklerini ayarlar[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) Emlak. Son olarak, kullanarak eklenen Özel XML Parçalarından birini bulur veya seçer.[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)yöntem. Lütfen referans için aşağıda verilen kodun konsol çıktısına da bakın.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsol Çıkışı**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
