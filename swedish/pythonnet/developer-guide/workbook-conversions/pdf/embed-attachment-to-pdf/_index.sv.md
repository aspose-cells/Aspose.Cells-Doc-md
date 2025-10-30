---
title: Bädda in bilaga i PDF med Python.NET
linktitle: Inbädda bilaga till PDF
type: docs
weight: 380
url: /sv/python-net/embed-attachment-to-pdf/
description: Lär dig hur du inbäddar Ole Object bilagor i PDF filer med Aspose.Cells för Python via .NET.
---

I Excel kan du infoga ett Ole Object med källadata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole Object för att öppna den inbäddade filen.

När du konverterar till PDF visas Ole Object oftast som en ikon eller miniatyrbild utan källdata. Med hjälp av egendomen [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) kan du bädda in Ole Object:s källdata som en bilaga i PDF. Användare kan dubbelklicka på ikonen/miniatyrbilden i PDF för att komma åt den inbäddade filen.

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
