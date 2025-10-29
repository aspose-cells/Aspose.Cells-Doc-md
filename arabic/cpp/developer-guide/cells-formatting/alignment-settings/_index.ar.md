---
title: إعدادات المحاذاة باستخدام ++C
linktitle: إعدادات المحاذاة
description: في مكتبة Aspose.Cells، يمكنك استخدام إعدادات محاذاة الخلية لضبط التخطيط وعرض النص. من خلال ضبط الإعدادات مثل المحاذاة الأفقية، المحاذاة العمودية والتفاف النص، ستحصل على مزيد من التحكم في كيفية تدفق النص في الخلايا. ستوفر لك هذه الوثيقة خطوات مفصلة وشيفرة عينية لمساعدتك في فهم كيفية استخدام Aspose.Cells لإعدادات محاذاة الخلية بسرعة.
keywords: Aspose.Cells، إعدادات محاذاة الخلية، المحاذاة الأفقية، المحاذاة العمودية، التفاف النص
type: docs
weight: 20
url: /ar/cpp/cells-alignment-settings/
---

## **ضبط إعدادات المحاذاة**

### **إعدادات المحاذاة في Microsoft Excel**

أي شخص قد استخدم Microsoft Excel لتنسيق الخلايا سيكون متعودًا على إعدادات المحاذاة في Microsoft Excel.

كما يمكنك رؤية من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقية وعمودية)
- المسافة البادئة.
- التوجيه.
- التحكم بالنص.
- اتجاه النص.

كل إعدادات المحاذاة هذه مدعومة تمامًا بواسطة Aspose.Cells ويتم مناقشتها بمزيد من التفصيل أدناه.

### **إعدادات المحاذاة في Aspose.Cells**

توفر Aspose.Cells فئةً تُمثِّل ملف Excel تدعى [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثِّل ورقة عمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). يُمثِّل كل عنصر في مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

توفر Aspose.Cells الأساليب [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) و [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) لفئة [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) والتي تُستخدم للحصول على تنسيق الخلية وتعيينه. توفر الفئة [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) خصائص مفيدة لتكوين إعدادات المحاذاة.

حدد أي نوع لمحاذاة النص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/). أنواع محاذاة النص المحددة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) هي:

|** أنواع محاذاة النص **|** الوصف **|
| :- | :- |
|Bottom|يمثل محاذاة النص السفلي
|Center|يمثل محاذاة النص الوسطية
|CenterAcross|تمثل محاذاة النص في وسط النص|
|Distributed|تمثل توزيع محاذاة النص|
|Fill|تمثل ملء محاذاة النص|
|General|تمثل محاذاة النص العامة|
|Justify|تمثل محاذاة النص التبريري|
|Left|يمثل محاذاة النص اليسار|
|Right|يمثل محاذاة النص اليمين|
|Top|يمثل محاذاة النص العلوي|
|JustifiedLow|يُحاذي النص بطول كاشيدا معدل للنص العربي.|
|ThaiDistributed|يوزع النص التايلاندي خصوصًا، لأن كل حرف يُعامل ككلمة.|

{{% alert color="primary" %}}

يمكنك أيضا تطبيق ضبط التوزيع المبرر باستخدام الخاصية [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/).

{{% /alert %}}

#### **المحاذاة الأفقية**

استخدم خاصية [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) لمحاذاة النص أفقياً.

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

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **المحاذاة الرأسية**

مشابهة للمحاذاة الأفقية، استخدم خاصية [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) لمحاذاة النص عمودياً.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **المسافة البادئة**

من الممكن تعيين مستوى المسافة البادئة للنص في خلية بواسطة خاصية [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **الاتجاه**

حدد اتجاه (دوران) النص في خلية بواسطة خاصية [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

##### **تفاف النص**

يعمل تفاف النص في خلية على جعل النص أسهل قراءة: يتم ضبط ارتفاع الخلية ليتناسب مع جميع النص، بدلاً من قطعه أو تسربه إلى الخلايا المجاورة. ضبط التفاف النص على تشغيل أو إيقاف بواسطة خاصية [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/).

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **تقليص للتناسب**

خيار لتفاف النص في حقل هو تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك بضبط خاصية [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) في [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) إلى **true**.

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
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **دمج الخلايا**

مثل Microsoft Excel ، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. طريقة واحدة هي استدعاء [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) في مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) الوسيلة المعاملات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

الطريقة الأخرى هي أولاً استدعاء [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) لجمع الخلايا المدمجة. الطريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) في [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) تأخذ نفس مجموعة المعلمات كما في الطريقة [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) المناقشة أعلاه وتعيد [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). الكائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) يوفر أيضاً الطريقة [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) التي تدمج المجموعة المحددة في الكائن [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).

##### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يتم تعيين ترتيب القراءة باستخدام خاصية [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) 'الكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)'. توفر Aspose.Cells أنواع توجيه نص محددة مسبقًا في تعداد [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
