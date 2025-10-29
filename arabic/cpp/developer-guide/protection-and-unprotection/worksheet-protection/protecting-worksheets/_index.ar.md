---
title: حماية أوراق العمل باستخدام C++
linktitle: حماية الأوراق العمل
type: docs
weight: 10
url: /ar/cpp/protecting-worksheets/
description: تعلم كيف تحمي أوراق العمل، الصفوف، الأعمدة، وخلايا معينة في ملفات Microsoft Excel باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

عند حماية ورقة العمل، تقتصر الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال، لا يمكن إدخال بيانات، أو إدراج أو حذف صفوف أو أعمدة، إلخ.

{{% /alert %}}

## **حماية الأوراق العمل**

### **مقدمة**

خيارات الحماية العامة في Microsoft Excel هي:

- المحتويات
- الكائنات
- السيناريوهات

لاتخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فإنها تختلف عن تشفير الملف. بشكل عام ، يعتبر حماية ورقة العمل مناسبة لأغراض العرض. فهي تمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **حماية ورقة العمل**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) الطريقة [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) التي تُستخدم لتطبيق الحماية على ورقة العمل. تقبل الطريقة [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) المعلمات التالية:

- نوع الحماية ، نوع الحماية المطبقة على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة تعداد [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/).
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور السابقة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بكلمة مرور بالفعل ، فقط قم بتمرير قيمة فارغة.

يحتوي تعداد [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) على أنواع حماية محددة مسبقًا التالية:

|**أنواع الحماية**|**الوصف**|
| :- | :- |
|All| لا يمكن للمستخدم تعديل أي شيء على هذه الورقة العمل|
|Contents| لا يمكن للمستخدم إدخال بيانات في هذه الورقة العمل|
|Objects| لا يمكن للمستخدم تعديل أجسام الرسم|
|Scenarios| لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|Structure| لا يمكن للمستخدم تعديل الهيكل|
|Windows| تم تطبيق الحماية على النوافذ|
|None| لا يوجد تطبيق للحماية|

المثال أدناه يوضح كيفية حماية ورقة عمل بكلمة مرور.

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

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

بعد استخدام الكود أعلاه لحماية الورقة العمل، يمكنك التحقق من الحماية على الورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى الورقة العمل، ستظهر لك نافذة التالي:

|**تحذير الذي يظهر عندما لا يستطيع المستخدم تعديل الورقة العمل**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

للعمل على الورقة العمل، قم بإلغاء حمايتها عن طريق تحديد **Protection**، ثم **Unprotect Sheet** من عنصر القائمة **Tools**.

بعد اختيار عنصر القائمة Unprotect Sheet، ستفتح نافذة تطالبك بإدخال كلمة المرور حتى تتمكن من العمل على الورقة العمل كما هو موضح أدناه:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **حماية خلايا قليلة في الورقة العمل باستخدام Microsoft Excel**

قد توجد حالات معينة حيث تحتاج إلى قفل بعض الخلايا فقط في الورقة العمل. إذا كنت ترغب في قفل بعض الخلايا المحددة في الورقة العمل، عليك أن تقوم بفتح كافة الخلايا الأخرى في الورقة العمل. جميع الخلايا في الورقة العمل تم تهيئتها بالفعل للقفل، يمكنك التحقق من ذلك عن طريق فتح أي ملف Excel في MS Excel والنقر على **Format | Cells...** لعرض صندوق الحوار **Format Cells** ثم النقر على علامة التبويب **Protection** ومن ثم رؤية مربع الاختيار المسمى "مقفل" يكون محددًا افتراضيًا.

تصف النقاط التالية كيفية قفل بعض الخلايا باستخدام MS Excel. ينطبق هذا الأسلوب على Microsoft Office Excel 97 و 2000 و 2002 و 2003 والإصدارات الأحدث.

1. حدد الورقة العمل بأكملها بالنقر على زر **Select All** (المستطيل الرمادي مباشرة فوق رقم الصف للصف 1 وعند اليسار من حرف العمود A).
1. انقر على **Cells** في القائمة **Format**، انقر على علامة التبويب **Protection**، ثم قم بإلغاء تحديد مربع الاختيار **Locked**.
   هذا يفتح جميع الخلايا على الورقة العمل
   إذا كانت الأمر **Cells** غير متاح، فقد يكون بعض أجزاء الورقة العمل مقفلة بالفعل. في القائمة **Tools**، قم بتوجيه المؤشر إلى **Protection**، ثم انقر على **Unprotect Sheet**.
1. حدد فقط الخلايا التي ترغب في قفلها وكرر الخطوة 2، ولكن هذه المرة حدد مربع الاختيار **Locked**.
١. في قائمة الـ**أدوات**, حدد **الحماية**, انقر فوق **حماية الورقة** ثم انقر فوق **موافق**.
١. في مربع حوار **حماية الورقة**, لديك الخيار لتحديد كلمة المرور واختيار العناصر التي ترغب في أن يتمكن المستخدمون من تغييرها.

### **حماية خلايا قليلة في ورقة العمل باستخدام Aspose Cells**

في هذه الطريقة، نستخدم واجهة برمجة التطبيقات Aspose.Cells فقط للقيام بالمهمة.

مثال: يوضح المثال التالي كيفية حماية عدد قليل من الخلايا في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل 3 خلايا (A1، B1، C1) فيها. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) إلى القيمة صحيح أو خاطئ وتطبيق طريقة *Column/Row.ApplyStyle()* لقفل أو فتح الصف/العمود بالسمات المطلوبة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **حماية صف في ورقة العمل**

تُتيح Aspose.Cells لك قفل أي صف بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) من فئة [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) لتطبيق [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) على صف معين في ورقة العمل. تأخذ هذه الطريقة معها مُعاملين: كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) وكائن [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) واللذان يحتويان على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية صف في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل الصف الأول فيها. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) إلى القيمة صحيح أو خاطئ لقفل أو فتح الصف/العمود باستخدام كائن [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **حماية عمود في ورقة العمل**

تُتيح Aspose.Cells لك بسهولة قفل أي عمود في ورقة العمل. هنا، يمكننا استخدام طريقة [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) من فئة [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) لتطبيق [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) على عمود معين في ورقة العمل. تأخذ هذه الطريقة معها مُعاملين: كائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) وكائن [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) واللذان يحتويان على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية عمود في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل العمود الأول فيه. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) إلى القيمة صحيح أو خاطئ لقفل أو فتح الصف/العمود باستخدام كائن [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **السماح للمستخدمين بتعديل المدى**

يُظهر المثال التالي كيفية السماح للمستخدمين بتعديل مدى محدد في ورقة العمل الخاصة.

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
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
