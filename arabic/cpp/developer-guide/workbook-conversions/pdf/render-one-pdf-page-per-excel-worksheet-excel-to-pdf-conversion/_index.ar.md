---
title: عرض صفحة PDF واحدة لكل ورقة عمل Excel  تحويل Excel إلى PDF مع C++
type: docs
weight: 100
url: /ar/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: تحويل أوراق عمل Excel إلى صيغة PDF مع صفحة واحدة لكل ورقة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

عند العمل مع ملفات Excel كبيرة جدًا (على سبيل المثال، مصنف يحتوي على العديد من الأوراق، وكل منها يحتوي على 50 عمودًا و300 أو أكثر من الصفوف)، قد ترغب في أن يعرض إذًا المخرج PDF صفحة واحدة لكل ورقة، بغض النظر عن حجم الورقة. هذا يعني أن كل صفحة قد تكون ذات حجم صفحة مختلف بشكل جذري. يمكن تحقيق ذلك باستخدام Aspose.Cells for C++.

{{% /alert %}} 

يرجى الاطلاع على الكود النموذجي التالي الذي يحول ملف Excel مع العديد من الأوراق إلى PDF.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

إذا تم ضبط خيار [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) على **true**، سيتم عرض جميع محتويات الورقة على صفحة PDF واحدة.

{{% /alert %}} {{% alert color="primary" %}} 

إذا كان جدول البيانات الخاص بك يحتوي على صيغ، من الأفضل استدعاء [Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل عرض الجدول كـ PDF. هذا يضمن إعادة حساب القيم المعتمدة على الصيغة، ويتم عرض القيم الصحيحة في PDF.

{{% /alert %}}
