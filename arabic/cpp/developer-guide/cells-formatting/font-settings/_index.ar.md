---
title: إعدادات الخط باستخدام C++
linktitle: إعدادات الخط
type: docs
weight: 30
url: /ar/cpp/cells-font-settings/
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جدول البيانات. تدعم تعيين إعدادات الخط للخلايا، مما يتيح للمستخدمين تخصيص نمط وخصائص الخطوط. ستوضح هذه المقالة كيف تستخدم مكتبة Aspose.Cells لضبط إعدادات الخطوط في الخلايا.
keywords: Aspose.Cells، Cells، Font Settings، Styles، Properties
---

{{% alert color="primary" %}}

يمكن التحكم في مظهر النص وشكله عن طريق تغيير إعدادات الخط. قد تشمل إعدادات الخط الاسم، النمط، الحجم، اللون، وتأثيرات أخرى للخطوط. تمامًا كبرنامج Microsoft Excel، يدعم Aspose.Cells أيضًا تكوين إعدادات الخطوط للخلايا.

{{% /alert %}}

## **تكوين إعدادات الخط**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورق عمل في ملف Excel. يمثل ورق العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). كل عنصر في مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) وطرق [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) و [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) تُستخدم للحصول على وتعيين نمط تنسيق الخلية. توفر الفئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص لتكوين إعدادات الخط.

### **تعيين اسم الخط**

يمكن للمطورين تطبيق أي خط على النص داخل خلية باستخدام خاصية [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

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

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تعيين نمط الخط إلى عريض**

يمكن للمطورين جعل النص عريضًا عن طريق ضبط خاصية [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) من كائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) على **صحيح**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **تعيين حجم الخط**

قم بتعيين حجم الخط باستخدام خاصية [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

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

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **تعيين لون الخط**

استخدم خاصية [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) لضبط لون الخط. اختر أي لون من التعداد اللوني (جزء من إطار عمل C++) وقم بتعيينه للخاصية [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

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

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **تعيين نوع تسطير الخط**

استخدم خاصية [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) لتسطير النص. تقدم Aspose.Cells مجموعة من أنواع تسطير الخط المحددة مسبقًا في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)

|**أنواع تسطير الخط**|**الوصف**|
| :- | :- |
|Accounting|تسطير واحد للحساب|
|Double|تسطير مزدوج|
|DoubleAccounting|تسطير حسابي مزدوج|
|None|بدون تسطير|
|Single|تسطير واحد|

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

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ضبط تأثير شطب**

تطبيق تأثير الشطب عن طريق ضبط خاصية [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) إلى **true**.

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

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ضبط تأثير الرمز الفرعي**

تطبيق الرمز الفرعي عن طريق ضبط خاصية [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) إلى **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **ضبط تأثير الرمز العلوي على الخط**

يمكن للمطورين تطبيق تأثير الرمز العلوي على الخط عن طريق ضبط خاصية [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) لكائن [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) إلى **true**.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
