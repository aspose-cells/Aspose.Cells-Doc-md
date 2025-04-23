---
title: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 70
url: /tr/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgeleri içinde depolanan ve bunlarla ilgili uygulamalar tarafından kullanılan XML verileridir. Şu anda Microsoft Excel UI aracılığıyla onları eklemenin bir doğrudan yolu yoktur. Ancak, bu parçaları programlı olarak çeşitli şekillerde ekleyebilirsiniz, örn. VSTO kullanarak, Aspose.Cells kullanarak vb. Aspose.Cells API'sını kullanarak Özel XML Parçası eklemek istiyorsanız [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) yöntemini kullanın. Ayrıca, [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) özelliğini kullanarak ID'sini ayarlayabilirsiniz. Benzer şekilde, belirli bir ID ile Özel XML Parçasını seçmek isterseniz, [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) yöntemini kullanabilirsiniz.

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**

Aşağıdaki örnek kod önce [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) yöntemi ile dört Özel XML Parçası ekler. Ardından bunların ID'lerini [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) özelliği ile ayarlar. Son olarak, eklenen Özel XML Parçalardan birini bulur veya seçer [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) yöntemini kullanarak. Lütfen aşağıdaki kodun konsol çıktısını da referans için inceleyiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
