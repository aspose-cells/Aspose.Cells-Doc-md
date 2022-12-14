---
title: Преобразование Excel в HTML с помощью всплывающей подсказки
type: docs
weight: 150
url: /ru/java/convert-excel-to-html-with-tooltip/
---
## **Преобразование Excel в HTML с помощью всплывающей подсказки**

Могут быть случаи, когда текст обрезается в сгенерированном HTML, и вы хотите отобразить весь текст в виде всплывающей подсказки при наведении курсора. Aspose.Cells поддерживает это, предоставляя**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**имущество. Настройка**[HtmlSaveOptions.AddTooltipText](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText)**собственность на**истинный**добавит полный текст в качестве всплывающей подсказки в сгенерированном HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML-файле.

![дело:изображение_альтернативный_текст](convert-excel-to-html-with-tooltip_1.jpg)

Следующий пример кода загружает[исходный файл excel](AddTooltipToHtmlSample.xlsx)и генерирует[выходной HTML-файл](AddTooltipToHtmlSample_out.zip)с подсказкой.

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
