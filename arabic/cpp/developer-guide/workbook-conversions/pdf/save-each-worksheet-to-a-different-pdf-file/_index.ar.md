---
title: حفظ كل ورقة عمل في ملف PDF مختلف باستخدام C++
linktitle: حفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 130
url: /ar/cpp/save-each-worksheet-to-a-different-pdf-file/
description: تعلم كيفية حفظ كل ورقة عمل في ملف Excel إلى ملف PDF منفصل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

يدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على الصور، الرسوم البيانية، وغيرها) إلى مستندات PDF. يمكن لـ Aspose.Cells for C++ العمل بشكل مستقل لتحويل جدول بيانات إلى PDF ولا حاجة لاستخدام Aspose.PDF لـ C++ لهذا التحويل. لا تتطلب عملية التحويل إنشاء أو استخدام ملفات مؤقتة حيث يمكن إتمامها بالكامل في الذاكرة.

{{% /alert %}} 

## **حفظ كل ورقة عمل في ملف PDF مختلف**
إذا كنت بحاجة إلى حفظ كل ورقة عمل في ملف Excel الخاص بك لإنشاء ملفات PDF مختلفة، يمكنك تحقيق ذلك بسهولة. يمكنك محاولة تعيين فهرس ورقة واحدة إلى [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) على حدة لعرضها كـ PDF.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

إذا كانت جداول البيانات الخاصة بك تحتوي على صيغ، فمن الأفضل الاتصال بـ [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) قبل تصيير الجدول إلى PDF. سيساعد ذلك على إعادة حساب القيم المعتمدة على الصيغ، وإظهار القيم الصحيحة في PDF.

{{% /alert %}}
