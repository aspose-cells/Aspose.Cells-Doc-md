---
title: Установите шрифт по умолчанию при рендеринге электронной таблицы на HTML.
type: docs
weight: 370
url: /ru/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells позволяет вам установить шрифт по умолчанию при рендеринге электронной таблицы на HTML. Пожалуйста, используйте[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) для этой цели. Это свойство полезно, когда в электронной таблице есть ячейки с недопустимыми или несуществующими шрифтами. Затем эти ячейки будут отображаться шрифтом, указанным с помощью параметра[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) имущество.

{{% /alert %}}

## Установите шрифт по умолчанию при рендеринге электронной таблицы на HTML.

Следующий пример кода создает книгу и добавляет некоторый текст в ячейку B4 первого рабочего листа и задает для нее какой-то неизвестный/несуществующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman и т. д.

 На снимке экрана показан эффект от установки разных имен шрифтов по умолчанию через[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)имущество.

![дело:изображение_альтернативный_текст](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Код генерирует[выходной файл HTML с Courier New](5115516) ,[вывод HTML с Arial](5115518) , и[выходной файл HTML с Times New Roman](5115517).

## Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
