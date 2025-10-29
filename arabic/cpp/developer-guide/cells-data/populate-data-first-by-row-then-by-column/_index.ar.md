---
title: ملء البيانات أولاً بواسطة الصف ثم بواسطة العمود باستخدام ++C
linktitle: تعبئة البيانات أولاً حسب الصف ثم حسب العمود
type: docs
weight: 1000
url: /ar/cpp/populate-data-first-by-row-then-by-column/
description: تعلم كيفية ملء البيانات أولاً بواسطة الصف ثم بواسطة العمود من خلال API Aspose.Cells for C++.
keywords: املأ البيانات أولاً حسب الصف ثم حسب العمود، ضع البيانات أولاً حسب الصف ثم حسب العمود، أضف البيانات أولاً حسب الصف ثم حسب العمود، إدخال البيانات عالية الأداء، إضافة البيانات عالية الأداء
---

{{% alert color="primary" %}} 

تحسين أداء ملف البيانات عن طريق تعبئته بالبيانات أولاً حسب الصف ثم حسب العمود.

{{% /alert %}} 

وضع البيانات في التسلسل A1، B1، A2، B2 أسرع من A1، A2، B1، B2. إذا كان هناك العديد من الخلايا في ورقة العمل واتبعت التسلسل الثاني، أي ملئ البيانات حسب الصف، يمكن أن يجعل هذا النصيب أسرع بكثير.

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
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
