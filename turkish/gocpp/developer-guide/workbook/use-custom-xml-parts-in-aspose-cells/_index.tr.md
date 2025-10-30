---
title: Golang kullanarak C++ ile Aspose.Cells ile Özel XML Parçalarını kullanın.
linktitle: Özel XML Parçalarını Kullanma
type: docs
weight: 390
url: /tr/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Golang kullanarak C++ ile Aspose.Cells ile Excel dosyalarında özel XML parçalarını programlama yoluyla kullanmayı öğrenin.
---

## Aspose.Cells'te Özel XML Parçalarını Kullanma

Özel XML Parçaları, SharePoint gibi farklı uygulamalar tarafından bir Excel dosyası içinde saklanan XML verileridir. Bu veriler, ihtiyaç duyan çeşitli uygulamalar tarafından kullanılır. Microsoft Excel bu veriyi kullanmaz, bu nedenle ona eklemek için GUI yoktur. Bu veriyi görmek için, **.xlsx** uzantısını **.zip** olarak değiştirip **WinZip** ile açabilirsiniz. Ayrıca, ZIP dosyasını herhangi bir üçüncü taraf Windows zip aracıyla (örneğin WinRAR veya WinZip) da açabilirsiniz. Veri, **customXml** klasörü içinde bulunur.

Aspose.Cells kullanarak [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) yöntemiyle özel XML parçaları ekleyebilirsiniz.

Aşağıdaki örnek kod, **Book Catalog XML**'yi eklemek için [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) yöntemi kullanır ve adı **BookStore**'dır. Bu kodun sonucu, aşağıdaki görüntüde gösterilmektedir. Görüldüğü gibi, Book Catalog XML, **BookStore** düğümü içine eklenmiştir; bu, bu özelliğin adıdır.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Özel XML Parçalarını Kullanmak için C++ Kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## İlgili Makale

- [Belge Bilgisi Panelinde Görünen Özel Özellikleri Ekleme](/cells/tr/cpp/adding-custom-properties-visible-inside-document-information-panel/)
