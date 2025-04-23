---
title: الحصول على كائن الخلية بواسطة DisplayName لحقل Pivot في جدول Pivot باستخدام C++
linktitle: الحصول على كائن الخلية بواسطة DisplayName لحقل Pivot في جدول Pivot
type: docs
weight: 70
url: /ar/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: تعلم كيفية استرجاع كائن الخلية بواسطة اسم العرض لعمود محوري وتطبيق التنسيق باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تقدم Aspose.Cells أسلوب [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/)، والذي يمكنك من خلاله الوصول إلى كائن الخلية بواسطة اسم العرض لحقل محوري. يكون هذا الأسلوب مفيدًا عندما ترغب في إبراز أو تنسيق عنوان الحقل المحوري الخاص بك. يوضح هذا المقال كيف تسترجع كائن الخلية بواسطة اسم العرض لحقل البيانات ثم تطبق عليه التنسيق.

{{% /alert %}}

## **الحصول على كائن الخلية بواسطة DisplayName لحقل Pivot في جدول Pivot**

الكود التالي يفتح أول جدول محوري في ورقة العمل ثم يسترجع الخلية بواسطة اسم العرض لثاني حقل بيانات من الجدول المحوري. ثم يغير لون التعبئة ولون الخط للخلية إلى اللون الأزرق الفاتح والأسود، على التوالي. تظهر في الصور لقطات شاشة لكيفية ظهور الجدول المحوري قبل وبعد تنفيذ الكود.

|**جدول مفصلي - قبل**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**جدول مفصلي - بعد**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
