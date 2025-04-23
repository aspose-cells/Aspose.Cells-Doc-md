---
title: إعدادات التعبئة باستخدام C++
linktitle: إعدادات التعبئة
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جدول البيانات. تدعم تعيين إعدادات التعبئة للخلايا، مما يسمح للمستخدمين بتخصيص خلفية ونمط الخلايا. ستقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لضبط إعدادات تعبئة الخلايا.
keywords: Aspose.Cells، خلايا، إعدادات التعبئة، خلفية، نمط
type: docs
weight: 50
url: /ar/cpp/cells-fill-settings/
---

## **الألوان وأنماط الخلفية**

يمكن لبرنامج Microsoft Excel تعيين ألوان الأمام (الإطار) والخلفية (تعبئة) للخلايا وأنماط الخلفية.

تدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيفية استخدام هذه الميزات باستخدام Aspose.Cells.

### **تعيين الألوان وأنماط الخلفية**

توفر أسبوس.خلايات فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) يُمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) لديها [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) و [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) الأساليب التي تستخدم للحصول وتعيين تنسيق الخلية. يوفر فئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص لضبط لوني النص الأمامي والخلفية للخلايا. توفر Aspose.Cells تعدادًا [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) يحتوي على مجموعة من أنواع أنماط الخلفية المحددة مسبقًا كما هو موضح أدناه.

|**أنماط الخلفية**|**الوصف**|
| :- | :- |
|DiagonalCrosshatch|تمثل نمط شفة الصليب المائل|
|DiagonalStripe| يمثل نمط خط مائل |
|Gray6| يمثل نمط رمادي بنسبة 6.25٪ |
|Gray12| يمثل نمط رمادي بنسبة 12.5٪ |
|Gray25| يمثل نمط رمادي بنسبة 25٪ |
|Gray50| يمثل نمط رمادي بنسبة 50٪ |
|Gray75| يمثل نمط رمادي بنسبة 75٪ |
|HorizontalStripe| يمثل نمط خط أفقي |
|None| يمثل عدم وجود خلفية |
|ReverseDiagonalStripe| يمثل نمط خط مائل عكسي |
|Solid| يمثل نمط صلب |
|ThickDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة سميكة |
|ThinDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة رفيعة |
|ThinDiagonalStripe| يمثل نمط خط مائل رفيع |
|ThinHorizontalCrosshatch| يمثل نمط علامة تقاطع أفقي رفيعة |
|ThinHorizontalStripe| يمثل نمط خط أفقي رفيع |
|ThinReverseDiagonalStripe| يمثل نمط خط مائل عكسي رفيع |
|ThinVerticalStripe| يمثل نمط خط عمودي رفيع |
|VerticalStripe| يمثل نمط خط عمودي |

في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **مهم معرفته**

{{% alert color="primary" %}}

- لتعيين لون الخلفية أو اللون الأمامي لخلية ما، استخدم خصائص [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) أو [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) لكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). سوف تؤثر كلا الخصائص فقط إذا تم تكوين خصية [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) لكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).
- تعيين الظل للخلية تحدد خاصية [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) لون الخلية.
  تحدد الخاصية [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) نوع نمط الخلفية المستخدمة للألوان الأمامية أو الخلفية. يوفر Aspose.Cells تعدادًا، [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/). يحتوي على مجموعة من الأنماط القياسية المحددة مسبقًا لأنماط الخلفية.
- إذا قمت بتحديد قيمة *BackgroundType.None* من تعداد [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/)، لن يتم تطبيق اللون الأمامي.
  بالمثل، لن يتم تطبيق اللون الخلفي إذا قمت باختيار القيم *BackgroundType.None* أو *BackgroundType.Solid*.
- عند استرجاع لون السطوع/التعبئة للخلية، إذا كان [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) يساوي *BackgroundType.None*، سيقوم [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) بإرجاع *Color.Empty*.

{{% /alert %}}

### **تطبيق تأثيرات تعبئة التدرج**

لتطبيق تأثيرات تعبئة التدرج المرغوبة على الخلية، استخدم الطريقة [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) لكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) وفقًا لذلك.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells، يمكن للمستخدم استخدام الألوان الموجودة في اللوحة بالإضافة إلى الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

### **إضافة ألوان مخصصة إلى اللوحة**

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel. تقدم فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) طريقة [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}
