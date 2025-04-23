---
title: عرض الصيغ بدلًا من القيم في ورقة عمل باستخدام C++
linktitle: عرض الصيغ بدلًا من القيم
type: docs
weight: 20
url: /ar/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: يوفر هذا المقال مثالاً برمجياً لاستخدام واجهة برمجة التطبيقات C++ لعرض الصيغ بدلاً من القيم في ورقة عمل أو جدول بيانات إكسل.
---

{{% alert color="primary" %}}

من الممكن عرض الصيغ بدلاً من القيم المحسوبة في Microsoft Excel باستخدام خيار **عرض الصيغ** من شريط العلامات **الصيغ**. عند عرض الصيغ، يعرض Microsoft Excel الصيغ في ورقة العمل. يمكنك تحقيق نفس الشيء باستخدام Aspose.Cells.

{{% /alert %}}

يوفر Aspose.Cells خاصية [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/). اضبط هذا على **صحيح** لإعداد Microsoft Excel لعرض الصيغ.

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
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
