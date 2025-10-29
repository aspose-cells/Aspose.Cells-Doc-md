---
title: إنشاء، الوصول، ونسخ النطاقات المسماة باستخدام C++
linktitle: إنشاء، الوصول، ونسخ النطاقات المسماة
type: docs
weight: 200
url: /ar/cpp/create-access-and-copy-named-ranges/
description: تعلم كيفية إنشاء، والوصول، ونسخ النطاقات المسماة في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **مقدمة**

 عادةً، تُستخدم علامات الأعمدة والصفوف للإشارة إلى خلايا فردية. من الممكن إنشاء أسماء وصفية لتمثيل خلايا، أو نطاقات خلايا، أو صيغ، أو قيم ثابتة. قد يشير كلمة **اسم** إلى سلسلة من الأحرف تمثل خلية أو نطاق خلايا أو صيغة أو قيمة ثابتة. تعيين اسم لنطاق يعني أنه يمكن الإشارة إلى ذلك النطاق بواسطة اسمه. استخدم أسماء بسيطة، مثل المنتجات، للإشارة إلى النطاقات الصعبة الفهم، مثل مبيعات!C20:C30. يمكن استخدام التسميات في الصيغ التي تشير إلى البيانات على نفس ورقة العمل؛ إذا كنت تريد تمثيل نطاق على ورقة عمل أخرى، يمكنك استخدام اسم. *النطاقات المسماة من بين الميزات الأقوى في Microsoft Excel، خاصة عند استخدامها كمصدر لنطاقات القوائم، PivotTables، الرسوم البيانية، وما إلى ذلك.

## **العمل مع النطاق المسمى باستخدام Microsoft Excel**

### **إنشاء نطاقات مسماة**

الخطوات التالية تصف كيفية تسمية خلية أو نطاق خلايا باستخدام **MS Excel**. ينطبق هذا الأسلوب على **Microsoft Office Excel 2003**، **Microsoft Excel 97**، 2000، و 2002.

1. حدد الخلية أو النطاق الذي ترغب في تسميته.
2. انقر على **مربع الاسم** في الطرف الأيسر من شريط الصيغة.
1. اكتب اسم الخلايا.
1. اضغط على ENTER.

{{% alert color="primary" %}}

لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.

{{% /alert %}}

## **العمل مع نطاق مسمى باستخدام Aspose.Cells**

هنا، نستخدم واجهة برمجة التطبيقات Aspose.Cells للقيام بالمهمة.
تقدم Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **إنشاء نطاق مسمى**

من الممكن إنشاء نطاق مسمى من خلال استدعاء طريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) مفرطة التحميل من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). تأخذ نسخة النموذج من الطريقة [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) المعلمات التالية:

- اسم الخلية العلوية اليسرى، اسم الخلية العلوية اليسرى في النطاق.
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.

عند استدعاء [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)، فإنه يُرجع نطاق المصنوع حديثًا كنموذج من فئة [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). استخدم هذا [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) لتكوين النطاق المسمى. على سبيل المثال، قم بتعيين اسم النطاق باستخدام خاصية [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). يوضح المثال التالي كيفية إنشاء نطاق مسمّى للخلايا التي تمتد عبر B4:G14.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **إدخال البيانات في الخلايا في النطاق المسمى**

يمكنك إدراج البيانات في الخلايا الفردية في المجموعة وفق النمط التالي:

- **سي + +**: النطاق (صف، عمود)

افترض أن لديك نطاق مسمى من الخلايا يمتد من A1 إلى C4. يصنع المصفوفة 4 * 3 = 12 خلية. يتم ترتيب الخلايا الفردية بشكل تسلسلي: نطاق(0، 0)، نطاق(0، 1)، نطاق(0، 2)، نطاق(1، 0)، نطاق(1، 1)، نطاق(1، 2)، نطاق(2، 0)، نطاق(2، 1)، نطاق(2، 2)، نطاق(3، 0)، نطاق(3، 1)، نطاق(3، 2).

استخدم الخصائص التالية لتحديد الخلايا في المدى:

- FirstRow يعيد فهرس الصف الأول في المدى المسمى.
- FirstColumn يعيد فهرس العمود الأول في المدى المسمى.
- RowCount يعيد العدد الكلي للصفوف في المدى المسمى.
- ColumnCount يعيد العدد الكلي للأعمدة في المدى المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **تحديد الخلايا في النطاق المسمى**

يمكنك إدراج البيانات في الخلايا الفردية في المجموعة وفق النمط التالي:

- **سي + +**: النطاق (صف، عمود)

إذا كان لديك نطاق مسمى يمتد من A1 إلى C4. تشكل المصفوفة 4 * 3 = 12 خلية. يتم ترتيب خلايا النطاق الفردي بشكل متتابع: النطاق(0، 0)، النطاق(0، 1)، النطاق(0، 2)، النطاق(1، 0)، النطاق(1، 1)، النطاق(1، 2)، النطاق(2، 0)، النطاق(2، 1)، النطاق(2، 2)، النطاق(3، 0)، النطاق(3، 1)، النطاق(3، 2).

استخدم الخصائص التالية لتحديد الخلايا في المدى:

- FirstRow يعيد فهرس الصف الأول في المدى المسمى.
- FirstColumn يعيد فهرس العمود الأول في المدى المسمى.
- RowCount يعيد العدد الكلي للصفوف في المدى المسمى.
- ColumnCount يعيد العدد الكلي للأعمدة في المدى المسمى.

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **الوصول إلى المدى المسمى**

#### **الوصول إلى نطاق مسمى محدد**

استدعاء [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) الكائن [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) الميثود للحصول على مدى بالاسم المحدد. تأخذ الميثود النموذجية [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) الاسم للمدى المسمى وتعيد المدى المحدد كمثيل لفئة [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). يوضح المثال التالي كيفية الوصول إلى مدى محدد بالاسم.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **الوصول إلى كافة المدى المسمى في ورقة العمل**

استدعِ طريقة [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) من مجموعة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) للحصول على جميع النطاقات المعرفة في ورقة العمل. تقوم الطريقة [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) بإرجاع مصفوفة تحتوي على جميع النطاقات المعرفة في مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **نسخ المدى المسمى**

توفر Aspose.Cells طريقة [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) لنسخ نطاق من الخلايا مع التنسيق إلى نطاق آخر.

المثال التالي يوضح كيفية نسخ مدى مصدر من الخلايا إلى مدى مسمى آخر.

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

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
