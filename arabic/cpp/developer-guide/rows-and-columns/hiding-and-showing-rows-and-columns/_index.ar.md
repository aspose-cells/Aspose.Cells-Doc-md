---
title: إخفاء وإظهار الصفوف والأعمدة باستخدام C++
linktitle: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 60
url: /ar/cpp/hiding-and-showing-rows-and-columns/
description: تعلم كيفية إخفاء وعرض الصفوف والأعمدة في ملفات Excel برمجياً باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

أحيانًا، يبدو من المنطقي إخفاء صفوف أو أعمدة معينة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة، وكذلك Aspose.Cells.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) يسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. يتم مناقشة بعض هذه الأساليب أدناه.

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) و[**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. تأخذ كلا الطريقين فهم فهرس الصف والعمود كمعلمة لإخفاء الصف أو العمود المحدد.

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

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully. File saved to: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **عرض الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء طرق [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) و[**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. تأخذ كلا الطريقين معلمتين:

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhide the 3rd row and set its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhide the 2nd column and set its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File modified and saved successfully!" << std::endl;

    return 0;
}
```

{{% alert color="primary" %}}

عند جعل عمود مخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى عرضه السابق أو لعرضه الأصلي، يرجى إلغاء إظهار العمود بعرض سلبي. على سبيل المثال: `worksheet.Cells.UnhideColumn(5, -1)`

{{% /alert %}}

### **إخفاء عدة صفوف وأعمدة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء طرق [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) و[**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) من مجموعة [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) على التوالي. تأخذ كلا الطريقين فهرس الصف أو العمود البدء وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet (zero-based index)
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet (zero-based index)
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) و[**UnhideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderows/) فئة [**UnhideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumns/) لجعل عدة صفوف وأعمدة مرئية.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
