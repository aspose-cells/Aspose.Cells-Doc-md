---
title: PDF ye Ekleri Python.NET ile gömmek
linktitle: Ekli Dosya Ekle PDF ye
type: docs
weight: 380
url: /tr/python-net/embed-attachment-to-pdf/
description: Aspose.Cells for Python via .NET kullanarak PDF dosyalarına Ole Nesne ekleri gömlemenin nasıl yapılacağını öğrenin.
---

Excel'de, kaynaktan verili Ole Nesnesini ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)) ekleyebilirsiniz. Gömülü dosyayı açmak için Ole Nesnesine çift tıklayın.

PDF'ye dönüştürürken, Ole Nesnesi genellikle kaynak verisi olmadan simge veya küçük resim olarak gösterilir. [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) özelliği kullanılarak, Ole Nesnesinin kaynak verisi PDF'ye ek olarak gömülebilir. Kullanıcılar PDF'deki simge/küçük resme çift tıklayarak gömülü dosyaya erişebilirler.

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
