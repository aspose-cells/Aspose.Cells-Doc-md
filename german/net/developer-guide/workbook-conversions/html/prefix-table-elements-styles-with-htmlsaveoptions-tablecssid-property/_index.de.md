---
title: Tabellenelemente Styles mit der Eigenschaft HtmlSaveOptions.TableCssId prefixieren
type: docs
weight: 110
url: /de/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, Tabellenelementstile mit der [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)-Eigenschaft zu versehen. Nehmen wir an, Sie setzen diese Eigenschaft mit einem Wert wie **MyTest_TableCssId**, dann finden Sie Tabellenelementstile wie unten gezeigt

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

Der folgende Screenshot zeigt die Auswirkungen der Verwendung der [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)-Eigenschaft auf die Ausgabe von HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft**

Der folgende Beispielcode zeigt, wie die [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)-Eigenschaft verwendet wird. Bitte überprüfen Sie das [Ausgabe-HTML](60489790.zip), das vom Code generiert wurde, als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.cs" >}}
