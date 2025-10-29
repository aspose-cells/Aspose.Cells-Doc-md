---
title: 透视筛选器（C++）
linktitle: 透视筛选器
type: docs
weight: 130
url: /zh/cpp/add-or-clear-pivot-filter/
description: 学习如何使用 C++ 和 Aspose.Cells 在透视表中添加筛选器。
keywords: 在没有Office 2013、Office 2016、Office 2019和Office 365的情况下在数据透视表中添加筛选器。
---

## **可能的使用场景**
当你使用已知数据创建数据透视表并希望筛选时，你需要学习并使用筛选功能。它可以帮助你有效筛选出所需的数据。通过使用Aspose.Cells API，你可以在数据透视表中添加和清除字段值上的筛选。 

## **在Excel中为数据透视表添加筛选**
在Excel中为数据透视表添加筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 点击你想要添加筛选的下拉箭头。
3. 从下拉菜单中选择“前十名”。
<br>
<img src="3.png" width=80% />
4. 设置显示模式和筛选数量。
<br>
<img src="4.png" width=80% />

## **在数据透视表中添加筛选**
请参阅以下示例代码。它设置数据并基于它创建数据透视表。然后在数据透视表的行字段上添加筛选器。最后，以[filterout.xlsx]格式保存工作簿。执行示例代码后，工作表中将添加一个带有Top10筛选器的数据透视表。

### **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **在Excel中清除数据透视表的筛选**
在 Excel 中清除数据透视表中的筛选，按照以下步骤操作：

1. 选择要清除筛选的数据透视表。 
2. 单击数据透视表中要清除筛选的下拉箭头。
3. 从下拉菜单中选择“清除筛选”。
<br>
<img src="1.png" width=80% />
4. 如果您要清除数据透视表中的所有筛选，还可以在 Excel 的“数据透视表分析”选项卡上单击“清除筛选”按钮。
<br>
<img src="2.png" width=80% />

## **清除数据透视表的筛选**
使用 Aspose.Cells 在数据透视表中清除筛选。请参阅以下示例代码。 
1. 设置数据并创建基于该数据的数据透视表。 
2. 在数据透视表的行字段上添加筛选。 
3. 以 [output XLSX](out_add.xlsx) 格式保存工作簿。执行示例代码后，将在工作表中添加带有 top10 筛选的数据透视表。 
4. 清除特定数据透视字段上的筛选。执行清除筛选的代码后，将清除特定数据透视字段上的筛选。请检查 [output XLSX](out_delete.xlsx)。

### **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
