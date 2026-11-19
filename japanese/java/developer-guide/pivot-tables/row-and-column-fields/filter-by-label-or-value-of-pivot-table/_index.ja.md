---
title: ラベルまたは値によるピボットテーブルのフィルタリング
linktitle: ラベルまたは値によるピボットテーブルのフィルタリング
description: Aspose.Cells for Java は包括的なピボットテーブルのフィルター機能をサポートしています。このアーティクルでは、ラベルフィルター、日付フィルター、値フィルター、上位 10 件フィルター、およびピボット項目を非表示または表示する機能を使って、ピボットテーブルのデータをフィルターする方法を説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, 上位 10 件フィルター, ピボット項目, ピボット項目の非表示
type: docs
weight: 10
url: /ja/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルターするための実用的な戦略を 5 つ提供します。テキストベースの行フィールドまたは列フィールドにはラベルフィルターを、日時セルまたは空白のみを含むフィールドには日付フィルター、集約された数値には値フィルター、値フィールドによるランキングには上位 10 件フィルターを適用できます。また、`IsHidden` プロパティを使用して個々のピボット項目を手動で非表示または表示することもできます。
これらの戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を使って適用できます。
{{% /alert %}}

## **はじめに**
ピボットテーブルは強力な分析ツールですが、集計結果そのものには、提示する必要のない情報が含まれることがよくあります。フィルターは、ピボットテーブルを特定のレポートに必要な行、列、または値に絞り込む主な手段です。Aspose.Cells for Java は、Microsoft Excel と同じフィルター機能をプログラムから利用できるため、レポート生成を完全に自動化できます。
このアーティクルでは、次のフィルター戦略について説明します。
1. **ラベルフィルター** — テキストラベルに基づいて、行または列フィールドの項目をフィルターします。
2. **日付フィルター** — 日時値（または空白）のみを含む行または列フィールドをフィルターします。
3. **値フィルター** — データフィールドの集計値に基づいて項目をフィルターします。
4. **上位 10 件フィルター** — 値フィールドによるランキングで上位または下位 N 件のみを表示します。
5. **ピボット項目の非表示 / 表示** — フィールド内の個々の項目の表示を手動で制御します。
各手法では、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスの異なるプロパティを使用します。フィルターを適用した後、新しいフィルター状態をキャッシュされたデータと計算結果に反映するには、ピボットテーブルで `getPivotCache().refresh()` を呼び出す必要があります。

## **ラベルフィルター**
ラベルフィルターを使用すると、行または列フィールドの項目を、テキストキャプションとパターンと比較することでフィルターできます。特定の文字で始まる製品名、特定の単語を含む製品名、またはその他のキャプションに基づく基準に一致する製品だけを表示したい場合に便利です。
Aspose.Cells では、`PivotField.filterByLabel(PivotFilterType, String)` メソッドを使ってラベルフィルターを適用できます。`PivotFilterType` 列挙型には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数には、比較に使用するラベル文字列を指定します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、指定した接頭辞でキャプションが始まる項目だけが残るようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、来四半期、または特定の日付範囲など、日付に基づく基準でピボットテーブルを絞り込めます。これらは、日時情報を格納するフィールドでのみ機能する特殊なフィルターです。

{{% alert color="primary" %}}
日付フィルターは、行領域または列領域に日時セルまたは空白値のみが含まれている場合にのみ機能します。対象のフィールドに数値やテキストなど他のデータ型が含まれている場合、日付フィルターは期待どおりの結果になりません。このフィルターを適用する前に、フィールドが日付として書式設定されていること、および各値が有効な `DateTime` インスタンスであるか、該当セルが空であることを確認してください。
Aspose.Cells では、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを使って日付フィルターを適用できます。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルターの種類に応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は、開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを持つワークブックを読み込み、表示可能な項目を特定の日付範囲に制限する日付フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合するのではなく、数値の合計をしきい値と比較します。代表的な使用例としては、販売額の合計が目標金額を超える製品だけを表示する、または取引件数が特定の範囲に収まる地域だけを表示する、といった場合があります。
Aspose.Cells では、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` メソッドを使って値フィルターを適用できます。`filterType` パラメーターには、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を指定します。`valueField` パラメーターは評価するデータフィールドを指定し、残りの引数にはしきい値を指定します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集約された販売値が数値のしきい値を超える項目だけを残す値フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **上位 10 件フィルター**
上位 10 件フィルターは、選択した値フィールドに基づいて、上位または下位 N 件だけを残す値フィルターの特殊な形式です。「売上金額による上位 10 製品」や「取引件数による下位 5 地域」などのランキングレポートで広く使用されます。

{{% alert color="primary" %}}
上位 10 件フィルターは、データ領域に 1 つ以上の値ピボットフィールドがある場合にのみ有効です。値フィールドが 1 つもない場合、項目を順位付けするための集計指標が存在せず、フィルターを適用できません。
Aspose.Cells では、`PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)` メソッドを使って上位 10 件フィルターを適用できます。`valueFieldIndex` パラメーターは、集約値に基づいて項目を順位付けするデータフィールドのインデックスであり、`filterType` は `itemCount` の単位を選択します（`PivotFilterType.COUNT` は固定数の項目を残し、`PivotFilterType.PERCENT` は項目の割合を残すため、`itemCount` はその割合自体になります）。`isTop` は上位項目を残すか（true）、下位項目を残すか（false）を示し、`itemCount` は残す項目数または割合を指定します。
次の例では、値フィールドを持つピボットテーブルを含むワークブックを読み込み、販売量の合計による上位 10 件だけを残す上位 10 件フィルターを適用して、ピボットテーブルを更新し、ワークブックを保存します。
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **ピボット項目の非表示または表示によるフィルター**
構造化されたフィルター API に加えて、Aspose.Cells では個々のピボット項目の表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復し、`IsHidden` プロパティの値を切り替えることで、数式ベースのフィルターを適用せずに特定の項目を選択的に非表示にできます。`IsHidden = true` に設定すると、その項目はピボットテーブルから非表示になります。`IsHidden = false` に設定すると、非表示が解除され、項目が再び表示されます。
この方法は、特定のレポートに表示すべきでない少数のカテゴリを非表示にするなど、フィルター条件が不規則または項目固有である場合に便利です。以下の例では、ワークブックを読み込み、そのピボットテーブルで特定の項目を名前によって非表示にし、項目を表示する方法も示します。その後、ピボットテーブルを更新し、ワークブックを保存します。

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **概要**
Aspose.Cells for Java は、Microsoft Excel と同等の完全なピボットテーブルフィルター機能を提供します。ラベル、日付、値のフィルターは最も一般的な分析シナリオに対応し、上位 10 件フィルターはランキングレポートにも対応します。フィルター条件が不規則な場合は、`PivotItem.IsHidden` プロパティが柔軟な項目単位の代替手段となります。これらの戦略を組み合わせることで（たとえば、ラベルフィルターを適用してから特定の項目を非表示にする）、対象を的確に絞ったピボットテーブルのレポートをすべてコードから作成できます。

## 関連記事
- [ピボットテーブルの挿入](/cells/ja/java/create-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルに行と列フィールドを追加](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルの値フィールドを管理](/cells/ja/java/manage-value-fields/)
- [Aspose.Cells for Java でピボットテーブルとピボットキャッシュを更新](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}