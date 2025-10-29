---
title: 使用Python.NET在PDF中嵌入附件
linktitle: 将附件嵌入到PDF中
type: docs
weight: 380
url: /zh/python-net/embed-attachment-to-pdf/
description: 学习如何使用 Aspose.Cells for Python 将 Ole 对象附件嵌入到 PDF 文件中 via .NET。
---

在 Excel 中，您可以插入带有源数据的 Ole 对象（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。双击 Ole 对象以打开嵌入的文件。

转换为 PDF 时，Ole 对象通常以图标或缩略图渲染，没有源数据。使用 [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) 属性，可以将 Ole 对象的源数据作为附件嵌入到 PDF 中。用户可以在 PDF 中双击图标/缩略图访问嵌入的文件。

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
