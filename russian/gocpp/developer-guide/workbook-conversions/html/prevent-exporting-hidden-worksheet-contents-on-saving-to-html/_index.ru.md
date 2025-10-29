---
title: Предотвратите экспорт скрытого содержимого листов при сохранении в HTML с помощью Golang через C++
linktitle: Предотвратить экспорт скрытого содержимого листа
type: docs
weight: 210
url: /ru/go-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Узнайте, как предотвратить экспорт скрытого содержимого листов при сохранении книг Excel в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexporthiddenworksheet/). По умолчанию оно установлено в **true**, и скрытые листы экспортируются в HTML. Если вы установите его в **false**, Aspose.Cells не будет экспортировать содержимое скрытых листов.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreventExportingHiddenWorksheetContentsOnSavingToHtml.go" >}}
