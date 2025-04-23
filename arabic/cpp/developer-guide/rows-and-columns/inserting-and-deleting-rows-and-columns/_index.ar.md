---
title: إدراج وحذف الصفوف والأعمدة في ملف Excel باستخدام C++
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/cpp/inserting-and-deleting-rows-and-columns/
description: توضح هذه المقالة كيفية إدراج وحذف الصفوف والأعمدة باستخدام API Aspose.Cells for C++.
keywords: تدير Aspose.Cells C++ الصفوف والأعمدة، إدراج الصفوف والأعمدة، حذف الصفوف والأعمدة
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.
لتلبية هذه المتطلبات، توفر Aspose.Cells مجموعة بسيطة جدًا من الفئات والطرق، التي سيتم مناقشتها أدناه.

### **إدارة الصفوف والأعمدة**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف Excel من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. من بين هذه الطرق ما يلي.

{{% alert color="primary" %}}

عند إضافة الصفوف أو الأعمدة، يتم إزاحة المحتوى في ورقة العمل إلى الأسفل أو إلى اليمين، وعند إزالة الصفوف أو الأعمدة، يتم إزاحة المحتوى للأعلى أو إلى اليسار.

{{% /alert %}}

## **إدراج الصفوف والأعمدة**

### **كيفية إدراج صف**

إدراج صف في ورقة العمل في أي مكان عن طريق استدعاء طريقة [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) من مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ طريقة [**InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) مؤشر الصف الذي سيتم إدراج الصف الجديد فيه.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiating a Workbook object
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRow(2);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية إدراج عدة صفوف**

لإضافة صفوف متعددة إلى ورقة العمل، استدعي طريقة [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) من مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ الطريقة [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) معلمتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

```c++
#include <iostream>
#include <fstream>
#include <memory>
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

    // Insert 10 rows into the worksheet starting from 3rd row
    worksheet.GetCells().InsertRows(2, 10);

    // Path of output excel file
    U16String outputFilePath = srcDir + u"output.out.xls";

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **كيفية إدراج صف مع تنسيق**

لإدراج صف بالتنسيق، استخدم التحميل الزائد [**InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) الذي يأخذ [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) كمعلمة. اضبط الخاصية [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) من فئة [**InsertOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/) باستخدام تعداد [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/). يحتوي التعداد [**CopyFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/insertoptions/getcopyformattype/) على ثلاثة أعضاء كما هو مدرج أدناه.

- SameAsAbove: يقوم بتنسيق الصف مثل الصف الذي يسبقه.
- SameAsBelow: يقوم بتنسيق الصف مثل الصف الذي يليه.
- Clear: يُمسح التنسيق.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"InsertingARowWithFormatting_out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting Formatting options
    InsertOptions insertOptions;
    insertOptions.SetCopyFormatType(CopyFormatType::SameAsAbove);

    // Inserting a row into the worksheet at 3rd position
    worksheet.GetCells().InsertRows(2, 1, insertOptions);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Row inserted successfully with formatting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية إدراج عمود**

كما يمكن للمطورين إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) من مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ الطريقة [**InsertColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) مؤشر العمود الذي سيتم إدراج العمود الجديد فيه.

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
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a column into the worksheet at 2nd position
    worksheet.GetCells().InsertColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Column inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **حذف الصفوف والأعمدة**

### **كيفية حذف عدة صفوف**

لحذف صفوف متعددة من ورقة العمل، استدعِ طريقة [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) من مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ الطريقة [**DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) معلمتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete 10 rows from the worksheet starting from 3rd row
    worksheet.GetCells().DeleteRows(2, 10);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Rows deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **كيفية حذف عمود**

لحذف عمود من ورقة العمل في أي مكان، استدعِ طريقة [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) من مجموعة [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). تأخذ الطريقة [**DeleteColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) مؤشر العمود الذي سيتم حذفه.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Delete a column from the worksheet at 5th position (index 4)
    worksheet.GetCells().DeleteColumn(4);

    // Save the modified Excel file
    U16String outputFilePath = srcDir + u"output.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Column deleted successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
