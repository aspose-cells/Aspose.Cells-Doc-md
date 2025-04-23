---
title: Предотвращение экспорта скрытого содержимого листа при сохранении в HTML
type: docs
weight: 90
url: /ru/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet). По умолчанию свойство [**ExportHiddenWorksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportHiddenWorksheet) установлено в **true**. Если вы установите его в **false**, то Aspose.Cells не будет экспортировать скрытое содержимое листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PreventExportingHiddenWorksheetContent-PreventExportingHiddenWorksheetContent.java" >}}

Помимо контроля за экспортом скрытых листов, вы также можете настроить дополнительные параметры для экспорта книги в HTML. В следующих статьях демонстрируются другие функции, поддерживаемые Aspose.Cells для экспорта книг в HTML.

- [Конвертировать Excel в HTML с заголовками](/cells/ru/java/convert-excel-to-html-with-headings/)
- [Исключить неиспользуемые стили во время преобразования Excel в HTML](/cells/ru/java/exclude-unused-styles-during-excel-to-html-conversion/)
- [Экспортировать комментарии при сохранении файла Excel в HTML](/cells/ru/java/export-comments-while-saving-excel-file-to-html/)
- [Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML](/cells/ru/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/)
- [Экспорт аналогичного стиля границы, когда стиль границы не поддерживается веб-браузерами](/cells/ru/java/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
{{< app/cells/assistant language="java" >}}
