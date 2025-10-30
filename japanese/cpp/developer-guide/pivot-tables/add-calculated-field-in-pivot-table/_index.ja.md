---
title: ピボットテーブルに計算フィールドを追加（C++）
linktitle: ピボットテーブルに計算フィールドを追加する
type: docs
weight: 130
url: /ja/cpp/add-calculated-field-in-pivot-table/
description: ピボットテーブルに計算フィールドを追加する方法（Aspose.Cells for C++用）
keywords: ピボットテーブルで既知のデータに基づいてピボットテーブルを作成すると、そのデータが望むものではないことがあります。望むデータは、これらの元のデータの組み合わせです。たとえば、データを望む前に元のデータを追加、減算、乗算、除算する必要があります。その場合、計算フィールドを構築し、計算のための対応する式を設定する必要があります。その後、計算フィールドにいくつかの統計およびその他の操作を行います。
---

## **可能な使用シナリオ**
既知のデータに基づいてピボットテーブルを作成すると、それに含まれるデータが望んでいるものではないことがあります。望んでいるデータは、これらの元のデータの組み合わせです。たとえば、データを望んだ形式にするために、元のデータを加算、減算、乗算、除算する必要があります。その場合、計算フィールドを構築し、計算用の対応する式を設定する必要があります。その後、計算フィールドで統計などの操作を行います。 

## **Excelのピボットテーブルに計算フィールドを追加**
Excelのピボットテーブルに計算フィールドを挿入するには、以下の手順に従います:

1. 追加したいピボットテーブルを選択します。 
2. リボットテーブルツールの「分析」タブに移動します。
3. 「フィールド、アイテム、およびセット」をクリックし、その後、ドロップダウンメニューから「計算フィールド」を選択します。
4. 「名前」フィールドに、計算フィールドの名前を入力します。
5. 「式」フィールドに、適切なピボットテーブルのフィールド名と数学演算子を使用して実行する計算の式を入力します。 
<br>
<img src="1.png" width=80% />
6. 「OK」をクリックして計算フィールドを作成します。
7. 新しい計算フィールドは、値のセクションの下にあるピボットテーブルフィールドリストに表示されます。
8. 計算フィールドをピボットテーブルの値セクションにドラッグして、計算された値を表示します。
<br>
<img src="2.png" width=80% />

## **C++を使ったピボットテーブルへの計算フィールド追加**
Aspose.Cellsを使用してExcelファイルに計算フィールドを追加します。次のサンプルコードを実行すると、ワークシートに計算フィールドを追加したピボットテーブルが追加されます。
1. 元のデータを設定し、ピボットテーブルを作成します。 
2. ピボットテーブル内の既存のPivotFieldに応じて計算フィールドを作成します。
3. 計算フィールドをデータ領域に追加します。 
4. 最後に、[output XLSX](out.xlsx)形式でブックを保存します。 

## **サンプルコード**
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
