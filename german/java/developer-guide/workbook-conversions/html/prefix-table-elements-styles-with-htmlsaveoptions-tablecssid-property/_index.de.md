---
title: Tabellenelemente Styles mit der Eigenschaft HtmlSaveOptions.TableCssId prefixieren
type: docs
weight: 110
url: /de/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Mögliche Verwendungsszenarien**

Mit Aspose.Cells können Sie Tabellenelementstilen mit der [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId)-Eigenschaft voranstellen. Angenommen, Sie legen diese Eigenschaft mit einem Wert wie *MyTest_TableCssId* fest, dann finden Sie Tabellenelementstile wie unten gezeigt.

{{< highlight java >}}

table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

Der folgende Screenshot zeigt die Auswirkungen der Verwendung der [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId)-Eigenschaft auf die Ausgabe von HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft**

Der folgende Beispielcode erläutert, wie die [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#TableCssId)-Eigenschaft genutzt werden kann. Bitte überprüfen Sie die durch den Code generierte [Ausgabe-HTML](60489791.zip) als Referenz.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.java" >}}
{{< app/cells/assistant language="java" >}}
