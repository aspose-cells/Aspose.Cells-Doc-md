---
title: تحديد نمط تنسيق مخصص لـ DBNum باستخدام C++
linktitle: تحديد تنسيق نمط DBNum المخصص
description: مكتبة Aspose.Cells هي مكتبة C++ للعمل مع ملفات الجدول الإلكتروني وتدعم تنسيق التواريخ والأرقام باستخدام أنماط تنسيق مخصصة. ستوضح هذه المقالة كيفية استخدام مكتبة Aspose.Cells لتحديد نمط التنسيق المخصص dbnum لتمكين المستخدمين من التحكم في عرض الأرقام بشكل أدق.
keywords: مكتبة Aspose.Cells، مكتبة C++، جدول إلكتروني، نمط تنسيق مخصص، تنسيق، dbnum ، التحكم في العرض
type: docs
weight: 110
url: /ar/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **سيناريوهات الاستخدام المحتملة**

تدعم مكتبة Aspose.Cells تنسيق نمط مخصص *DBNum*. على سبيل المثال، إذا كانت قيمة الخلية 123 وقد حددت تنسيقها المخصص كـ [DBNum2][$-804]General فستُعرض كالرمز 壹佰贰拾叁. يمكنك تحديد تنسيقك المخصص للخلية باستخدام طريقة [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) وخصيصة [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **الكود المثالي**

يُظهر الكود النموذجي التالي كيفية تحديد تنسيق نمط مخصص *DBNum*. يرجى مراجعة [ملف PDF الناتج](43352081.pdf) للمزيد من المساعدة.

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
