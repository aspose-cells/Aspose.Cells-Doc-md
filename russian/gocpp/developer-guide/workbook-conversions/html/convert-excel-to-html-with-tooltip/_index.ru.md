---
title: Конвертация Excel в HTML с подсказкой с помощью C++
linktitle: Преобразовать Excel в HTML c всплывающей подсказкой
type: docs
weight: 200
url: /ru/go-cpp/convert-excel-to-html-with-tooltip/
description: Конвертация Excel в HTML с добавлением подсказок с помощью Aspose.Cells и C++.
---

## **Преобразование Excel в HTML со всплывающей подсказкой**

Бывают случаи, когда в сгенерированном HTML часть текста обрезана, и вы хотите отображать полный текст в виде подсказки при наведении. Aspose.Cells поддерживает это свойством [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/). Установка свойства [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getaddtooltiptext/) в **true** добавит полный текст в виде подсказки в сгенерированный HTML.

На следующем изображении показана всплывающая подсказка в сгенерированном HTML файле.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Следующий пример кода загружает [исходный Excel-файл](98107416.xlsx) и генерирует [выходной HTML-файл](98107417.zip) с подсказкой.

Образец кода

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToHtmlWithTooltip.go" >}}
