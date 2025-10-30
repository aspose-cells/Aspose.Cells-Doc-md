---
title: Tabellenelemente Styles mit der Eigenschaft HtmlSaveOptions.TableCssId prefixieren
type: docs
weight: 110
url: /de/python-net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, Tabellenelementstile mit der [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)-Eigenschaft zu versehen. Nehmen wir an, Sie setzen diese Eigenschaft mit einem Wert wie **MyTest_TableCssId**, dann finden Sie Tabellenelementstile wie unten gezeigt

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

Der folgende Screenshot zeigt die Auswirkungen der Verwendung der [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)-Eigenschaft auf die Ausgabe von HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft**

Der folgende Beispielcode zeigt, wie die [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)-Eigenschaft verwendet wird. Bitte überprüfen Sie das [Ausgabe-HTML](60489790.zip), das vom Code generiert wurde, als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.py" >}}
{{< app/cells/assistant language="python-net" >}}
