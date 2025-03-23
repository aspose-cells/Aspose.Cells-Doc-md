---
title: Convert Excel file to PDF format compatible with PDFA-1a with C++
linktitle: Convert Excel file to PDF format compatible with PDFA-1a
type: docs
weight: 130
url: /cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Learn how to convert Excel files to PDF/A-1a compliant PDF format using Aspose.Cells with C++.
---

## **Possible Usage Scenarios**

PDF/A is a unique flavor of PDF designed for the long-term preservation of documents. PDF/A is an ISO-standardized version of the Portable Document Format (PDF) which is an archival format of PDF that embeds all fonts used in the document within the PDF file. PDF/A differs from PDF by prohibiting features, such as font linking (as opposed to font embedding) and encryption. Aspose.Cells enables you to save the Excel files to PDF/A compliant PDF files (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, and PDF/A-3u are supported). This topic describes how to save the Excel workbook to PDF/A compliant (PDF/A-1a) PDF file.

## **Convert Excel file to PDF Format Compatible with PDF/A-1a**

Developers may use the [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) that enables you to save the Excel files to PDF/A compliant PDF files.

The following sample code explains how to convert Excel file to PDF format compatible with PDF/A-1a. Please see its [output PDF](outputCompliancePdfA1a.pdf) as well as the screenshot for a reference.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```