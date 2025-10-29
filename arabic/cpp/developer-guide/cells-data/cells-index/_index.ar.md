---
title: الحصول على فهرس الخلايا باستخدام C++
linktitle: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/cpp/get-cells-index/
description: تعلم كيفية الحصول على فهرس الصف أو العمود بواسطة اسم الصف أو العمود أو الخلايا. قم بتحويل اسم الخلية إلى فهرس صف وعمود بصفر بادئ باستخدام Aspose.Cells مع C++.
keywords: الحصول على فهرس الصف والعمود بواسطة اسم الخلية، الحصول على فهرس العمود بواسطة اسم العمود، الحصول على فهرس الصف بواسطة اسم الصف، الحصول على الفهرس بواسطة اسم الخلية.
---

{{% alert color="primary" %}}
العرض الافتراضي لExcel هو مرجع نمط A1، حيث يُعرف كل عمود بالحرف A و B و C ....، وتُسمى الخلايا A1 و B2 و C3 ... وهلم جرا.
قد ترغب في معرفة أي صف وعمود تحتوي عليه هذه الخلية.

{{% /alert %}}

## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج فقط إلى التلاعب ببيانات معينة على ورقة العمل بواسطة فهرس الصف والعمود، تحتاج إلى معرفة فهارس الصف والعمود لتلك الخلية المحددة. 
تقدم Aspose.Cells هذه الميزة للحصول على فهرس الصف والعمود بواسطة اسم الصف والعمود والخلية. 
توفر Aspose.Cells الخصائص والأساليب التالية لمساعدتك على تحقيق أهدافك:
- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/rownametoindex/)

ملاحظة: الفهرسة تبدأ من الصفر في Aspose.Cells for C++، ولكن معرف الصف يبدأ من واحد في MS Excel.

## **الحصول على فهارس الخلايا باستخدام Aspose.Cells**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Cell curr = cells.Find(u"Blackberry", nullptr);
    int currRow, currCol;

    // Get row and column index of current cell
    CellsHelper::CellNameToIndex(curr.GetName(), currRow, currCol);
    std::cout << "Row Index: " << currRow << "  Column Index: " << currCol << std::endl;

    // Get column name by column index
    U16String columnName = CellsHelper::ColumnIndexToName(currCol);

    // Get row name by row index
    U16String rowName = CellsHelper::RowIndexToName(currRow);

    std::cout << "Column Name: " << columnName.ToUtf8() << " Row Name: " << rowName.ToUtf8() << std::endl;

    // Get column index by column name
    int columnIndex = CellsHelper::ColumnNameToIndex(columnName);

    // Get row index by row name
    int rowIndex = CellsHelper::RowNameToIndex(rowName);

    std::cout << "Column Index: " << columnIndex << " Row Index: " << rowIndex << std::endl;

    // Assertions
    if (columnIndex != currCol || rowIndex != currRow) {
        std::cerr << "Assertion failed!" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
