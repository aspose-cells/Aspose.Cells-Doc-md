---
title: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML
type: docs
weight: 370
url: /ru/python-net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет установить шрифт по умолчанию при рендеринге электронной таблицы в HTML. Пожалуйста, используйте [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) для этой цели. Это свойство полезно, если в электронной таблице есть ячейки с недопустимыми или несуществующими шрифтами. Тогда эти ячейки будут отображаться шрифтом, указанным в свойстве [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

{{% /alert %}}

## Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML

Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.

На скриншоте показан эффект установки различных наименований шрифтов по умолчанию через свойство [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Код генерирует [выходной файл HTML с Courier New](5115516), [выходной HTML с Arial](5115518) и [выходной файл HTML с Times New Roman](5115517).

## Образец кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetDefaultFontWhileRendering-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
