---
title: Встроить вложение в PDF с помощью Python.NET
linktitle: Встроить вложение в PDF
type: docs
weight: 380
url: /ru/python-net/embed-attachment-to-pdf/
description: Узнайте, как встроить вложения Ole Object в PDF файлы, используя Aspose.Cells для Python via .NET.
---

В Excel вы можете вставить Ole Object с исходными данными ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Дважды щелкните Ole Object, чтобы открыть встроенный файл.

При конвертировании в PDF Ole Object обычно отображается как иконка или миниатюра без исходных данных. Используя свойство [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/), вы можете встроить исходные данные Ole Object в PDF как вложение. Пользователи могут дважды щелкнуть по иконке/миниатюре в PDF, чтобы получить доступ к встроенному файлу.

```python
from aspose.cells import Workbook, PdfSaveOptions

# Open the template file
wb = Workbook("embedded-attachments-example.xlsx")

# Set to embed Ole Object attachment.
pdf_save_options = PdfSaveOptions()
pdf_save_options.embed_attachments = True

# Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdf_save_options)
```

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="python-net" >}}
