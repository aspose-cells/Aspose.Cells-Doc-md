---
title: Встроить вложение в PDF
type: docs
weight: 370
url: /ru/java/embed-attachment-to-pdf/

---

В Excel вы можете вставить объект OLE со структурными данными ([пример вложенных вложений.xlsx](пример вложенных вложений.xlsx)) . Дважды щелкните по объекту OLE, встроенный файл будет открыт.

Обычно при конвертации в pdf объект OLE будет отображаться в виде значка или миниатюры без структурных данных объекта OLE. С помощью опции [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-) можно встроить структурные данные объекта OLE в качестве вложения в PDF. Вы можете дважды щелкнуть по значку или миниатюре в PDF, чтобы открыть исходный файл объекта OLE.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![вставленное-вложение.png](вставленное-вложение.png)

