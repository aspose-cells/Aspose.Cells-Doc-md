---
title: نسخ ارتفاعات الصفوف من النطاق المصدر إلى النطاق الهدف باستخدام C++
linktitle: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة
type: docs
weight: 590
url: /ar/cpp/copy-row-heights-of-source-range-to-destination-range/
description: تعلم كيفية نسخ ارتفاعات الصفوف من نطاق مصدر إلى نطاق هدف باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 أحيانًا، يحتاج المستخدمون إلى نسخ ارتفاعات الصفوف من نطاق مصدر إلى نطاق هدف. يوفر Aspose.Cells قيمة [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) لهذا الغرض. عند تعيين الخاصية [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) باستخدام قيمة [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/)، سيتم نسخ ارتفاعات جميع الصفوف داخل النطاق المصدر إلى النطاق الهدف.

{{% /alert %}}

 يوضح رمز العينة التالي كيف يمكن استخدام قيمة [**PasteType::RowHeights**](https://reference.aspose.com/cells/cpp/aspose.cells/pastetype/) لنسخ ارتفاعات الصفوف من نطاق مصدر إلى نطاق هدف. عند فتح ملف Excel الناتج الذي تم إنشاؤه بواسطة هذا الرمز في Microsoft Excel، ستلاحظ أن ارتفاعات الصفوف في النطاق الهدف مطابقة تمامًا لارتفاعات الصفوف في النطاق المصدر.

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

    // Create workbook object
    Workbook workbook;

    // Source worksheet
    Worksheet srcSheet = workbook.GetWorksheets().Get(0);

    // Add destination worksheet
    Worksheet dstSheet = workbook.GetWorksheets().Add(u"Destination Sheet");

    // Set the row height of the 4th row. This row height will be copied to destination range
    srcSheet.GetCells().SetRowHeight(3, 50);

    // Create source range to be copied
    Range srcRange = srcSheet.GetCells().CreateRange(u"A1:D10");

    // Create destination range in destination worksheet
    Range dstRange = dstSheet.GetCells().CreateRange(u"A1:D10");

    // PasteOptions, we want to copy row heights of source range to destination range
    PasteOptions opts;
    opts.SetPasteType(PasteType::RowHeights);

    // Copy source range to destination range with paste options
    dstRange.Copy(srcRange, opts);

    // Write informative message in cell D4 of destination worksheet
    dstSheet.GetCells().Get(u"D4").PutValue(u"Row heights of source range copied to destination range");

    // Save the workbook in xlsx format
    workbook.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Row heights copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
