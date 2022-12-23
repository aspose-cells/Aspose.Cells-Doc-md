---
title: Aspose.Cells'de Özel XML Parçalarını Kullanın
type: docs
weight: 390
url: /tr/net/use-custom-xml-parts-in-aspose-cells/
---
## Aspose.Cells'de Özel XML Parçalarını Kullanma

Özel XML Parçaları, excel dosyası içinde SharePoint vb. farklı uygulamalar tarafından saklanan XML verileridir. Bu veriler, ona ihtiyaç duyan farklı uygulamalar tarafından tüketilir. Microsoft Excel bu verileri kullanmaz, bu nedenle eklenecek GUI yoktur. Uzantısını değiştirerek bu verileri görüntüleyebilirsiniz.**.xlsx** içine**.zip** ve sonra kullanarak açarak**WinZip** . ZIP dosyasını, WinRAR veya WinZip gibi herhangi bir 3. bölüm Windows zip yardımcı programını kullanarak da açabilirsiniz.**özelXml** Klasör.

 Aspose.Cells'i kullanarak özel XML parçaları ekleyebilirsiniz.[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)yöntem.

 Aşağıdaki örnek kod,[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) yöntemini ekler ve**Kitap Kataloğu XML** ve onun adı**Kitapçı**. Aşağıdaki resimde bu kodun sonucu gösterilmektedir. Gördüğünüz gibi Book Catalog XML, bu özelliğin adı olan BookStore düğümünün içine eklenir.

![yapılacaklar:resim_alternatif_metin](use-custom-xml-parts-in-aspose-cells_1.png)

![yapılacaklar:resim_alternatif_metin](use-custom-xml-parts-in-aspose-cells_2.png)

## Özel XML parçalarını kullanmak için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## İlgili Makale

- [Belge Bilgileri Panelinde görünen Özel Özellikler ekleme](/cells/tr/net/adding-custom-properties-visible-inside-document-information-panel/)
