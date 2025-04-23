---
title: تحويل الجدول إلى ODS باستخدام C++
linktitle: تحويل الجدول إلى ملف ODS
type: docs
weight: 70
url: /ar/cpp/convert-table-to-ods/
description: تحويل ملف Excel يحتوي على جدول إلى تنسيق ODS باستخدام Aspose.Cells مع C++.
---

يدعم Aspose.Cells تحويل ملف Excel يحتوي على جدول إلى ملف ODS. عليك فقط حفظ الملف بتنسيق ODS وسيحتوي ملف ODS الناتج على جدول يعمل بشكل صحيح.

## كود عينة

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C++

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Open an existing file that contains a table/list object in it
    U16String inputFilePath = sourceDir + u"SampleTable.xlsx";
    Workbook workbook(inputFilePath);

    // Save the file in ODS format
    workbook.Save(outputDir + u"ConvertTableToOds_out.ods");

    std::cout << "Conversion to ODS completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

الملف ODS الناتج من كود العينة مرفق للرجوع إليه.

[**Output ODS File**](ConvertTableToOds_out.ods)
