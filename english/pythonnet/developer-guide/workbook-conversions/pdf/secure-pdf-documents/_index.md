---
title: Secure PDF Documents
type: docs
weight: 120
url: /python-net/secure-pdf-documents/
description: Learn how to pass in PDF security options when saving spreadsheets to PDF with Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, developers need to work with encrypted PDF files. For example:

- Secure the documents with owner and user passwords so **that** not just anyone can open it.
- Set restrictions or permissions to the document after the document is opened. e.g., restrict whether the document content can be printed or extracted.

This article explains how to pass in PDF security options when saving spreadsheets to PDF.

{{% /alert %}}

Aspose.Cells for Python via .NET provides [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) for working with security. You can set owner and user passwords while saving to PDF. **Either** the owner password or the user password will be required to open the encrypted PDF document for viewing.

- The user password can be null or an empty string, **in which case** no password will be required from the user when opening the PDF document.
- Opening the PDF document with the correct owner password allows full access **(without any access restrictions specified)** to the document.
- Opening the PDF document with the correct user password (or opening a document that does not have a user password) allows limited access **as specified by the permissions**.

The sample code below describes how to secure PDFs with Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering it to PDF. This ensures that **formula‑dependent** values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
