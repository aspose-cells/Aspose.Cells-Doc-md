---
title: ピボットテーブルでの上位10件の表示またはフィルター処理
linktitle: ピボットテーブルでの上位10件の表示またはフィルター処理
description: ピボットフィールドで上位または下位の項目だけを表示する方法を Aspose.Cells for Java で学びます。この prudenceでは、Excel 97-2003 の Top10AutoShow メソッド、Top10AutoShowSettings によるオプションの読み取り、および FilterTop10 を使用した Excel 2007-365 の上位10件フィルターについて説明します。
keywords: Aspose.Cells, Java, ピボットテーブル, 上位10件, 自動表示, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /ja/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十の項目が含まれる場合、読み取りにくくなります。上位10件のレポートは、順位付けされた項目のうち上位または下位のみを表示します。これは、「売上による上位5製品」や「販売数による下位3地域」などのランキングレポートに必要な機能です。Aspose.Cells はこのために 2 つのメカニズムをサポートしており、それぞれ Microsoft Excel の 2 つの世代に対応します。
- **Excel 97-2003 自動表示** — `PivotField.top10AutoShow()` メソッド。これは、ピボットフィールドに直接保存される従来の「上位/下位 N 件を表示」設定です。初期のピボットテーブル形式の一部であるため、新旧を問わずすべての Excel バージョンで動作します。
- **Excel 2007-365 上位10件フィルター** — `PivotField.filterTop10()` メソッド。これは、フィールドメニューの「値フィルター」に表示される新しい上位10件値フィルターです。フィールドに関連付けられた `PivotFilter` オブジェクトとして保存され、項目数とパーセンテージに基づく順位付けを提供します。

## **Excel 97-2003 での上位10件の表示 (top10AutoShow)**
従来の自動表示は、`PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` を 1 回呼び出すことで設定します。
- `isAutoShow` — フィールドの自動表示設定を有効または無効にします。
- `isTop` — `true` の場合は上位の項目を保持し、`false` の場合は下位の項目を保持します。
- `count` — 保持する項目数です。たとえば、従来の上位10件レポートでは 10 を指定します。
- `rankBy` — 項目を順位付けするデータフィールドのゼロベースインデックスです。フィールド自体を基準に項目を順位付けするには、`rankBy` に -1 を指定します。
順位付けは、値フィールドまたはフィールド自体を基準にできます。以下に、代表的な 2 つの方法を示します。

### **値フィールドによる順位付け**
行フィールドの項目を、「Sales の合計」のような通常の値フィールドで順位付けします。次の例では、1 つの行フィールド (`Sport`) と 1 つのデータフィールド (`Sales`) を持つピボットテーブルを作成し、その後、売上による上位 2 件のスポーツを表示します。`rankBy` が 0 なのは、「Sales の合計」がインデックス 0 のデータフィールドだからです。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// 「Sum of Sales」で上位2項目を表示する（データフィールドのインデックス0）
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **フィールド自体による順位付け**
フィールド自体を基準に順位付けすることもできます。`rankBy` に -1 を指定します。この方法では追加のデータフィールドは不要で、フィールドを行（または列）領域に配置するだけで十分です。次の例では、フィールド自体を基準に順位付けした下位 3 件のスポーツを表示します。この設定を保存すると、-1 がこの形式の既定値であるため、ピボットテーブル XML から `rankBy` 属性が省略されます。また、`Top10AutoShowSettings.getRankBy()` により -1 が読み返されます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// フィールド自体でランキングされた下位3つの項目を表示 (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **現在のオプションの読み取り (Top10AutoShowSettings)**
`PivotField.getTop10AutoShowSettings()` メソッドは、フィールドに現在保存されている自動表示のオプションを参照できる `PivotFieldTop10AutoShowSettings` オブジェクトを返します。このオブジェクトを使用すると、既存のワークブック、または設定したばかりのピボットテーブルが項目をどのように表示するかを確認できます。ファイルから読み込んだワークブックも対象です。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

4 つのプロパティは、ピボットテーブル XML に書き込まれる従来の自動表示属性 (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) と対応しています。したがって、読み返される値は、どの Excel バージョンでもそのまま適用されます。

## **注記**

{{% alert color="primary" %}}
- `PivotField` に直接公開されている `isAutoShow()`、`isAscendShow()`、`getAutoShowCount()`、`getAutoShowField()` は、非推奨としてマークされています。代わりに `Top10AutoShowSettings` オブジェクトを使用してください。`Top10AutoShowSettings.isAutoShow()` は `PivotField.isAutoShow()` を、`Top10AutoShowSettings.isTop()` は `PivotField.isAscendShow()` を、`Top10AutoShowSettings.getAutoShowCount()` は `PivotField.getAutoShowCount()` を、`Top10AutoShowSettings.getRankBy()` は `PivotField.getAutoShowField()` を置き換えます。設定を変更するには、サポートされている `PivotField.top10AutoShow()` メソッドを使用してください。
- `top10AutoShow` は行フィールドと列フィールドで使用できます。ページ（フィルター）領域にのみ配置されているフィールドは、その項目がピボットテーブルの本体領域に配置されないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365: 上位10件フィルター (filterTop10)**
新しい Excel バージョンでは、フィールドメニューの「値フィルター」にある「上位10件」を値フィルターとして利用できます。Aspose.Cells では、`PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` メソッドでこの機能を実現しています。このメソッドは作成された `PivotFilter` を返します。
- `valueFieldIndex` — 集計値によって項目を順位付けするデータフィールドのゼロベースインデックスです。
- `type` — `itemCount` の意味を決定します。`PivotFilterType.COUNT` は固定数の項目を保持します（ダイアログの「項目」オプション）。`PivotFilterType.PERCENT` は項目の割合を保持するため、`itemCount` は割合自体を表します。30 を指定すると上位 30 パーセントを保持します。`PivotFilterType.SUM` は累積値によるカバレッジに基づいて順位付けします。
- `isTop` — 上位の場合は `true`、下位の場合は `false` です。
- `itemCount` — 「上位 N 件」の N を表します。単位は `type` によって決まります。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Top 10 フィルター - 「Sales の合計」に基づいて上位 2 項目を保持します（データフィールドのインデックスは 0）
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// パーセントベースのフィルターを使用する場合は、項目の上位 30% を保持します:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` と `filterTop10` は、互いに異なる 2 つの機能です。自動表示は、ピボットフィールドに設定される従来の `autoShow` 属性を書き込み、Excel 97 以降のすべての Excel バージョンで適用されます。`filterTop10` は Excel 2007 以降が必要な新しい `PivotFilter` エントリを書き込みます。古い Excel バージョンでワークブックを開くと、新しいフィルターを使用するピボットテーブルは、すべての項目を表示する動作にフォールバックします。レガシーツールとの往復処理が必要なドキュメントでは `top10AutoShow` を、新しいワークブックでは、他の値フィルターと組み合わせられる `filterTop10` を使用してください。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値によるピボットテーブルのフィルター処理](/cells/ja/java/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行フィールドと列フィールドを追加](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/java/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/java/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}