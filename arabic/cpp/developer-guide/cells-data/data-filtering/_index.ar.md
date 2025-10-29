---
title: تصفية البيانات باستخدام C++
linktitle: تصفية البيانات
type: docs
weight: 85
url: /ar/cpp/data-filtering/
description: تعلم كيفية إضافة تصفية بيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: إضافة مرشح حسب اللون، إضافة مرشحات التاريخ، إضافة مرشحات الأرقام، إضافة مرشح ديناميكي، إضافة مرشحات النص، إضافة مرشح مخصص بحسب الاحتواء، إضافة مرشح مخصص بدون الاحتواء، إضافة مرشح مخصص يبدأ بـ، إضافة مرشح مخصص ينتهي بـ
---

{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة لتصفية بيانات ورق العمل تلقائيًا. تدعم Aspose.Cells بشكل كامل ميزات تصفية بيانات Microsoft Excel الملقم. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel، وكيفية كتابة الشفرات باستخدام Aspose.Cells.

{{% /alert %}}

## **عنصرية البيانات**

التصفية التلقائية هي أسرع طريقة لتحديد العناصر الوحيدة التي ترغب في عرضها في قائمة. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر في القائمة وفقًا لمعايير محددة. تصفية بناءً على النصوص أو الأرقام أو التواريخ.

### **التصفية التلقائية في Microsoft Excel**

لتفعيل ميزة التصفية التلقائية في Microsoft Excel:

1. انقر على صف العنوان في ورقة العمل.
1. من قائمة **البيانات**، حدد **تصفية** ثم **تصفية تلقائية**.

عند تطبيق التصفية التلقائية على ورقة عمل، يظهر التبديل (السهام السوداء) إلى يمين عناوين العمود.

1. انقر على سهم التصفية لرؤية قائمة الخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

| **الخيارات** | **الوصف** |
| :- | :- |
||All| عرض كافة العناصر في القائمة مرة واحدة.|
||Custom| تخصيص معايير التصفية مثل الاحتواء/عدم الاحتواء|
||Filter by Color| تصفية بناءً على اللون المملوء|
||Date Filters| تصفية الصفوف بناءً على معايير مختلفة على التاريخ|
||Number Filters| أنواع مختلفة من التصفية على الأرقام مثل المقارنة والمتوسطات وأعلى 10 وما إلى ذلك.|
||Text Filters| تصفية مختلفة مثل تبدأ بـ، تنتهي بـ، تحتوي على الخ،|
||Blanks/Non Blanks| يمكن تنفيذ هذه التصفيات من خلال تصفية النصوص الفارغة|

يقوم المستخدمون بتصفية بيانات ورقة العمل يدويًا في Microsoft Excel باستخدام هذه الخيارات.

### **تصفية أوتوماتيكية بواسطة Aspose.Cells**

تقدم Aspose.Cells فئة، `Workbook` التي تمثل ملف Excel. تحتوي فئة `Workbook` على مجموعة `Worksheets` التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تمثل صفحة العمل بواسطة فئة `Worksheet`. توفر فئة `Worksheet` مجموعة واسعة من الخصائص والطرق لإدارة صفحات العمل. لإنشاء مرشح تلقائي، استخدم خاصية `AutoFilter` من فئة `Worksheet`. الخاصية `AutoFilter` هي كائن من فئة `AutoFilter`، وتوفر الخاصية `Range` لتحديد نطاق الخلايا التي تشكل صف الرأس. يطبق المرشح التلقائي على نطاق الخلايا الذي يعتبر صف الرأس.

في كل ورقة عمل، يمكنك فقط تحديد نطاق تصفية واحد. هذا محدود بواسطة Microsoft Excel. لفلترة البيانات المخصصة، استخدم طريقة `AutoFilter.Custom`.

في المثال المعطى أدناه، قمنا بإنشاء نفس تصفية الأوتوماتيكية باستخدام Aspose.Cells كما قمنا بإنشائها باستخدام مايكروسوفت إكسل في القسم السابق.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range of the heading row
    worksheet.GetAutoFilter().SetRange(u"A1:B1");

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **أنواع مختلفة من التصفية**

توفر Aspose.Cells خيارات متعددة لتطبيق مرشحات مختلفة مثل مرشح الألوان، مرشح التاريخ، مرشح الأرقام، مرشح النص، مرشح الخانات الفارغة والخانات الغير فارغة.

##### **لون التعبئة**

تقدم Aspose.Cells وظيفة `AddFillColorFilter` لتصفية البيانات بناءً على خاصية لون التعبئة للخلايا. في المثال المقدم أدناه، تم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل ملفات العينة من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

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
    Workbook workbook(srcDir + u"ColouredCells.xlsx");

    // Instantiating a CellsColor object for foreground color
    CellsColor clrForeground = workbook.CreateCellsColor();
    clrForeground.SetColor(Color::Red());

    // Instantiating a CellsColor object for background color
    CellsColor clrBackground = workbook.CreateCellsColor();
    clrBackground.SetColor(Color::White());

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddFillColorFilter function to apply the filter
    worksheet.GetAutoFilter().AddFillColorFilter(0, BackgroundType::Solid, clrForeground, clrBackground);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredColouredCells.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من مرشحات التاريخ مثل تصفية جميع الصفوف التي تحتوي على تواريخ في يناير 2018. يوضح رمز العينة التالي هذا التصفية باستخدام وظيفة `AddDateFilter`. يتم تقديم ملفات العينة أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call AddDateFilter function to apply the filter
    worksheet.GetAutoFilter().AddDateFilter(0, DateTimeGroupingType::Month, 2018, 1, 0, 0, 0, 0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Date filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تاريخ ديناميكي**

أحيانًا تكون المرشحات الديناميكية مطلوبة استنادًا إلى التاريخ، مثل جميع الخلايا التي تحتوي على تواريخ في يناير بغض النظر عن السنة. في هذه الحالة، يتم استخدام وظيفة `DynamicFilter` كما هو موضح في رمز العينة التالي. يتم تقديم ملفات العينة أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

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
    U16String inputFilePath = srcDir + u"Date.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredDynamicDate.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call DynamicFilter function to apply the filter
    worksheet.GetAutoFilter().Dynamic_Filter(0, DynamicFilterType::January);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Dynamic filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **رقم**

يمكن تطبيق المرشحات المخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على رقم بين مدى معين. يوضح المثال التالي استخدام وظيفة `Custom()` لتصفية الأعداد. يتم تقديم ملفات العينة أدناه.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

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
    U16String inputFilePath = srcDir + u"Number.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"FilteredNumber.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Custom function to apply the filter
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::GreaterOrEqual, 5, true, FilterOperatorType::LessOrEqual, 10);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **نص**

إذا كانت عمود يحتوي على نص ويجب اختيار الخلايا التي تحتوي على نص معين، يمكن استخدام وظيفة `Filter()`. في المثال التالي، يحتوي قالب الملف على قائمة بالدول ويجب اختيار الصف الذي يحتوي على اسم دولة معين. يوضح الكود التالي تصفية النصوص. يتم تقديم ملفات العينة أدناه.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

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
    U16String inputFilePath = srcDir + u"Text.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"FilteredText.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call Filter function to apply the filter
    worksheet.GetAutoFilter().Filter(0, u"Angola");

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Filter applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **فراغات**

إذا كان عمود يحتوي على نص وبعض الخلايا فارغة، ويجب تحديد تلك الصفوف التي تحتوي على خلايا فارغة فقط، يمكن استخدام وظيفة `MatchBlanks()` كما هو موضح أدناه. يتم تقديم ملفات العينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف فارغ مصفى.xlsx](72417325.xlsx)

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
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outDir + u"FilteredBlank.xlsx");

    std::cout << "Filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **غير فارغة**

