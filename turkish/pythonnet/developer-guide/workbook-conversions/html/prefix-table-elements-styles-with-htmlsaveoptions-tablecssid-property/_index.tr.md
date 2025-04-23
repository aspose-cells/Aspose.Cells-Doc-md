---
title: HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek
type: docs
weight: 110
url: /tr/python-net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, tablo öğeleri stillerini [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id) özelliği ile ön eklemek için izin verir. Varsayalım ki, bu özelliği **MyTest_TableCssId** gibi bir değerle ayarlarsanız, aşağıdaki gibi tablo öğeleri stilleri bulacaksınız

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

Aşağıdaki ekran görüntüsü, çıktı HTML'sine [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id) özelliğinin kullanılmasının etkisini gösterir.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssId özelliği ile Tablo Öğeleri Stillerini Ön Eklemek**

Aşağıdaki örnek kod, [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id) özelliğinin kullanımını gösterir. Referans için kod tarafından oluşturulan [çıktı HTML'si](60489790.zip)'ni inceleyin.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.py" >}}
