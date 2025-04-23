---
title: Преобразовать Excel в HTML c всплывающей подсказкой
type: docs
weight: 200
url: /ru/net/convert-excel-to-html-with-tooltip/
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Могут быть случаи, когда текст обрезается в сгенерированном HTML, и вы хотите отобразить полный текст в виде подсказки при событии наведения. Aspose.Cells поддерживает это, предоставляя свойство [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext). Установка свойства [**HtmlSaveOptions.AddTooltipText**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/addtooltiptext) в **true** добавит полный текст в виде подсказки в сгенерированное HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

В следующем коде загружается [исходный файл Excel](98107416.xlsx) и создается [файл HTML вывода](98107417.zip) с подсказкой.

Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToHtmlWithTooltip-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
