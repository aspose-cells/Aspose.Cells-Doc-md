---
title: إعدادات الحماية المتقدمة منذ Excel XP مع C++
linktitle: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/cpp/advanced-protection-settings-since-excel-xp/
description: تعلم كيفية تطبيق إعدادات الحماية المتقدمة في ملفات Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

منذ إصدار Excel 2002 أو XP، أضافت Microsoft العديد من إعدادات الحماية المتقدمة.

{{% /alert %}}

## **مقدمة**

تقييد أو السماح للمستخدمين بـ:

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج صفوف أو أعمدة أو روابط تشعبية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة المقدمة من Excel XP أو الإصدارات اللاحقة.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **أدوات**, اختر **الحماية** ثم **حماية الورقة**. سيتم عرض مربع الحوار.

لعرض إعدادات الحماية المتاحة في Excel 2016:

1. من القائمة **ملف**, اختر **حماية الدفتر** ثم **حماية الورقة الحالية**.
1. حدد **حماية الورقة** في قائمة **مراجعة**.

سيؤدي اتباع الخطوات المذكورة أعلاه إلى إظهار مربع حوار يمكنك من خلاله السماح أو تقييد ميزات ورقة العمل أو تطبيق كلمة مرور على ورقة العمل.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) خاصية [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) التي تُستخدم لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/) هي في الواقع كائن لفئة [**Protection**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/) التي تحتوي على عدة خصائص بوليانية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook excel(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Restricting users to delete columns of the worksheet
    worksheet.GetProtection().SetAllowDeletingColumn(false);

    // Restricting users to delete row of the worksheet
    worksheet.GetProtection().SetAllowDeletingRow(false);

    // Restricting users to edit contents of the worksheet
    worksheet.GetProtection().SetAllowEditingContent(false);

    // Restricting users to edit objects of the worksheet
    worksheet.GetProtection().SetAllowEditingObject(false);

    // Restricting users to edit scenarios of the worksheet
    worksheet.GetProtection().SetAllowEditingScenario(false);

    // Restricting users to filter
    worksheet.GetProtection().SetAllowFiltering(false);

    // Allowing users to format cells of the worksheet
    worksheet.GetProtection().SetAllowFormattingCell(true);

    // Allowing users to format rows of the worksheet
    worksheet.GetProtection().SetAllowFormattingRow(true);

    // Allowing users to format columns of the worksheet
    worksheet.GetProtection().SetAllowFormattingColumn(true);

    // Allowing users to insert hyperlinks in the worksheet
    worksheet.GetProtection().SetAllowInsertingHyperlink(true);

    // Allowing users to insert rows in the worksheet
    worksheet.GetProtection().SetAllowInsertingRow(true);

    // Allowing users to select locked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingLockedCell(true);

    // Allowing users to select unlocked cells of the worksheet
    worksheet.GetProtection().SetAllowSelectingUnlockedCell(true);

    // Allowing users to sort
    worksheet.GetProtection().SetAllowSorting(true);

    // Allowing users to use pivot tables in the worksheet
    worksheet.GetProtection().SetAllowUsingPivotTable(true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();

    return 0;
}
```

{{% alert color="primary" %}}

يرجى عدم استدعاء طريقة [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) من فصل [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) عند استخدام الخاصية [**GetProtection()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getprotection/). أيضًا، قم بحفظ الملف بصيغة Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط من Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد تحرير المستخدمين للخلايا، يجب قفل الخلايا قبل تطبيق أي إعدادات حماية. وإلا، يمكن تحرير الخلايا حتى وإن كانت ورقة العمل محمية. في Microsoft Excel XP، يمكن قفل الخلايا من خلال مربع الحوار التالي:

|**مربع الحوار لقفل الخلايا في Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن قفل الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells أيضًا. يمكن أن تحوي كل خلية تنسيق [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) يحتوي على خاصية Boolean، [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). قم بضبط الخاصية [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) على **true** أو **false** لقفل الخلية أو إلغاء قفلها.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Lock the style of cell A1
    worksheet.GetCells().Get(u"A1").GetStyle().SetIsLocked(true);

    // Protect the sheet
    worksheet.Protect(ProtectionType::All);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet protected successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
