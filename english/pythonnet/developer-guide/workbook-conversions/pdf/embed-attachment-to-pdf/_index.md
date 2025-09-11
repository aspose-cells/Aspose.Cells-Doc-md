---
title: Embed Attachment to PDF with Python.NET
linktitle: Embed Attachment to PDF
type: docs
weight: 380
url: /python-net/embed-attachment-to-pdf/
description: Learn how to embed Ole Object attachments in PDF files using Aspose.Cells for Python via .NET.
---

In Excel, you can insert an Ole Object with source data ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double click the Ole Object to open the embedded file.

When converting to PDF, the Ole Object is typically rendered as an icon or thumbnail without source data. Using the [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) property, you can embed the Ole Object's source data as an attachment in PDF. Users can double-click the icon/thumbnail in PDF to access the embedded file.

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