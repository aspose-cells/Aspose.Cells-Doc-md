---
title: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 70
url: /tr/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgelerinin içinde saklanan ve bunlarla ilgilenen uygulamalar tarafından kullanılan XML verileridir. Şu anda, bunları Microsoft Excel arayüzü kullanarak doğrudan eklemenin bir yolu yoktur. Ancak, bunları programatik olarak çeşitli yollarla ekleyebilirsiniz örn. VSTO kullanarak, Aspose.Cells kullanarak vb. [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) metodunu kullanarak Aspose.Cells for Python via .NET API ile Özel XML Parçası ekleyebilirsiniz. Ayrıca, kimliğini [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) özelliği ile ayarlayabilirsiniz. Ayrıca, Kimliğe göre özel XML Parçasını seçmek isterseniz, [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) metodunu kullanabilirsiniz.

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**

Aşağıdaki örnek kod önce [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) yöntemi ile dört Özel XML Parçası ekler. Ardından bunların ID'lerini [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) özelliği ile ayarlar. Son olarak, eklenen Özel XML Parçalardan birini bulur veya seçer [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) yöntemini kullanarak. Lütfen aşağıdaki kodun konsol çıktısını da referans için inceleyiniz.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **Konsol Çıktısı**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

