---
title: طباعة التعليقات أثناء الحفظ إلى PDF باستخدام C++
linktitle: طباعة التعليقات أثناء الحفظ إلى صيغة PDF
type: docs
weight: 10
url: /ar/cpp/print-comments-while-saving-to-pdf/
description: تعلم كيفية طباعة التعليقات أثناء حفظ ملفات إكسل إلى PDF باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يسمح Microsoft Excel بطباعة التعليقات عند الطباعة أو الحفظ بصيغة PDF مع الخيارات التالية:

- لا شيء
- في نهاية الجدول
- كما هو معروض على الجدول

يوفر Aspose.Cells التعداد [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) لدعم نفس الميزة. يحتوي تعداد [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) على الأعضاء التالية:

- PrintNoComments
- PrintInPlace
- PrintSheetEnd

{{% /alert %}}

## **طباعة التعليقات عند الحفظ إلى PDF**

يوضح الكود التالي كيفية استخدام [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) لطباعة التعليقات عند الحفظ إلى PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleWorkbookWithComments.xlsx";

    // Path of output pdf file
    U16String outputFilePath = outDir + u"PrintCommentWhileSavingToPdf_out.pdf";

    // Create a workbook from source Excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    /*
     * For print no comments use "PrintCommentsType::PrintNoComments"
     * and for print the comments as displayed on sheet use "PrintCommentsType::PrintInPlace"
     * For Print the comments at the end of sheet we use "PrintCommentsType::PrintSheetEnd"
    */
    worksheet.GetPageSetup().SetPrintComments(PrintCommentsType::PrintSheetEnd);

    // Save workbook in pdf format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with comments printed at the end of the sheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
