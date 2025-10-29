---
title: حماية مشروع VBA لكائن دفتر عمل إكسل بكلمة مرور باستخدام C++
linktitle: حماية كلمة السر لمشروع VBA لسجل العمل الخاص بـ Excel
type: docs
weight: 10
url: /ar/cpp/password-protect-the-vba-project-of-excel-workbook/
description: تعلم كيفية حماية مشروع VBA لكائن دفتر عمل إكسل باستخدام Aspose.Cells مع C++.
---

## **حماية مشروع VBA لملف إكسل بكلمة مرور في C++**

يمكنك حماية مشروع VBA (تطبيقات Visual Basic) لدفترك باستخدام Aspose.Cells عبر استخدام [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/) الأسلوب.

## **الكود المثالي**

يُحمّل الشيفرة التالية ملف إكسل عينة، ويصل إليها مشروع VBA الخاص بها، ويحميه بكلمة مرور. وأخيرًا، يحفظه كملف إكسل ناتج.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";

    // Load the source Excel file
    Workbook wb(inputFilePath);

    // Access the VBA project of the workbook
    VbaProject vbaProject = wb.GetVbaProject();

    // Lock the VBA project for viewing with password
    vbaProject.Protect(true, u"11");

    // Save the output Excel file
    wb.Save(outputFilePath);

    std::cout << "VBA project password protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
