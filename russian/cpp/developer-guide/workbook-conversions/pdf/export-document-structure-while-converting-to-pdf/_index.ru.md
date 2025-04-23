---  
title: Экспортировать структуру документа при конвертации в PDF на C++  
linktitle: Экспорт структуры документа при конвертации в PDF  
type: docs  
weight: 360  
url: /ru/cpp/export-document-structure-while-converting-to-pdf/  
description: Узнайте, как экспортировать структуру документа при преобразовании в PDF с помощью Aspose.Cells на C++.  
---  

Функции логической структуры PDF обеспечивают механизм включения информации о структуре содержимого документа в PDF. Aspose.Cells сохраняет информацию о структуре из документа Microsoft Excel, такую как ячейки, строки, таблицы, листы, изображения, фигуры, заголовки/колонтитулы и т.д.  

С помощью опции [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/), вы можете сохранить в структурированный PDF с экспортированной структурой документа.  

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


