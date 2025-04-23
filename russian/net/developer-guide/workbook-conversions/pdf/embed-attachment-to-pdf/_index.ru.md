---
title: Встроить вложение в PDF
type: docs
weight: 380
url: /ru/net/embed-attachment-to-pdf/

---

В Excel можно вставить объект Ole с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Двойной щелчок по объекту Ole откроет вложенный файл.

В целом, при конвертации в pdf, Ole Object будет отображаться как иконка или миниатюра без исходных данных Ole Object. Вариантом [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/embedattachments/) можно встроить исходные данные Ole Object как вложение в PDF. Дважды щелкнув на иконке или миниатюре в PDF, вы сможете открыть исходный файл Ole Object.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-EmbedAttachmentToPdf.cs" >}}

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="csharp" >}}
