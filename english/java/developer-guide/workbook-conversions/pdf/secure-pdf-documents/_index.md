---  
title: Secure PDF Documents  
type: docs  
weight: 260  
url: /java/secure-pdf-documents/  
description: Secure PDF files while converting from Excel files. This article demonstrates generating a secure PDF file from Excel with Aspose.Cells for Java API.  
keywords: secure pdf documents java, secure pdf documents, excel to secure pdf, excel to secure pdf java, convert excel to secure pdf, convert excel to secure pdf java, convert excel to password protected pdf, convert excel to password protected pdf java, excel to password protected pdf java, excel to password protected pdf  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}

Sometimes, developers need to work with encrypted PDF files. For example:

- Secure the documents with owner and user passwords so that not just anyone can open them.  
- Set restrictions or permissions to the document after the document is opened, e.g., restrict whether the document content can be printed or extracted.  

This article explains how to pass PDF security options when saving spreadsheets to PDF.

{{% /alert %}}

Aspose.Cells provides [**PdfSecurityOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions/) for working with security. You can set owner and user passwords while saving to PDF. The owner password or user password will be required to open the encrypted PDF document for viewing.

- The user password can be null or an empty string; in such a case, no password will be required from the user when opening the PDF document.  
- Opening the PDF document with the correct owner password allows full access (without any access restrictions specified) to the document.  
- Opening the PDF document with the correct user password (or opening a document that does not have a user password) allows limited access according to the specified permissions.  

The sample code below describes how to create secured PDF files with Aspose.Cells for Java API.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SecurePDFDocuments-SecurePDFDocuments.java" >}}

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) just before rendering it to PDF. This ensures that formula‑dependent values are recalculated, and the correct values are rendered in the PDF.

{{% /alert %}}  
{{< app/cells/assistant language="java" >}}
