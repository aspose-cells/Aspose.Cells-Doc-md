---
title: إخفاء عرض القيم الصفرية في ورقة العمل باستخدام C++
linktitle: إخفاء عرض القيم الصفرية في ورقة العمل
type: docs
weight: 50
url: /ar/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: توضح لك هذه المقالة رمزًا برمجيًا يشرح كيفية إخفاء القيم الصفرية بشكل برمجي في جدول Excel باستخدام مكتبة أو واجهة برمجة التطبيقات C++.
keywords: إخفاء القيم الصفرية في ورقة عمل إكسل باستخدام C++
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى إخفاء القيم الصفرية في جدول بيانات. قد يكون اختيار شخصي أو معيار تنسيق.

{{% /alert %}} 

لإخفاء القيم الصفرية في ورقة العمل في Microsoft Excel (على سبيل المثال Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**، ثم حدد علامة تبويب **العرض**.
1. ألغِ تحديد خيار **قيم الصفر**.
1. انقر على **موافق**.

الرجاء رؤية الشيفرة المثالية التالية التي تظهر إخفاء الأصفار باستخدام Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
