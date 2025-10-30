---  
title: C++ ile PDF ye Dönüşüm Sırasında Belge Yapısını Dışa Aktarma  
linktitle: PDF ye Dönüştürürken Belge Yapısını Dışa Aktar  
type: docs  
weight: 360  
url: /tr/cpp/export-document-structure-while-converting-to-pdf/  
description: Aspose.Cells kullanarak C++ ile PDF ye dönüştürürken belge yapısını nasıl dışa aktaracağınızı öğrenin.  
---  

PDF mantıksal yapısı olanakları, belge içeriği yapısına ilişkin bilgileri PDF dosyasına dahil etmek için bir mekanizma sağlar. Aspose.Cells, Microsoft Excel belgesinden hücre, satır, tablo, çalışma sayfası, resim, şekil, üstbilgi/altbilgi gibi yapısal bilgileri korur.  

[PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/) seçeneği ile, belge yapısı dışa aktarılmış bir işaretli PDF olarak kaydedebilirsiniz.  

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


{{< app/cells/assistant language="cpp" >}}
