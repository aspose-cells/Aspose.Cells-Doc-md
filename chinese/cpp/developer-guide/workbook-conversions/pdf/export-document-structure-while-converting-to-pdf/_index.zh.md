---  
title: 使用C++在将文档转换为PDF时导出结构  
linktitle: 在将其转换为PDF时导出文档结构  
type: docs  
weight: 360  
url: /zh/cpp/export-document-structure-while-converting-to-pdf/  
description: 了解如何在使用Aspose.Cells将文档转换为PDF时导出结构信息。  
---  

PDF的逻辑结构功能提供了一种机制，将文档内容结构信息合并到PDF文件中。Aspose.Cells可以保留Microsoft Excel文档中的结构信息，如单元格、行、表、工作表、图片、形状、页眉/页脚等。  

使用[PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/)选项，可以将导出的结构信息保存为带有结构的标签PDF。  

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


