---
title: C++でピボットフィルター
linktitle: ピボットフィルタ
type: docs
weight: 130
url: /ja/cpp/add-or-clear-pivot-filter/
description: C++を使用してAspose.Cellsでピボットテーブルにフィルターを追加する方法を学ぶ
keywords: オフィス 2013、オフィス 2016、オフィス 2019、およびオフィス 365を使用せずにピボットテーブルにフィルタを追加する。
---

## **可能な使用シナリオ**
既知のデータを使ってピボットテーブルを作成し、フィルタリングしたい場合は、フィルタを学び、使う必要があります。これにより、目的のデータを効果的にフィルターできます。Aspose.Cells APIを使用すると、フィールド値にフィルタを追加およびクリアできます。 

## **Excelでピボットテーブルにフィルタを追加する方法**
Excelのピボットテーブルにフィルタを追加するには、次の手順に従います:

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルに追加したいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「トップ10」を選択します。
<br>
<img src="3.png" width=80% />
4. 表示モードとフィルタの数を設定します。
<br>
<img src="4.png" width=80% />

## **ピボットテーブルにフィルタを追加**
次のサンプルコードを参照してください。データを設定し、それに基づいてPivotTableを作成します。次に、ピボットテーブルの行フィールドにフィルタを追加します。最後に、[output XLSX](filterout.xlsx)形式でブックを保存します。サンプルコードを実行した後は、ワークシートにトップ10フィルタが追加されたピボットテーブルが表示されます。

### **サンプルコード**
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

## **Excelのピボットテーブルのフィルタをクリアする方法**
Excelでピボットテーブルのフィルタをクリアするには、以下の手順に従います：

1. クリアしたいPivotTableを選択します。 
2. ピボットテーブルでクリアしたいフィルタのドロップダウン矢印をクリックします。
3. ドロップダウンメニューから「フィルタをクリア」を選択します。
<br>
<img src="1.png" width=80% />
4. ピボットテーブルからすべてのフィルタをクリアしたい場合は、ExcelのリボンのPivotTable Analyzeタブで「フィルタをクリア」ボタンをクリックすることもできます。
<br>
<img src="2.png" width=80% />

## **ピボットテーブルのフィルタをクリア**
Aspose.Cellsを使用したピボットテーブルでのフィルタのクリア。次のサンプルコードを参照してください。 
1. データを設定し、それに基づいてPivotTableを作成します。 
2. ピボットテーブルの行フィールドにフィルタを追加します。 
3. [output XLSX](out_add.xlsx)形式でブックを保存します。サンプルコードを実行した後は、ワークシートにトップ10フィルタが追加されたピボットテーブルが表示されます。 
4. 特定のピボットフィールドのフィルタをクリアします。フィルタをクリアするコードを実行した後、特定のピボットフィールドのフィルタがクリアされます。[output XLSX](out_delete.xlsx)をご確認ください。

### **サンプルコード**
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
