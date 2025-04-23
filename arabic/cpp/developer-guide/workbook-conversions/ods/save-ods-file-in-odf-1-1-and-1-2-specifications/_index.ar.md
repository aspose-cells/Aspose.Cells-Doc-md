---
title: حفظ ملف ODS في مواصفات ODF 1.1 و 1.2 و 1.3 باستخدام C++
linktitle: الحفظ كـ ODF 1.1 و 1.2 و 1.3
description: تحويل Excel إلى ODF 1.1 و 1.2 و 1.3 باستخدام Aspose.Cells باستخدام C++.
type: docs
weight: 230
url: /ar/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells حفظ ملف ODS (**جداول بيانات المستند المفتوح**) بصيغة ODF (**صيغة المستند المفتوح**) وفقًا لمواصفات 1.1 و 1.2 و 1.3. لدى Aspose.Cells خاصية [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) التي تحدد إصدار ODF لحفظ ملفات ODS. القيمة الافتراضية لهذه الخاصية هي [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/)، لذلك الملف ODS المحفوظ بدون ضبط هذه الخاصية يستخدم مواصفات 1.2.

{{% /alert %}}

يفترض الكود النموذجي أدناه إنشاء كائن عمل، يضيف قيمة إلى الخلية A1 في الورقة الأولى ثم يقوم بحفظ ملف ODS وفقًا لمواصفات ODF 1.1 و 1.2 و 1.3. بشكل افتراضي، يتم حفظ ملف ODS بمواصفات ODF 1.2.

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
