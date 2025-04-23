---
title: عرض وإخفاء الصفوف والأعمدة وأشرطة التمرير باستخدام C++
linktitle: عرض وإخفاء الصفوف والأعمدة وأشرطة التمرير
type: docs
weight: 20
url: /ar/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: يوضح هذا المقال كيفية عرض وإخفاء صفوف وأعمدة أوراق عمل إكسل برمجيًا باستخدام لغة C++ وواجهة برمجة تطبيقات Aspose.Cells. يمكن تعديل رؤية أشرطة التمرير، وإخفاء عدة صفوف وأعمدة.
---

{{% alert color="primary" %}}

توفر Aspose.Cells طرقًا للتحكم في رؤية الصفوف والأعمدة وأشرطة التمرير في ورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف إكسل. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. بعض منها مذكور أدناه.

### **إظهار الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء الطريقتين [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) و [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. كلا الطريقتين تتطلب معلمات:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

عند جعل عمود مخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى العرض السابق المخصص أو عرضه بعرضه الأصلي، يرجى إلغاء إخفاء العمود بعرض سالب. على سبيل المثال: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء الطريقتين [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) و [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. كلا الطريقتين يتطلب معلمة فهرس الصف والعمود لإخفاء الصف أو العمود المحدد.

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

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **إخفاء صفوف وأعمدة متعددة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء الطريقتين [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) و [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. كلا الطريقتين يتطلبان فهرس الصف أو العمود الابتدائي وعدد الصفوف أو الأعمدة التي ينبغي إخفاؤها كمعلمات.

```c++
#include <iostream>
#include <memory>
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إظهار وإخفاء شريط التمرير**

يُستخدم شريط التمرير للتنقل في محتويات أي ملف. عادة ما تكون هناك نوعين من شرائط التمرير:

- شرائط التمرير العمودية
- شرائط التمرير الأفقية

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.

### **التحكم في رؤية شرائط التمرير**

توفر Aspose.Cells فئة، {0}، التي تمثل ملف إكسل. تقدم فئة {1} مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في رؤية أشرطة التمرير، استخدم خصائص {2} و {3} من فئة {4} و {5}. {6} و {7} هما خصائص منطقية، مما يعني أن هذه الخصائص يمكن أن تخزن قيم **صحيح** أو **خطأ**.

#### **جعل أشرطة التمرير مرئية**

اجعل أشرطة التمرير مرئية عن طريق تعيين خاصية [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) أو [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) للفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) إلى **صحيح**.

#### **إخفاء أشرطة التمرير**

إخف أشرطة التمرير عن طريق تعيين خاصية [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) أو [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) للفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) إلى **خطأ**.

**كود عينة**

إليك كود كامل يفتح ملف إكسل، `book1.xls`، ويخفي أشرطة التمرير، ثم يحفظ الملف المعدل باسم `output.xls`.

```c++
#include <iostream>
#include <fstream>
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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
