---
title: Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId
type: docs
weight: 110
url: /ru/python-net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет префиксить стили элементов таблиц с помощью [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id). Предположим, вы установите это свойство с каким-либо значением, например **MyTest_TableCssId**, тогда вы увидите стили элементов таблиц, как показано ниже

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

На следующем скриншоте показано влияние использования свойства [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id) на выходной HTML.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **Префиксные стили элементов таблицы с помощью свойства HtmlSaveOptions.TableCssId**

Следующий образец кода демонстрирует, как использовать свойство [**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id). Пожалуйста, проверьте [выходной HTML](60489790.zip), сгенерированный кодом, для справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.py" >}}
{{< app/cells/assistant language="python-net" >}}
