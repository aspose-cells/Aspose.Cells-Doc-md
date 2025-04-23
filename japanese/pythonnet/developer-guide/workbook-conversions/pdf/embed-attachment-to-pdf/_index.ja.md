---
title: Python.NETを使用してPDFに添付されたファイルを埋め込む
linktitle: PDFに添付を埋め込む
type: docs
weight: 380
url: /ja/python-net/embed-attachment-to-pdf/
description: Aspose.Cells for Python via .NETを使用して、Ole Objectの添付ファイルをPDFに埋め込む方法を学びます。
---

Excelでは、Ole Objectを挿入できます（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。Ole Objectをダブルクリックして埋め込みファイルを開きます。

PDFに変換する際、Ole Objectは一般的にアイコンまたはサムネイルとしてレンダリングされ、ソースデータは表示されません。 [PdfSaveOptions.embed_attachments](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/embed_attachments/) プロパティを使用して、Ole Objectのソースデータを添付ファイルとしてPDFに埋め込むことができます。ユーザーはPDFのアイコン/サムネイルをダブルクリックして埋め込まれたファイルにアクセスできます。

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
