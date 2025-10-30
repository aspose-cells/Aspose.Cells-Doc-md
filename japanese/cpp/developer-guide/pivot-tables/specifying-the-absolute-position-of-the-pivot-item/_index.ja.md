---
title: C++を使用してピボットアイテムの絶対位置を指定
linktitle: ピボットアイテムの絶対位置を指定する
type: docs
weight: 50
url: /ja/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Aspose.Cellsを使用してC++でピボットアイテムの絶対位置を指定する方法を学びます。
---

{{% alert color="primary" %}}

時々、ユーザーはピボットアイテムの絶対位置を指定する必要があります。Aspose.Cells APIはこの要件を達成するための新しいプロパティとメソッドを公開しています。

- 親ノードに関係なくすべてのPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)プロパティが追加されました。- 同じ親ノード内のPivotItemsの位置インデックスを指定するために使用できる[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)プロパティが追加されました。
- [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)メソッドを追加し、ピボットアイテムを上または下に移動させることができます。ここで、`count`は移動させる位置の数です。`count`の値が負の場合は上に移動し、正の場合は下に移動します。`isSameParent`は、移動操作が同じ親ノードで行われるかどうかを示すブール型のパラメータです。
- `PivotItem.Move(int count)`メソッドは廃止されました。したがって、新たに追加された[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)メソッドの使用を推奨します。

{{% /alert %}}

以下のサンプルコードは、ピボットテーブルを作成し、同じ親ノード内のピボットアイテムの位置を指定します。[ソースExcel](5112632.xlsx)と[出力Excel](5112619.xlsx)をダウンロードして参考にしてください。出力Excelを開くと、「4H12」が親「K11」の0番目の位置にあり、「DIF400」は3番目の位置にあります。同様に、CA32は位置1、AAA3は位置2にあります。

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

ご注意：`PivotTable.RefreshData`と`PivotTable.CalculateData`メソッドを呼び出す必要があることに注意してください。[**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)、[**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)プロパティおよび[**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/)メソッドを使用する前に。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
