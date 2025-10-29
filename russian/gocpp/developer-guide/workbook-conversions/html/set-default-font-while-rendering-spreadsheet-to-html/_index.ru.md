---
title: Установите шрифт по умолчанию при рендеринге таблицы в HTML с помощью Golang через C++
linktitle: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML
type: docs
weight: 370
url: /ru/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Узнайте, как устанавливать шрифт по умолчанию при отображении таблицы в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет устанавливать шрифт по умолчанию при преобразовании таблицы в HTML. Пожалуйста, используйте [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) для этой цели. Эта характеристика полезна, когда в таблице есть ячейки с недопустимыми или несуществующими шрифтами. Тогда такие ячейки будут отображаться в шрифте, указанном с помощью свойства [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML

Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.

На снимке экрана показан эффект установки разных шрифтов по умолчанию через свойство [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Код генерирует [выходной файл HTML с Courier New](5115516), [выходной HTML с Arial](5115518) и [выходной файл HTML с Times New Roman](5115517).

## Образец кода

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
