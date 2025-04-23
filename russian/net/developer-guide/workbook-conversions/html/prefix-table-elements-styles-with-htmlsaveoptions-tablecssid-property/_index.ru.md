---
title: Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ru/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет префиксить стили элементов таблиц с помощью [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid). Предположим, вы установите это свойство с каким-либо значением, например **MyTest_TableCssId**, тогда вы увидите стили элементов таблиц, как показано ниже

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

На следующем скриншоте показано влияние использования свойства [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid) на выходной HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId**

Следующий образец кода демонстрирует, как использовать свойство [**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid). Пожалуйста, проверьте [выходной HTML](60489790.zip), сгенерированный кодом, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.cs" >}}
{{< app/cells/assistant language="csharp" >}}
