---
title: Предотвращение экспорта скрытого содержимого листа при сохранении в HTML
type: docs
weight: 210
url: /ru/python-net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**HtmlSaveOptions.export_hidden_worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_hidden_worksheet). По умолчанию оно установлено в **true**, и скрытые листы экспортируются в HTML. Если вы установите его в **false**, Aspose.Cells не будет экспортировать содержимое скрытых листов.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PreventExportingHiddenContentWhileSavingAsHTML.py" >}}

