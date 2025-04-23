---
title: Aspose.Cells te Özel XML Parçalarını Kullanma
type: docs
weight: 390
url: /tr/net/use-custom-xml-parts-in-aspose-cells/
---

## Aspose.Cells'te Özel XML Parçalarını Kullanma

Özel XML Parçaları, farklı uygulamaların (SharePoint vb.) excel dosyasında depoladığı XML verileridir. Bu veriye ihtiyaç duyan farklı uygulamalar tarafından tüketilir. Microsoft Excel bu veriyi kullanmadığı için eklemek için bir GUI yoktur. **.xlsx** uzantısını **.zip**'e değiştirerek ve ardından **WinZip** ile açarak bu veriyi görebilirsiniz. Ayrıca ZIP dosyasını, WinRAR veya WinZip gibi 3. taraf Windows zip araçlarından herhangi biri ile açabilirsiniz. Veri **customXml** klasörünün içinde bulunmaktadır.

Aspose.Cells, [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) yöntemi aracılığıyla özel XML parçaları eklemenize olanak tanır.

Aşağıdaki örnek kod, [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) yönteminin kullanımını gösterir ve **Kitap Kataloğu XML** ekler, adı ise **Kitap Deposu**'dur. Aşağıdaki görüntü, bu kodun sonucunu göstermektedir. Gördüğünüz gibi Kitap Kataloğu XML, bu özelliğin adı olan Kitap Deposu düğümünün içine eklenmiştir.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Özel XML Parçalarını Kullanmak için C# Kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## İlgili Makale

- [Belge Bilgi Paneli içinde görülebilen Özel Özellikler eklemek](/cells/tr/net/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="csharp" >}}
