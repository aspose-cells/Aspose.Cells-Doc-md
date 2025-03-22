---  
title: Export Document Structure While Converting to PDF with C++  
linktitle: Export Document Structure While Converting to PDF  
type: docs  
weight: 360  
url: /cpp/export-document-structure-while-converting-to-pdf/  
description: Learn how to export document structure while converting to PDF with Aspose.Cells in C++.  
---  

PDF logical structure facilities provide a mechanism for incorporating information regarding the document content structure into a PDF file. Aspose.Cells preserves information about the structure from a Microsoft Excel document, such as cell, row, table, worksheet, image, shape, header/footer, etc.  

With option [PdfSaveOptions.ExportDocumentStructure](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/exportdocumentstructure/), you can save to a tagged PDF with document structure exported.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the Excel file with image, shape, chart, etc.
    Workbook workbook(u"document-structure-example.xlsx");

    // Set to export document structure.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetExportDocumentStructure(true);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with document structure!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

  