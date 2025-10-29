---
title: الحصول على التحقق من صحة الخلية في ملفات ODS باستخدام C++
linktitle: الحصول على التحقق من الخلية في ملفات ODS
type: docs
weight: 180
url: /ar/cpp/get-cell-validation-in-ods-files/
description: تعلم كيفية الحصول على التحقق من صحة الخلية في ملفات ODS باستخدام Aspose.Cells for C++.
keywords: الحصول على التحقق من الخلية، الحصول على التحقق من الخلية 
---

## **الحصول على التحقق من الخلية في ملفات ODS**

مع Aspose.Cells for C++، يمكنك الحصول على التحقق المطبق على خلية في ملفات ODS. توفر الواجهة [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) من فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

يوضح رمز العينة التالي كيفية استخدام طريقة [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) بتحميل [ملف ODS المصدر](101089354.ods) وقراءة التحقق من صحة الخلية A9.

### **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