عندما يجب تصفية الخلايا التي تحتوي على أي نص، استخدم وظيفة التصفية `MatchNonBlanks` كما هو موضح أدناه. يتم تقديم ملفات العينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف تصفية غير فارغ.xlsx](72417326.xlsx)

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

    // Create workbook object and open the Excel file
    Workbook workbook(srcDir + u"Blank.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter
    worksheet.GetAutoFilter().MatchNonBlanks(0);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(outDir + u"FilteredNonBlank.xlsx");

    std::cout << "Non-blank filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تصفية مخصصة مع الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي. الملفات النموذجية معروضة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::Contains, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "AutoFilter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تصفية مخصصة مع عدم الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي لا تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows containing string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::NotContains, u"Be");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File filtered and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تصفية مخصصة تبدأ ب**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تبدأ بسلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows starting with string "Ba"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"Ba");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تصفية مخصصة تنتهي ب**

يوفر Excel تصفية مخصصة مثل تصفية الصفوف التي تنتهي بسلسلة معينة. يتوفر هذا الميزة في Aspose.Cells ويتم استعراضها أدناه من خلال تصفية الأسماء في ملف العينة المُعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

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
    U16String inputFilePath = srcDir + u"sourseSampleCountryNames.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"outSourseSampleCountryNames.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating AutoFilter by giving the cells range
    worksheet.GetAutoFilter().SetRange(u"A1:A18");

    // Initialize filter for rows end with string "ia"
    worksheet.GetAutoFilter().Custom(0, FilterOperatorType::BeginsWith, u"ia");

    // Refresh the filter to show/hide filtered rows
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة](/cells/ar/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.](/cells/ar/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="cpp" >}}
