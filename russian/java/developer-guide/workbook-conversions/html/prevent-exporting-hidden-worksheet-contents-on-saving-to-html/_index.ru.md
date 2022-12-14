---
title: Запретить экспорт скрытого содержимого рабочего листа при сохранении в HTML
type: docs
weight: 90
url: /ru/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Вы можете сохранять книги Excel в формате HTML. Однако, если рабочая книга содержит скрытые рабочие листы, Aspose.Cells по умолчанию экспортирует содержимое скрытого рабочего листа в выходной файл HTML (_ files), который содержит такие файлы, как рабочие листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда такой способ экспорта содержимого скрытых рабочих листов не подходит. Например, если скрытый рабочий лист содержит изображения, которые не следует экспортировать в_каталог файлов.

{{% /alert %}}

Aspose.Cells обеспечивает[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) имущество. По умолчанию[**Экспорт скрытого рабочего листа**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) свойство установлено на**истинный**. Если вы установите его на**ЛОЖЬ**, то Aspose.Cells не будет экспортировать скрытое содержимое листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Помимо контроля за экспортом скрытых рабочих листов или нет, вы также можете настроить дополнительные параметры для экспорта книги в HTML. В следующих статьях демонстрируются другие функции, поддерживаемые Aspose.Cells для экспорта книг в формат HTML.

- [Преобразование Excel в HTML с заголовками](/cells/ru/java/convert-excel-to-html-with-headings/)
- [Исключить неиспользуемые стили во время преобразования Excel в HTML](/cells/ru/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Экспорт комментариев при сохранении файла Excel в HTML](/cells/ru/java/export-comments-while-saving-excel-file-to-html/)
- [Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML](/cells/ru/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Экспорт аналогичного стиля границы, если стиль границы не поддерживается веб-браузерами](/cells/ru/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
