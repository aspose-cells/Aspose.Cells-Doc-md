---
title: Secure PDF Documents with Node.js via C++
linktitle: Secure PDF Documents
type: docs
weight: 120
url: /nodejs-cpp/secure-pdf-documents/
description: Learn how to secure PDF documents by using owner and user passwords, and set permissions for PDF files using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Sometimes, developers need to work with encrypted PDF files. For example:

- Secure the documents with owner and user passwords so not just anyone can open it.
- Set restrictions or permissions to the document after the document is opened. e.g. restrict whether the document content can be printed or extracted.

This article explains how to pass in PDF security options when saving spreadsheets to PDF.

{{% /alert %}}

Aspose.Cells provides [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) for working with security. You can set owner and user passwords while saving to PDF. The owner password or user password will be required to open the encrypted PDF document for viewing.

- The user password can be null or an empty string; in this case, no password will be required from the user when opening the PDF document.
- Opening the PDF document with the correct owner password allows full access (without any access restrictions specified) to the document.
- Opening the PDF document with the correct user password (or opening a document that does not have a user password) allows limited access as the permissions specified.

The sample code below describes how to secure PDFs with Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) just before rendering it to PDF. This ensures that formula dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}