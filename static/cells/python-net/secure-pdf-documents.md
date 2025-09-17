##Secure PDF Documents
Learn how to pass in PDF security options when saving spreadsheets to PDF with Aspose.Cells for Python via .NET API.
Sometimes, developers need to work with encrypted PDF files. For example:
- Secure the documents with owner and user passwords so not just anyone can open it.
- Set restrictions or permissions to the document after the document is opened. e.g. restrict whether the document content can be printed or extracted.
This article explains how to pass in PDF security options when saving spreadsheets to PDF.
Aspose.Cells for Python via .NET provides [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) for working with security.  You can set owner and user passwords while saving to PDF. The owner password or user password will be required to open the encrypted PDF document for viewing.
- The user password can be null or empty string, in this case no password will be required from the user when opening the PDF document.
- Opening the PDF document with the correct owner password allows full access(without any access restrictions specified) to the document.
- Opening the PDF document with the correct user password (or opening a document that does not have a user password) allows limited access as the permissions specified.
The sample code below describes how to secure PDFs with Aspose.Cells for Python via .NET.
If the spreadsheet contains formulas, it is best to call [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) just before rendering it to PDF. This ensures that formula dependent values are recalculated and the correct values are rendered in the PDF.
