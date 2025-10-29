---
title: عرض نمط تنسيق التاريخ المخصص g و ge mm dd باستخدام C++
description: Aspose.Cells هو مكتبة C++ للعمل مع جداول البيانات يدعم عرض التواريخ باستخدام أنماط تنسيق التاريخ المخصصة g و ge . تصف هذه المقالة كيفية عرض أنماط تنسيق التاريخ المخصصة باستخدام مكتبة Aspose.Cells بحيث يمكن للمستخدمين التحكم في كيفية عرض التواريخ إذا رغبوا في ذلك.
keywords: Aspose.Cells، مكتبة C++، جدول بيانات إلكتروني، تنسيق تاريخ مخصص، عرض، نمط g ، نمط ge ، تحكم في العرض
type: docs
weight: 160
url: /ar/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

أصبح بإمكان Aspose.Cells الآن تقديم أنماط صيغ التاريخ المخصصة مثل g، ge.mm.dd وما شابه. يرجى التحقق من ملف جدول البيانات المرفق [ملف Excel المصدر] (5112361.xlsx) و [ملف PDF المحول] (5112360.pdf) بواسطة Aspose.Cells للرجوع إليه.

{{% /alert %}}

يقوم الكود النموذجي التالي بتحويل [ملف Excel المصدر] (5112361.xlsx) الذي يحتوي على قيم تاريخية بأنماط صيغ مخصصة مثل g و ge.mm.dd إلى [PDF الناتج] (5112360.pdf).

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

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
