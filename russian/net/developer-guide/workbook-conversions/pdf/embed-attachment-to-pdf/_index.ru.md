---
title: Встроить вложение в PDF
type: docs
weight: 380
url: /ru/net/embed-attachment-to-pdf/

---

В Excel вы можете вставить объект OLE со структурными данными ([пример вложенных вложений.xlsx](пример вложенных вложений.xlsx)) . Дважды щелкните по объекту OLE, встроенный файл будет открыт.

Обычно, при конвертации в PDF объект Ole будет отображаться как значок или миниатюра без исходных данных объекта Ole. С помощью параметра [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/) вы можете встроить исходные данные объекта Ole в качестве вложения в PDF. Вы можете дважды щелкнуть по значку или миниатюре в PDF, чтобы открыть исходный файл объекта Ole.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![вставленное-вложение.png](вставленное-вложение.png)
