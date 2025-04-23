---
title: تجميع وفك تجميع الصفوف والأعمدة باستخدام C++
linktitle: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 50
url: /ar/cpp/grouping-and-ungrouping-rows-and-columns/
description: تعلم كيفية تجميع وفك تجميع الصفوف والأعمدة في ملفات Excel باستخدام Aspose.Cells مع C++.
---

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

|**تجميع الصفوف والأعمدة.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة تجميع الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل، تم مناقشة بعض هذه الطرق أدناه بالمزيد من التفاصيل.

### **تجميع الصفوف والأعمدة**

يمكن تجميع الصفوف أو الأعمدة عن طريق استدعاء [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) و [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Group first six rows (from 0 to 5) and make them hidden
    worksheet.GetCells().GroupRows(0, 5, true);

    // Group first three columns (from 0 to 2) and make them hidden
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns grouped successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

يمكن للمطورين تكوين إعدادات التجميع باستخدام خاصية [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) لفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

### **صفوف ملخصية أسفل التفاصيل**

من الممكن التحكم في ما إذا كانت الصفوف الملخصية تُعرض أسفل التفاصيل عن طريق تعيين خاصية [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) لفئة [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) إلى **صحيح** أو **خطأ**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Setting SummaryRowBelow property to false
    worksheet.GetOutline().SetSummaryRowBelow(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **أعمدة ملخصية على يمين التفاصيل**

يمكن للمطورين أيضًا التحكم في عرض الأعمدة الملخصية على يمين التفاصيل عن طريق تعيين خاصية [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) لفئة [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) إلى **صحيح** أو **خطأ**.

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
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Grouping first six rows and first three columns
    worksheet.GetCells().GroupRows(0, 5, true);
    worksheet.GetCells().GroupColumns(0, 2, true);

    // Set summary column to the right
    worksheet.GetOutline().SetSummaryColumnRight(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إلغاء تجميع الصفوف والأعمدة**

لإلغاء تجميع أي صفوف أو أعمدة مجمعة، يُمكن استدعاء [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) و [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). تأخذ كلا الطريقتين معلمتين:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) لديه تحميل زائد يأخذ معامل بولياني ثالث. يتم تعيينه على **صحيح** يزيل جميع المعلومات المجمّعة. وإلا، يتم إزالة معلومات المجموعة الخارجية فقط.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Ungrouping first six rows (from 0 to 5)
    worksheet.GetCells().UngroupRows(0, 5);

    // Ungrouping first three columns (from 0 to 2)
    worksheet.GetCells().UngroupColumns(0, 2);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```
