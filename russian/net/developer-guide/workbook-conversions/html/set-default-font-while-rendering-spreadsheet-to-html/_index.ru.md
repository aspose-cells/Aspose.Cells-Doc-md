---
title: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML
type: docs
weight: 370
url: /ru/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет установить шрифт по умолчанию при рендеринге электронной таблицы в HTML. Пожалуйста, используйте [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) для этой цели. Это свойство полезно, если в электронной таблице есть ячейки с недопустимыми или несуществующими шрифтами. Тогда эти ячейки будут отображаться шрифтом, указанным в свойстве [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML

Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.

На скриншоте показан эффект установки различных наименований шрифтов по умолчанию через свойство [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Код генерирует [выходной файл HTML с Courier New](5115516), [выходной HTML с Arial](5115518) и [выходной файл HTML с Times New Roman](5115517).

## Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
