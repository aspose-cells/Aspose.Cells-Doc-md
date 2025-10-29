---
title: ثيمات وألوان إكسل باستخدام C++
linktitle: ثيمات وألوان إكسل
type: docs
weight: 100
url: /ar/cpp/excel-themes-and-colors/
description: كود C++ لاستخدام مخطط ألوان إكسل مع واجهة برمجة التطبيقات Aspose.Cells for C++
keywords: إنشاء وتطبيق مخططات الألوان باستخدام C++، إنشاء مخطط لون مخصص برمجيًا، كيفية تطبيق مخطط لون مخصص برمجيًا، كيفية استخدام مخطط الألوان في إكسل باستخدام C++
---

## **كيفية تطبيق وإنشاء مخطط الألوان في إكسل**
تجعل مواضيع المستند من السهل تنسيق ألوان وخطوط وتأثيرات تنسيق الرسومات للوثائق وتحديثها بسرعة. 
المواضيع توفر مظهرًا موحدًا مع الأنماط المسماة والتأثيرات البصرية والكائنات الأخرى المستخدمة في دفتر العمل. على سبيل المثال، الأنماط المميزة 1، على سبيل المثال، تظهر بشكل مختلف في موضوعات Office و Apex. في كثير من الأحيان، تطبق موضوع المستند ومن ثم تعدله إلى الشكل الذي تريده.

### **كيفية تطبيق مخطط لون في إكسل**
1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.
1. انقر على زر "الألوان" في قسم "الثيمات".
<br>
<img src="color.png" width=70% />
1. اختر لوحة ألوان تتناسب مع متطلباتك أو قم بتحويل المؤشر فوق نظام لرؤية معاينة مباشرة.

### **كيفية إنشاء مجموعة ألوان مخصصة في إكسيل**
يمكنك إنشاء مجموعة ألوان خاصة بك لإعطاء مستندك مظهرًا جديدًا وفريدًا أو لتلائم معايير علامة تجارية منظمتك.

1. افتح Excel وانتقل إلى علامة "تخطيط الصفحة" في شريط الأدوات.
1. انقر على زر "الألوان" في قسم "الثيمات".
1. انقر على زر "تخصيص الألوان...".
<br>
<img src="color2.png" width=70% />

1. في مربع الحوار "إنشاء ألوان ثيم جديدة"، يمكنك اختيار الألوان لكل عنصر عن طريق النقر على القوائم المنسدلة للألوان بجوارها. يمكنك اختيار الألوان من اللوحة أو تعريف ألوان مخصصة باستخدام خيار "مزيد من الألوان".
<br>
<img src="color3.png" width=70% />
1. بعد اختيار جميع الألوان المطلوبة، قم بتوفير اسم لمجموعة الألوان المخصصة في حقل "الاسم".

1. انقر على زر "حفظ" لحفظ مجموعة الألوان المخصصة الخاصة بك. ستكون مجموعة الألوان المخصصة الخاصة بك الآن متاحة في قائمة الألوان المنسدلة للاستخدام المستقبلي.

## **كيفية إنشاء وتطبيق مجموعة ألوان في Aspose.Cells**
توفر Aspose.Cells ميزات لتخصيص الثيمات والألوان.

### **كيفية إنشاء موضوع ألوان مخصص في Aspose.Cells**
إذا تم استخدام ألوان الثيمة في الملف، فليس من الضروري تعديل كل خلية بشكل فردي، بل نحتاج فقط إلى تعديل الألوان في الثيمة.

المثال التالي يوضح كيفية تطبيق ثيمات مخصصة باستخدام الألوان المرغوبة. نحن نستخدم ملف قالب عيني تم إنشاؤه يدويًا في Microsoft Excel 2007.

المثال التالي يحمل ملف XLSX قالبيًا، يحدد الألوان لأنواع مختلفة من الألوان الثيمية، بالإضافة إلى تطبيق الألوان المخصصة وحفظ ملف إكسيل.

```cpp
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

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية تطبيق ألوان الثيم في Aspose.Cells**

المثال التالي يطبق ألوان الخلفية والخط لخلية استنادًا إلى أنواع ألوان الثيمة الافتراضية (للجدول). يحفظ أيضًا ملف إكسيل على القرص.

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

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية الحصول على وتعيين ألوان الثيم في Aspose.Cells**
 فيما يلي بعض الطرق والخصائص التي تنفذ فيها ألوان الثيم.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): يستخدم لتعيين لون النص الأمامي.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): يستخدم لتعيين لون الخلفية.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): يستخدم لتعيين لون الخط.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): يستخدم للحصول على لون ثيم.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): يستخدم لتعيين لون ثيم.

المثال التالي يوضح كيفية الحصول على وتعيين ألوان الثيم.

المثال التالي يستخدم ملف XLSX قالب، يحصل على الألوان لأنواع مختلفة من الألوان الثيم، يقوم بتغيير الألوان ويحفظ ملف Microsoft Excel.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [استخراج بيانات الثيم من ملف Excel](/cells/ar/cpp/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="cpp" >}}
