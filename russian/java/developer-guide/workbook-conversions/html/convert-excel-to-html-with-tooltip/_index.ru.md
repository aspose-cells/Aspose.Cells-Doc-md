---
title: Преобразовать Excel в HTML c всплывающей подсказкой
type: docs
weight: 150
url: /ru/java/convert-excel-to-html-with-tooltip/
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Возможно, есть случаи, когда текст обрезается в создаваемом HTML, и вы хотите отображать полный текст в виде всплывающей подсказки при событии наведения. Aspose.Cells поддерживает это, предоставляя свойство [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText). Установка свойства [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#AddTooltipText) в **true** добавит полный текст в виде всплывающей подсказки в создаваемое HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Приведенный ниже код загружает [исходный файл Excel](AddTooltipToHtmlSample.xlsx) и генерирует [выходной HTML файл](AddTooltipToHtmlSample_out.zip) с всплывающей подсказкой.

## Образец кода

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.java" >}}
