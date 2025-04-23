---
title: HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek
type: docs
weight: 110
url: /tr/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, tablo öğeleri stillerini [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid) özelliği ile ön eklemek için izin verir. Varsayalım ki, bu özelliği **MyTest_TableCssId** gibi bir değerle ayarlarsanız, aşağıdaki gibi tablo öğeleri stilleri bulacaksınız

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

Aşağıdaki ekran görüntüsü, çıktı HTML'sine [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid) özelliğinin kullanılmasının etkisini gösterir.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek**

Aşağıdaki örnek kod, [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid) özelliğinin kullanımını gösterir. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489790.zip)'ni inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.cs" >}}
{{< app/cells/assistant language="csharp" >}}
