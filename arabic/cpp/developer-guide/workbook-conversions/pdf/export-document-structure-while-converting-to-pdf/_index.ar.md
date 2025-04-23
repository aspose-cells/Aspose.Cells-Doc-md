---  
title: تصدير بنية المستند أثناء التحويل إلى PDF باستخدام C++  
linktitle: تصدير هيكل الوثيقة أثناء التحويل إلى PDF  
type: docs  
weight: 360  
url: /ar/cpp/export-document-structure-while-converting-to-pdf/  
description: تعلم كيف تصدر بنية المستند أثناء التحويل إلى PDF باستخدام Aspose.Cells في C++.  
---  

توفر مرافق الهيكل المنطقي لملف PDF آلية لدمج معلومات حول بنية محتوى المستند في ملف PDF. يحفظ Aspose.Cells المعلومات عن بنية المستند من مستند Excel من Microsoft، مثل الخلية، الصف، الجدول، ورقة العمل، الصورة، الشكل، الرأس/التذييل، وما إلى ذلك.  

مع خيار [PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/)، يمكنك حفظ ملف PDF موسوم مع تصدير بنية المستند.  

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


