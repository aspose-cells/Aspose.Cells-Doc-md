---
title: Secure PDF Documents
type: docs
weight: 260
url: /java/secure-pdf-documents/
description: Secure PDF files while converting from Excel files. This article demonstrates generating secure PDF file from Excel with Aspose.Cells for Java API.
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf
---

{{% alert color="primary" %}}

Sometimes, developers need to work with encrypted PDF files. For example, they need to secure documents with user and owner passwords so not just anyone can open them, or want to restrict whether the document content can be printed or extracted.

This article explains how to pass in PDF security options when saving spreadsheets to PDF.

{{% /alert %}} 

Aspose.Cells APIs provide the [**PdfSecurityOptions**](https://apireference.aspose.com/cells/java/com.aspose.cells/PdfSecurityOptions) class for working with the security of PDF file format. The sample code below describes how to create secured PDF files with Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) just before rendering it to PDF. This ensures that formula dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}
