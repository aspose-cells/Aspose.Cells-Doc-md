---
title: 在PivotTable中添加计算字段（C++）
linktitle: 在数据透视表中添加计算字段
type: docs
weight: 130
url: /zh/cpp/add-calculated-field-in-pivot-table/
description: 如何在透视表中添加计算字段 Aspose.Cells for C++。
keywords: 在数据透视表中添加计算字段。
---

## **可能的使用场景**
当您基于已知数据创建数据透视表时，您会发现其中的数据不是您想要的。您想要的数据是这些原始数据的组合。例如，您需要在希望获取数据之前对原始数据进行加法、减法、乘法和除法。这时，您需要构建一个计算字段并设置相应的计算公式。然后对计算字段执行一些统计和其他操作。 

## **在Excel的数据透视表中添加计算字段**
在Excel中的数据透视表中插入计算字段，请按照以下步骤进行：

1. 选择要向其添加计算字段的数据透视表。 
2. 转到功能区中的数据透视表分析选项卡。
3. 单击“字段、项和集” ，然后从下拉菜单中选择“计算字段”。
4. 在“名称”字段中输入计算字段的名称。
5. 在"公式"字段中，输入要使用适当的数据透视表字段名称和数学运算符进行计算的公式。 
<br>
<img src="1.png" width=80% />
6. 单击"确定"创建计算字段。
7. 新的计算字段将出现在数据透视表字段列表中的值部分。
8. 将计算字段拖动到数据透视表的值部分中，以显示计算值。
<br>
<img src="2.png" width=80% />

## **使用 C++ 添加透视表中的计算字段**
使用Aspose.Cells向Excel文件中添加计算字段。请查看以下示例代码。执行示例代码后，数据透视表将添加一个带有计算字段的工作表。
1. 设置原始数据并创建数据透视表。 
2. 根据数据透视表中现有的PivotField创建计算字段。
3. 将计算字段添加到数据区。 
4. 最后，以[out.xlsx]格式保存工作簿。 

## **示例代码**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
