---
title: ترتيب البيانات مع C++
linktitle: ترتيب البيانات
type: docs
weight: 130
url: /ar/cpp/sort-data-of-excel/
description: تعلم كيفية ترتيب البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: فرز البيانات بترتيب تصاعدي أو تنازلي، فرز البيانات بناءً على لون الخلفية
---

{{% alert color="primary" %}}

فرز البيانات هو واحد من الميزات المفيدة في Microsoft Excel. يتيح للمستخدمين ترتيب البيانات لجعلها أسهل في المسح. تتيح Aspose.Cells للمطورين ترتيب بيانات ورقة العمل ترتيب أبجدي أو رقمي والذي يعمل بنفس الطريقة التي يقوم بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **الترتيب**. سيتم عرض مربع الحوار للترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات مع Aspose.Cells**

يوفر Aspose.Cells الفئة [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/) المستخدمة لفرز البيانات بترتيب تصاعدي أو تنازلي. تحتوي الفئة على بعض الأعضاء المهمة، على سبيل المثال، خصائص مثل Key1 ... Key3 و Order1 ... Order3. يتم استخدام هذه الأعضاء لتعريف المفاتيح المرتبة وتحديد ترتيب ترتيب المفتاح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) البيانات التالية:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)، الخلايا للورقة العمل الأساسية.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه، يتم فرز البيانات بشكل مناسب.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

إذا كنت ترغب في فرز *من اليسار إلى اليمين*، استخدم السمة [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/).

{{% /alert %}}

### **فرز البيانات مع لون الخلفية**

يوفر Excel ميزات لفرز البيانات بناءً على لون الخلفية. نفس الميزة متوفرة باستخدام Aspose.Cells باستخدام DataSorter حيث يمكن استخدام [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor في [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) لفرز البيانات بناءً على لون الخلفية. يتم وضع جميع الخلايا التي تحتوي على اللون المحدد في [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/)، الوظيفة في الأعلى أو الأسفل وفقًا لإعداد SortOrder ولم يتم تغيير ترتيب بقية الخلايا على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/cpp/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/cpp/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="cpp" >}}
