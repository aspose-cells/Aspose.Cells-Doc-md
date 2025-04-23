---
title: Встроить вложение в PDF
type: docs
weight: 370
url: /ru/java/embed-attachment-to-pdf/

---

В Excel можно вставить объект Ole с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Двойной щелчок по объекту Ole откроет вложенный файл.

Обычно при преобразовании в pdf объект Ole отображается в виде значка или миниатюры без исходных данных. При использовании опции [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), вы можете встроить исходные данные Ole-объекта как вложение в PDF. Двойной щелчок по значку или миниатюре в PDF откроет исходный файл Ole-объекта.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}

![embedded-attachment.png](embedded-attachment.png)

{{< app/cells/assistant language="java" >}}
