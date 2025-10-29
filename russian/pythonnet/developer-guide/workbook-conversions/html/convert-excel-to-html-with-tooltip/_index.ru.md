---
title: Преобразовать Excel в HTML c всплывающей подсказкой
type: docs
weight: 200
url: /ru/python-net/convert-excel-to-html-with-tooltip/
description: В этой теме показано, как преобразовать Excel в HTML с подсказкой, используя Aspose.Cells для Python via NET.
keywords: Преобразовать Excel в HTML с подсказкой Python, Преобразовать Excel в HTML с подсказкой Python via NET, Python via NET Excel в HTML с подсказкой, Python Рабочая книга в HTML с подсказкой.
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Могут быть случаи, когда текст обрезается в сгенерированном HTML, и вы хотите отобразить полный текст в виде подсказки при событии наведения. Aspose.Cells поддерживает это, предоставляя свойство [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/). Установка свойства [**HtmlSaveOptions.add_tooltip_text**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/add_tooltip_text/) в **true** добавит полный текст в виде подсказки в сгенерированное HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

В следующем коде загружается [исходный файл Excel](98107416.xlsx) и создается [файл HTML вывода](98107417.zip) с подсказкой.

Образец кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ConvertExcelFileToHtmlWithTooltip-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
