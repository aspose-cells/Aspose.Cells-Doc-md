---
title: تحديد تحذير الفرز أثناء فرز البيانات باستخدام C++
linktitle: تحديد تحذير الفرز أثناء فرز البيانات
type: docs
weight: 140
url: /ar/cpp/specifying-sort-warning-while-sorting-data/
description: تعلم كيفية تحديد تحذير الفرز أثناء فرز البيانات بواسطة استخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: إضافة تحذير الفرز عند فرز البيانات، تعيين تحذير الفرز أثناء فرز البيانات، حدد تحذير الفرز عند فرز البيانات.
---

## **سيناريوهات الاستخدام المحتملة**

الرجاء النظر في هذه البيانات النصية أي {11، 111، 22}. تم فرز هذه البيانات النصية لأن 111 يأتي قبل 22 من حيث النص. ولكن إذا كنت تريد فرز هذه البيانات ليس كنص ولكن كأرقام، فإنه سيصبح {11، 22، 111} لأن 111 يأتي بعد 22 من الناحية الرقمية. توفر Aspose.Cells الخاصية {0} للتعامل مع هذه المسألة. يرجى ضبط هذه الخاصية كـ **true** وستتم فرز بياناتك النصية كبيانات رقمية. توضح اللقطة الناتجة التحذير الموضح من قبل Microsoft Excel عند فرز البيانات النصية التي تبدو مثل بيانات رقمية.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **الكود المثالي**

الكود المصدري العينة التالي يوضح استخدام الخاصية [**DataSorter.GetSortAsNumber()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortasnumber/) كما هو موضح سابقا. يرجى الاطلاع على [ملف Excel عينة](43352075.xlsx) و [ملف الإخراج Excel](43352076.xlsx) لمزيد من المساعدة.

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
    Workbook workbook(srcDir + u"sampleSortAsNumber.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create cell area
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A20");

    // Create data sorter
    DataSorter sorter = workbook.GetDataSorter();

    // Find the index of column A
    int idx = CellsHelper::ColumnNameToIndex(u"A");

    // Add key in sorter for sorting in ascending order
    sorter.AddKey(idx, SortOrder::Ascending);
    sorter.SetSortAsNumber(true);

    // Perform sort
    sorter.Sort(worksheet.GetCells(), ca);

    // Save the output workbook
    workbook.Save(outDir + u"outputSortAsNumber.xlsx");

    std::cout << "Sorting completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
