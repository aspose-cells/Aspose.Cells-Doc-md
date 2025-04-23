---
title: إعدادات الحدود باستخدام C++
linktitle: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells في C++ لضبط نمط ولون حدود الخلايا. من خلال تعديل العرض والنمط واللون للحدود، يمكنك التحكم بشكل أكبر في مظهر الخلايا وظهورها.
keywords: Aspose.Cells، إعدادات حدود الخلايا، C++، عرض الحد، نمط الحد، لون الحد
type: docs
weight: 40
url: /ar/cpp/cells-border-settings/
---

## **إضافة حدود إلى الخلايا**

يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال، الحد العلوي هو الحد المضاف إلى أعلى موضع من الخلية. يمكن للمستخدمين أيضًا تعديل نمط وخطوط الألوان للحدود.

مع Aspose.Cells، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة كما في Microsoft Excel.

### **إضافة حدود إلى الخلايا**

توفر مكتبة Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) يمثل كائن من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

يقدم Aspose.Cells طريقة [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) في فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). تُستخدم طريقة [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) لتعيين نمط تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص لإضافة حدود إلى الخلايا.

#### **إضافة حدود إلى خلية**

يمكن للمطورين إضافة حدود إلى خلية باستخدام مجموعة [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) من كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). يُمرر نوع الحد كفهرس إلى مجموعة [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/). جميع أنواع الحدود معرفَة مسبقًا في تعداد [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**تعداد الحدود**

| **أنواع الحدود** | **الوصف** |
|------------------|-----------------|
| الحد السفلي     | خط الحد السفلي |
| القطع القطري للأسفل     | خط قطري من أعلى اليسار إلى أسفل اليمين |
| القطع القطري للأعلى       | خط قطري من أسفل اليسار إلى أعلى اليمين |
| الحد الأيسر       | خط الحد الأيسر |
| الحد الأيمن      | خط الحد الأيمن |
| الحد العلوي        | خط الحد العلوي |

تخزن مجموعة [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) جميع الحدود. يُمثل كل حد في مجموعة [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) بواسطة كائن [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) يوفر خصيتين، [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) و[**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) لضبط لون الخط ونمط الحد على التوالي.

لضبط لون خط الحد، اختر لونًا باستخدام تعداد اللون وقم بتعيينه لخاصية لون كائن الحد.

يتم ضبط نمط خط الحد عن طريق اختيار نمط خط من تعداد [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/).

**تعداد CellBorderType**

| **أنماط الخطوط**       | **الوصف**               |
|------------------------|-------------------------------|
| DashedDot               | خط مخطوط رفيع مغير |
| DashedDotDot            | خط مخطوط مع خطقطار رفيع |
| Dashed                | خط مخطط |
| Dotted                | خط نقطي |
| Double                | خط مزدوج |
| Hair                  | خط شعر |
| MediumDashDot         | خط مخطوط متوسط |
| MediumDashDotDot      | خط مخطوط مخطط متوسط |
| MediumDashed          | خط مخطط متوسط |
| None                  | بدون خط |
| Medium                | خط متوسط |
| SlantedDashDot        | خط مائل مخطوط متوسط |
| Thick                 | خط سميك |
| Thin                  | خط رقيق |

اختر أحد أنماط الخط ثم قم بتعيينه إلى خاصية [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) لكائن [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Visit Aspose!");

    Style style = cell.GetStyle();

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    cell.SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls");
    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يجب تعيين كل من نمط الخط ولونه في نفس الوقت. يجب أن يكون لنظامي الخطوط القطرية نفس النمط واللون.

{{% /alert %}}

#### **إضافة حدود لمجموعة من الخلايا**

من الممكن أيضًا إضافة حدود لنطاق من الخلايا بدلاً من خلية واحدة فقط. للقيام بذلك، أولاً، أنشئ نطاق خلايا عبر استدعاء طريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) لمجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). تأخذ المعلمات التالية:

- الصف الأول، الصف الأول من المجموعة.
- العمود الأول، يمثل العمود الأول من المجموعة.
- عدد الصفوف، عدد الصفوف في المجموعة.
- عدد الأعمدة، عدد الأعمدة في المجموعة.

تعيد طريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) كائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)، الذي يحتوي على النطاق المحدد من الخلايا. يوفر كائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) طريقة [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) التي تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

- **نوع الحد**، نوع الحد، مختار من تعداد [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).
- **نمط الخط**، نمط خط الحد، مختار من تعداد [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/).
- **اللون**، لون الخط، المحدد من تعداد الألوان.

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

    // Obtain the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
