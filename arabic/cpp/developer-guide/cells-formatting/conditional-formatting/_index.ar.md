---
title: تعيين التنسيقات الشرطية لملفات إكسل و ODS باستخدام C++
linktitle: تنسيقات مشروطة
type: docs
weight: 60
url: /ar/cpp/conditional-formatting/
description: كيفية تطبيق التنسيقات الشرطية على ملفات إكسل و ODS باستخدام C++
keywords: تطبيق تنسيقات مشروطة 
---

## **مقدمة**

تعتبر التنسيق الشرطي ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق تنسيقات على خلية أو مجموعة من الخلايا وجعل تنسيق ذلك يتغير اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكنك جعل الخلية تظهر بخط عريض فقط عندما تكون قيمة الخلية أكبر من 500. عندما تفي قيمة الخلية بالشرط، يتم تطبيق التنسيق المحدد على الخلية. إذا لم تفي قيمة الخلية بشرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel، حدد **تنسيق** ثم **التنسيق الشرطي** لفتح مربع حوار التنسيق الشرطي.

Aspose.Cells تدعم تطبيق التنسيق الشرطي على الخلايا أثناء التشغيل. يوضح هذا المقال كيفية القيام بذلك. كما يوضح كيفية حساب اللون الذي يستخدمه Excel لتنسيق اللون الشرطي.

## **تطبيق التنسيق الشرطي**

Aspose.Cells تدعم التنسيق الشرطي بعدة طرق:

- باستخدام جدول البيانات للمصمم
- باستخدام طريقة النسخ.
- إنشاء التنسيق الشرطي أثناء التشغيل.

### **استخدام جدول البيانات للمصمم**

يمكن للمطورين إنشاء جدول بيانات للمصمم يحتوي على تنسيق شرطي في Microsoft Excel ثم فتح هذا الجدول بواسطة Aspose.Cells. تحمل Aspose.Cells وتحفظ جدول البيانات الخاص بالمصمم، مع الإبقاء على أي إعدادات تنسيق شرطي.

### **استخدام طريقة النسخ**

تسمح Aspose.Cells للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء الطريقة [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **تطبيق التنسيق الشرطي أثناء التشغيل**

Aspose.Cells تتيح لك إضافة وإزالة التنسيق الشرطي أثناء التشغيل. الأمثلة البرمجية أدناه تُظهر كيفية تحديد التنسيق الشرطي:

1. قم بإنشاء ورقة العمل.
1. أضف تنسيق شرطي فارغ.
1. حدد النطاق الذي ينبغي تطبيق التنسيق عليه.
1. حدد شروط التنسيق.
4. حفظ الملف.

بعد هذا المثال يأتي عدد من الأمثلة الصغيرة الأخرى التي توضح كيفية تطبيق إعدادات الخط، إعدادات الحدود، وأنماط.

أضاف Excel 2007 المزيد من التنسيق الشرطي المتقدم الذي تدعمه أيضًا Aspose.Cells. الأمثلة هنا، توضح كيفية استخدام التنسيق البسيط، والأمثلة ك Excel 2007 تظهر كيفية تطبيق التنسيق الشرطي المتقدم أكثر.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **تعيين الخط**

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يمكنك تغيير نمط الخط فقط، لون النص، نمط التسطير، ونمط الإشطار فقط.

{{% /alert %}}

### **تعيين الحدود**

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يمكنك استخدام أنماط الخطوط الرفيعة فقط لحدود التخطيط. الخطوط المائلة غير مسموح بها.

{{% /alert %}}

### **تعيين النمط**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مواضيع متقدمة**
- [إضافة التدرج اللوني ثنائي اللون والثلاثي اللون](/cells/ar/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [تطبيق تنسيقات متقدمة للتنسيق](/cells/ar/cpp/apply-advanced-conditional-formatting/)
- [تطبيق التنسيق الشرطي في الأوراق العمل](/cells/ar/cpp/apply-conditional-formatting-in-worksheets/)
- [تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي](/cells/ar/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [توليد صور شريط بيانات التنسيق الشرطي](/cells/ar/cpp/generate-conditional-formatting-databars-images/)
- [الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
