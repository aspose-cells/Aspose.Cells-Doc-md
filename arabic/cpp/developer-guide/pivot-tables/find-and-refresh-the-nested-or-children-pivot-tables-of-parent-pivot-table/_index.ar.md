---
title: العثور وتحديث الجداول المحورية المتداخلة أو الأطفال لجدول محوري والدة باستخدام C++
linktitle: العثور وتحديث الجداول المحورية المتداخلة أو الأطفال
type: docs
weight: 60
url: /ar/cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: تعلم كيفية العثور على وتحديث الجداول المحورية المتداخلة أو الأطفال باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يستخدم جدول دوران واحد جدول دوران آخر كمصدر بيانات، لذا يطلق عليه جدول دوران فرعي أو مدمج. يمكنك العثور على جداول الدوران الفرعية لجدول دوران أم باستخدام الطريقة [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/).

## **العثور وتحديث جداول الدوران المدمجة أو الفرعية لجدول الدوران الأم**

يحمل رمز العينة التالي [ملف إكسل المثالي](61767747.xlsx) الذي يحتوي على ثلاثة جداول دوران. الجداول الدوران السفلية هي أطفال الجدول الدوران العلوي كما هو موضح في هذه اللقطة من الشاشة. يعثر الكود على جدول الدوران الفرعي باستخدام الطريقة [**PivotTable::GetChildren()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getchildren/) ومن ثم يقوم بتحديثها واحدًا تلو الآخر.

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleFindAndRefreshNestedOrChildrenPivotTables.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access third pivot table
    PivotTable ptParent = ws.GetPivotTables().Get(2);

    // Access the children of the parent pivot table
    Vector<PivotTable> ptChildren = ptParent.GetChildren();

    // Refresh all the children pivot table
    int count = ptChildren.GetLength();
    for (int idx = 0; idx < count; idx++)
    {
        // Access the child pivot table
        PivotTable ptChild = ptChildren[idx];

        // Refresh the child pivot table
        ptChild.RefreshData();
        ptChild.CalculateData();
    }

    std::cout << "Children pivot tables refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
