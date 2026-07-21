---
title: تعطيل شرائط الجدول المحوري باستخدام C++
linktitle: تعطيل شريط جدول الدوران
type: docs
weight: 90
url: /ar/cpp/disable-pivot-table-ribbons/
description: تعلم كيفية تعطيل شرائط الجدول المحوري في ملفات Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 التقارير المعتمدة على الجدول المحوري مفيدة ولكنها عرضة للأخطاء إذا لم يكن لدى المستخدمين المستهدفين معرفة مفصلة بـ Excel لتكوين هذه التقارير. في هذه الحالات، ترغب المنظمات في تقييد قدرة المستخدمين على تعديل تقرير يعتمد على الجدول المحوري. الميزات الشائعة للجدول المحوري مثل إضافة مرشحات إضافية، slicers، الحقول، أو تغيير ترتيب بعض العناصر في التقرير غير موصى بها غالبًا لكل مستخدم. من ناحية أخرى، يجب أن يكون هؤلاء المستخدمون قادرين على تحديث التقرير واستخدام المرشحات أو slicers الموجودة. قدمت Aspose.Cells هذه القدرة للمطورين لتقييد المستخدمين من تغيير هذه التقارير أثناء إنشائها. لهذا الغرض، يوفر Excel ميزة تعطيل شريط أدوات الجدول المحوري، وتوفرها Aspose.Cells أيضًا. يمكن للمطورين تعطيل الشريط الذي يحتوي على أدوات لتعديل هذه التقارير.

{{% /alert %}}

## **تعطيل شريط الأدوات لجداول الدوران باستخدام PivotTable.EnableWizard**

 يوضح هذا المقتطف الكود كيفية تفعيل الميزة من خلال الوصول إلى جدول محوري من ورقة ثم تعيين [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) إلى **false**. يمكن تنزيل ملف جدول محوري نموذجي من [الرابط](pivot_table_test.xlsx).

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
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
