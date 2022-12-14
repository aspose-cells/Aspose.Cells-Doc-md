---
title: Запретить экспорт скрытого содержимого рабочего листа при сохранении в HTML
type: docs
weight: 210
url: /ru/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/
---
{{% alert color="primary" %}}

Вы можете сохранять книги Excel в формате HTML. Однако, если рабочая книга содержит скрытые рабочие листы, Aspose.Cells по умолчанию экспортирует содержимое скрытого рабочего листа в выходной файл HTML (_ files), который содержит такие файлы, как рабочие листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда такой способ экспорта содержимого скрытых рабочих листов не подходит. Например, если скрытый рабочий лист содержит изображения, которые не следует экспортировать в_каталог файлов.

{{% /alert %}}

 Aspose.Cells обеспечивает[**HtmlSaveOptions.ExportHiddenWorksheet**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exporthiddenworksheet) имущество. По умолчанию установлено значение**истинный** а скрытые рабочие листы экспортируются в HTML. Если вы установите его**ЛОЖЬ**, Aspose.Cells не будет экспортировать скрытое содержимое рабочего листа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PreventExportingHiddenContent-PreventExportingHiddenContentWhileSavingAsHTML.cs" >}}

