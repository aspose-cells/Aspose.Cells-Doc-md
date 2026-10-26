---
title: Aspose.Cells for C++ における値フィールド
description: Aspose.Cells for C++ でピボットテーブルのデータ領域に基本フィールドを追加する方法、PivotField.Function で集計関数を変更する方法、値フィールドを行軸や列軸に配置する方法を解説します。
linktitle: Aspose.Cells for C++ における値フィールド
keywords: Aspose.Cells, C++, ピボットテーブル, 値フィールド, PivotField, PivotField.Function, データフィールド, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /ja/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## データ領域へのフィールド追加
データ (値) 領域に基本フィールドを追加することは、ソースデータの集計方法を形作る最初のステップです。Aspose.Cells は `PivotTable.AddFieldToArea(PivotFieldType, string)` を提供します。このオーバーロードは、定数 `PivotFieldType.Data` とソース列名を受け取ります。データ領域にフィールドを追加すると、API はそのフィールドを `PivotTable.DataFields` コレクションに追加された順序で公開します。既定では、数値型のソース列は `ConsolidationFunction.Sum` で集計され、非数値型の列は `Count` が既定値となります。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    Cells cells = worksheet.GetCells();
    // A1:D1のヘッダー
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));
    // A2:D9のデータ行を、jで分岐するネストループで設定
    for (int i = 1; i <= 8; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            switch (j)
            {
                case 0:
                    cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
                    break;
                case 1:
                    if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
                    else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
                    else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
                    else cells.Get(i, j).PutValue(U16String("Daikon"));
                    break;
                case 2:
                    cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
                    break;
                case 3:
                    if (i == 1) cells.Get(i, j).PutValue(100);
                    else if (i == 2) cells.Get(i, j).PutValue(150);
                    else if (i == 3) cells.Get(i, j).PutValue(80);
                    else if (i == 4) cells.Get(i, j).PutValue(90);
                    else if (i == 5) cells.Get(i, j).PutValue(50);
                    else if (i == 6) cells.Get(i, j).PutValue(60);
                    else if (i == 7) cells.Get(i, j).PutValue(40);
                    else cells.Get(i, j).PutValue(45);
                    break;
            }
        }
    }
 // F3にPivotTable1という名前のピボットテーブルを追加
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);
    // ピボットレイアウト: 行にCategoryとItem、列にYear、データフィールドにAmountを配置
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    workbook.Save(u"output_drag.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 集計関数の変更
データ領域に配置された各フィールドは内部的に `PivotField` インスタンスとしてラップされ、その `Function` プロパティは `ConsolidationFunction` 列挙体の値を返します。同じ `Function` セッターで、利用可能な集計 (`Sum`、`Count`、`Average`、`Max`、`Min`、`Product`、`StdDev`、`StdDevp`、`Var`、`Varp` など) を切り替えられます。

{{% alert color="primary" %}}
`Function` を変更しても集計にのみ影響し、ソース列は変更されません。
したがって、1 つのデータフィールドを `Sum` のままにしておきながら、同じソース列を対象とする 2 番目のデータフィールドを `Count` や `Average` で追加することが、すべて 1 つのピボット内で行えます。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana", u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) {
                worksheet.GetCells().Get(i, j).PutValue(i <= 4 ? u"Fruit" : u"Vegetable");
            } else if (j == 1) {
                worksheet.GetCells().Get(i, j).PutValue(items[i - 1]);
            } else if (j == 2) {
                worksheet.GetCells().Get(i, j).PutValue(years[i - 1]);
            } else {
                worksheet.GetCells().Get(i, j).PutValue(amounts[i - 1]);
            }
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField countField = pivotTable.GetDataFields().Get(1);
    countField.SetFunction(ConsolidationFunction::Count);

    pivotTable.CalculateData();

    wb.Save(u"output_function.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## 値フィールドを行軸または列軸に配置する
ピボットテーブルに 2 つ以上のデータフィールドが含まれている場合、Aspose.Cells は `PivotTable.ValuesField` という追加の仮想フィールドを公開します。この仮想フィールドは、データ領域に存在するすべてのデータフィールドの集計を表します。これを基本ピボットフィールドとして行領域または列領域にドラッグすることができ、複数のメジャーを並べてレイアウトする場合に役立ちます。

{{% alert color="primary" %}}
値フィールドが存在しない場合や 1 つしかない場合、`PivotTable.ValuesField` は機能しません。
以下のシナリオでは、同じピボット構造に対して上記の各機能を示す 3 つのエンドツーエンドの例を順に説明します。
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();
    cells.Get(0, 0).PutValue(U16String("Category"));
    cells.Get(0, 1).PutValue(U16String("Item"));
    cells.Get(0, 2).PutValue(U16String("Year"));
    cells.Get(0, 3).PutValue(U16String("Amount"));

    std::vector<U16String> categories = {
        U16String("Fruit"), U16String("Fruit"), U16String("Fruit"), U16String("Fruit"),
        U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable"), U16String("Vegetable")
    };
    std::vector<U16String> items = {
        U16String("Apple"), U16String("Apple"), U16String("Banana"), U16String("Banana"),
        U16String("Carrot"), U16String("Carrot"), U16String("Daikon"), U16String("Daikon")
    };
    int years[8] = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[8] = { 100, 150, 80, 90, 50, 60, 40, 45 };

    for (int i = 1; i <= 8; i++) {
        for (int j = 0; j <= 3; j++) {
            if (j == 0) cells.Get(i, j).PutValue(categories[i - 1]);
            else if (j == 1) cells.Get(i, j).PutValue(items[i - 1]);
            else if (j == 2) cells.Get(i, j).PutValue(years[i - 1]);
            else cells.Get(i, j).PutValue(amounts[i - 1]);
        }
    }

    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:D9", 2, 5);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::Count);

    pivotTable.AddFieldToArea(PivotFieldType::Column, pivotTable.GetValuesField().GetName());

    pivotTable.CalculateData();
    workbook.Save(u"output_plot.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}