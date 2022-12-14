---
title: Преобразование Excel в HTML с помощью всплывающей подсказки
type: docs
weight: 200
url: /ru/net/convert-excel-to-html-with-tooltip/
---
## **Преобразование Excel в HTML с помощью всплывающей подсказки**

Могут быть случаи, когда текст обрезается в сгенерированном HTML, и вы хотите отобразить весь текст в виде всплывающей подсказки при наведении курсора. Aspose.Cells поддерживает это, предоставляя**[HtmlSaveOptions.AddTooltipText] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** имущество. Настройка**[HtmlSaveOptions.AddTooltipText] (https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext)** собственность на**истинный** добавит полный текст в качестве всплывающей подсказки в сгенерированном HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML-файле.

![дело:изображение_альтернативный_текст](convert-excel-to-html-with-tooltip_1.jpg)

 Следующий пример кода загружает[исходный файл excel](98107416.xlsx) и генерирует[выходной HTML-файл](98107417.zip) с подсказкой.

Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
