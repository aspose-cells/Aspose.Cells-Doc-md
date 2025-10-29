---
title: 用C++指定数据透视项的绝对位置
linktitle: 指定数据透视项的绝对位置
type: docs
weight: 50
url: /zh/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: 学习如何使用Aspose.Cells在C++中指定数据透视项的绝对位置。
---

{{% alert color="primary" %}}

有时，用户需要指定数据透视项的绝对位置。Aspose.Cells API引入了几项新属性和一个方法来实现此需求。

- 添加了[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)属性，可用于指定所有数据透视项的位置索引，而不论父节点如何。添加了[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)属性，可用于指定在同一父节点下的数据透视项的位置索引。
- 增加了 [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) 方法，用于根据计数值上移或下移项目，其中计数代表移动的位置数。如果计数值小于零，则项目上移；如果大于零，则下移。布尔类型的 `isSameParent` 参数表示是否在同一父节点中进行移动操作。
- 淘汰了 `PivotItem.Move(int count)` 方法；建议使用新添加的 [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) 方法。

{{% /alert %}}

以下示例代码创建了一个数据透视表，并在同一父节点内指定了数据透视项的位置。您可以下载[源Excel](5112632.xlsx)和[输出Excel](5112619.xlsx)文件以供参考。打开输出Excel文件后，您会看到数据透视项“4H12”位于父节点“K11”的第0位，“DIF400”位于第3位，类似的，CA32在第1位，AAA3在第2位。

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

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

请注意，在使用 [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)、[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) 属性和 [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) 方法之前，必须调用 `PivotTable.RefreshData` 和 `PivotTable.CalculateData` 方法。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
