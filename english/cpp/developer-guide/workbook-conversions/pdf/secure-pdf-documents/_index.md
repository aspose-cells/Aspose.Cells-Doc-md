---
title: Secure PDF Documents with C++
linktitle: Secure PDF Documents
type: docs
weight: 120
url: /cpp/secure-pdf-documents/
description: Learn how to secure PDF documents with owner and user passwords using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes, developers need to work with encrypted PDF files. For example:

- Secure the documents with owner and user passwords so not just anyone can open it.
- Set restrictions or permissions to the document after the document is opened. e.g. restrict whether the document content can be printed or extracted.

This article explains how to pass in PDF security options when saving spreadsheets to PDF.

{{% /alert %}}

Aspose.Cells provides [**PdfSecurityOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) for working with security. You can set owner and user passwords while saving to PDF. The owner password or user password will be required to open the encrypted PDF document for viewing.

- The user password can be null or empty string, in this case no password will be required from the user when opening the PDF document.
- Opening the PDF document with the correct owner password allows full access (without any access restrictions specified) to the document.
- Opening the PDF document with the correct user password (or opening a document that does not have a user password) allows limited access as the permissions specified.

The sample code below describes how to secure PDFs with Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;
using namespace Aspose::Cells::Rendering::PdfSecurity;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"securepdf_test.out.pdf";

    // Open an Excel file
    Workbook workbook(inputFilePath);

    // Instantiate PDFSaveOptions to manage security attributes
    PdfSaveOptions saveOption;

    // Create and configure PDF security options
    PdfSecurityOptions securityOptions;
    securityOptions.SetUserPassword(u"user");
    securityOptions.SetOwnerPassword(u"owner");
    securityOptions.SetExtractContentPermission(false);
    securityOptions.SetPrintPermission(false);

    // Assign security options to save options
    saveOption.SetSecurityOptions(securityOptions);

    // Save the PDF document with encrypted settings
    workbook.Save(outputFilePath, saveOption);

    std::cout << "PDF saved with security settings successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

If the spreadsheet contains formulas, it is best to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) just before rendering it to PDF. This ensures that formula-dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}