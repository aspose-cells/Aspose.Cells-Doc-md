---
title: فرز البيانات في العمود باستخدام قائمة فرز مخصصة باستخدام C++
linktitle: فرز البيانات في العمود بقائمة فرز مخصصة
type: docs
weight: 290
url: /ar/cpp/sort-data-in-column-with-custom-sort-list/
description: تعلم كيفية فرز البيانات في العمود باستخدام قائمة مخصصة بواسطة استخدام واجهة برمجة التطبيقات Aspose.Cells for C++.
keywords: فرز البيانات في العمود باستخدام قائمة الفرز المخصصة، فرز البيانات حسب القائمة المخصصة.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك فرز البيانات في العمود باستخدام قائمة مخصصة. يمكن القيام بذلك باستخدام [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). ومع ذلك، فإن هذه الطريقة تعمل فقط إذا لم يكن لدى العناصر في القائمة المخصصة فواصل داخلها. إذا كانت تحتوي على فواصل مثل "USA,US"، "China,CN" وغيرها، فلابد من استخدام [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). هنا، المعامل الأخير ليس سلسلة نصية بل هو مصفوفة من السلاسل النصية.

## **فرز البيانات في العمود بقائمة فرز مخصصة**

يوضح رمز العينة التالي كيفية استخدام طريقة [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) لفرز البيانات باستخدام القائمة الفرزية المخصصة. يرجى الاطلاع على [ملف إكسل العينة](50528327.xlsx) المستخدم في هذا الرمز و[ملف إكسل الناتج](50528328.xlsx) الناتج عنه. يظهر لقطة الشاشة التالية تأثير الكود على ملف إكسل العينة عند التنفيذ.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **الكود المثالي**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
