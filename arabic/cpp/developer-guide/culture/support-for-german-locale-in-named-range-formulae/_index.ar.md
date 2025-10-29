---
title: دعم إعدادات اللغة الألمانية في صيغ النطاقات المسماة باستخدام C++
linktitle: دعم اللغة الألمانية في صيغ النطاقات المسماة
type: docs
weight: 60
url: /ar/cpp/support-for-german-locale-in-named-range-formulae/
description: تعلم كيفية التعامل مع صيغ النطاقات المسماة باللغة الألمانية باستخدام Aspose.Cells مع C++.
---

يتم كتابة الصيغ الإنجليزية في المناطق المسماة. يمكن فتح هذا الملف Excel في بيئة حيث تم تكوين النظام ليكون باللغة الألمانية؛ ومع ذلك، ستتم ترجمة الصيغة الإنجليزية إلى اللغة الألمانية. توضح المثال التالي هذه الخاصية، لكنها تتطلب وجود Excel مثبت باللغة الألمانية وتعيين نظام التشغيل إلى اللغة الألمانية أيضًا.

يمكن تنزيل ملف نموذجي لاختبار هذه الميزة من الرابط التالي:

[sampleNamedRangeTest.xlsm](73990165.xlsm)

```c++
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

    // Define the name and formula for the named range
    const U16String name(u"HasFormula");
    const U16String value(u"=GET.CELL(48, INDIRECT(\"ZS\",FALSE))");

    // Load the source workbook
    Workbook wbSource(srcDir + u"sampleNamedRangeTest.xlsm");

    // Get the worksheet collection
    WorksheetCollection wsCol = wbSource.GetWorksheets();

    // Add a new named range and get its index
    int32_t nameIndex = wsCol.GetNames().Add(name);

    // Get the named range by index
    Name namedRange = wsCol.GetNames().Get(nameIndex);

    // Set the formula for the named range
    namedRange.SetRefersTo(value);

    // Save the workbook with the new named range
    wbSource.Save(outDir + u"sampleOutputNamedRangeTest.xlsm");

    std::cout << "Named range added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
