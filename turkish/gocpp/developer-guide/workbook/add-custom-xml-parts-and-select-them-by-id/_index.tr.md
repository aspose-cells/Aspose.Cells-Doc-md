---
title: Özelleştirilmiş XML Parçaları Ekleyin ve ID ile Seçin Golang ile C++
linktitle: Özel XML Parçalarını Ekleyin ve ID leri ile Seçin
type: docs
weight: 70
url: /tr/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Aspose.Cells kullanarak Golang ile C++ aracılığıyla Excel dosyalarına özel XML parçaları nasıl eklenir ve seçilir öğrenin.
---

## **Olası Kullanım Senaryoları**

Özel XML Parçaları, Microsoft Excel belgeleri içinde depolanan XML verileridir ve bunlarla etkileşimde bulunan uygulamalar tarafından kullanılır. Şu anda bunları eklemenin doğrudan bir yolu Microsoft Excel UI kullanılarak yoktur. Ancak, bunları programlı olarak, VSTO veya Aspose.Cells kullanarak çeşitli yollarla ekleyebilirsiniz. Aspose.Cells API'sini kullanarak bir Özel XML Parçası eklemek için [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) metodunu kullanın. Ayrıca, kimliğini [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) özelliğiyle ayarlayabilirsiniz. Benzer şekilde, bir XML Parçasını Kimlik ile seçmek için [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/) metodunu kullanabilirsiniz.

## **Özel XML Parçalarını ekleyin ve ID'leri ile seçin**

Aşağıdaki örnek kod öncelikle [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) yöntemiyle dört Özel XML Parçası ekler. Ardından, kimliklerini [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/) özelliğiyle ayarlar. Son olarak, eklenen Özel XML Parçalarından birini bulur veya seçer. Lütfen aşağıdaki kodun konsol çıkışını referans olarak inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Konsol Çıktısı**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
