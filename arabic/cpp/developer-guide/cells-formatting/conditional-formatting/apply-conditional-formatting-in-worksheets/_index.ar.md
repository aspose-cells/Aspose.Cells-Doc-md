---
title: تطبيق التنسيق الشرطي في أوراق العمل باستخدام C++
linktitle: تطبيق التنسيق الشرطي
description: كيفية استخدام مكتبة Aspose.Cells في C++ لتطبيق التنسيق الشرطي في أوراق العمل. من خلال تعديل هذه المعايير، يمكنك السيطرة بشكل أكبر على مظهر وتنسيق الخلايا.
keywords: Aspose.Cells، التنسيق الشرطي، C++، ورقة العمل، التنسيق
type: docs
weight: 130
url: /ar/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

يهدف هذا المقال إلى توفير فهم مفصل حول كيفية إضافة التنسيق الشرطي إلى مجموعة من الخلايا في ورقة عمل.

التنسيق الشرطي هو ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق التنسيقات على مجموعة من الخلايا وأن يتغير ذلك التنسيق اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكن أن تكون خلفية الخلية حمراء لتسليط الضوء على قيمة سالبة، أو يمكن أن لون النص يكون أخضرًا لقيمة موجبة. عندما تفي قيمة الخلية بشرط التنسيق، يتم تطبيق التنسيق. إذا لم تف بقيمة الخلية شرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية.

من الممكن تطبيق التنسيق الشرطي بواسطة Office Automation، ولكن ذلك يأتي مع عيوبه. هناك أسباب وقضايا عديدة متضمنة: مثلاً، الأمان، الاستقرار، التوسع السريع والسرعة. السبب الرئيسي للبحث عن حل آخر هو أن Microsoft نفسها تنص بشدة على عدم استخدام Office Automation لحلول البرنامج.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة التحكم، وإضافة التنسيق الشرطي للخلايا ببضعة أسطر بسيطة باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

## **استخدام Aspose.Cells لتطبيق تنسيق مشروط بناءً على قيمة الخلية**

1. **قم بتنزيل وتثبيت Aspose.Cells**.
   1. قم بتنزيل Aspose.Cells for C++.
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
   جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.
1. **إنشاء مشروع**.
   ابدأ بيئة تطوير C++ الخاصة بك وأنشئ تطبيق وحدة تحكم جديد.
1. **إضافة المراجع**.
   أضف مرجعًا إلى Aspose.Cells في مشروعك، على سبيل المثال، أضف مرجعًا إلى ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. **تطبيق التنسيق الشرطي استنادًا إلى قيمة الخلية**.
   إليك الكود المستخدم لإنجاز المهمة. يطبق التنسيق الشرطي على خلية.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

عند تنفيذ الكود أعلاه، يُطبق التنسيق الشرطي على الخلية “A1” في ورقة العمل الأولى من ملف الإخراج (output.xls). يعتمد التنسيق الشرطي المطبق على A1 على قيمة الخلية. إذا كانت قيمة A1 بين 50 و100، يكون لون الخلفية أحمر بسبب التنسيق الشرطي المطبق.

## **استخدام Aspose.Cells لتطبيق التنسيق الشرطي بناءً على الصيغة**

1. **تطبيق التنسيق الشرطي باستخدام صيغة (قطعة الكود)**
   أدناه هو الكود لإنجاز المهمة. يتم تطبيق التنسيق الشرطي على B3.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

عند تنفيذ الكود أعلاه، يُطبق التنسيق الشرطي على الخلية “B3” في ورقة العمل الأولى من ملف الإخراج (output.xls). يعتمد التنسيق الشرطي المطبق على الصيغة التي تحسب قيمة “B3” كمجموع B1 و B2.
{{< app/cells/assistant language="cpp" >}}
