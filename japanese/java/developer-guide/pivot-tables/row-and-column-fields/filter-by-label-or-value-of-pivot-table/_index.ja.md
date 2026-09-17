---
title: ラベルまたは値でピボットテーブルをフィルタリングする
linktitle: ラベルまたは値でピボットテーブルをフィルタリングする
description: Aspose.Cells for Java は包括的なピボットテーブルのフィルタリング機能をサポートします。この記事では、ラベルフィルタ、日付フィルタ、値フィルタ、トップ10フィルタ、およびピボットアイテムの表示・非表示によるフィルタリング方法について説明します。
keywords: Aspose.Cells, Java ライブラリ, スプレッドシート, ピボットテーブル, フィルタ, ラベルフィルタ, 値フィルタ, 日付フィルタ, トップ10フィルタ, ピボットアイテム, ピボットアイテムを非表示
type: docs
weight: 10
url: /ja/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルタリングするための5つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルタを適用したり、フィールドに日時セルまたは空白のみが含まれている場合に日付フィルタを使用したり、集計された数値に対して値フィルタを適用したり、値フィールドによるランキングでトップ10フィルタを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを表示・非表示にしたりできます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}

## **Introduction**
ピボットテーブルは強力な分析ツールですが、生の集計には特定のレポートに必要なよりもはるかに多くの情報が含まれていることがよくあります。フィルタリングは、ピボットテーブルを特定のレポートにとって重要な行、列、または値に絞り込むための主要なメカニズムです。Aspose.Cells for Java は、Microsoft Excel で利用可能なフィルタリング機能をミラーリングし、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で説明するフィルタリング戦略は以下の通りです。
1. **ラベルフィルタ** — テキストラベルに基づいて行または列フィールドのアイテムをフィルタリングします。
2. **日付フィルタ** — 日時値（または空白）のみを含む行または列フィールドをフィルタリングします。
3. **値フィルタ** — データフィールドの集計値に基づいてアイテムをフィルタリングします。
4. **トップ10フィルタ** — 値フィールドでランク付けされた上位または下位のN個のアイテムのみを表示します。
5. **ピボットアイテムの表示/非表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは、`PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルタを適用した後、キャッシュされたデータと計算値が新しいフィルタ状態を反映するように、ピボットテーブルで `refreshData()` と `calculateData()` を呼び出す必要があります。

## **Label Filter**
ラベルフィルタを使用すると、行または列フィールドのアイテムを、テキストキャプションとパターンを比較してフィルタリングできます。これは、特定の文字で始まる名前、特定の単語を含む名前、または他のキャプションベースの基準に一致する製品のみを表示する場合に便利です。
Aspose.Cells は、ラベルフィルタリングを `PivotField.filterByLabel(PivotFilterType, String)` メソッドを通じて公開しています。`PivotFilterType` 列挙型には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2番目の引数は比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まるアイテムのみが表示されるようにするラベルフィルタを適用し、ピボットテーブルを更新して結果を保存します。

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook(fileName);
// インデックスでワークシートにアクセスする（最初のワークシート）
Worksheet worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// 最初の行のPivotFieldを取得する
PivotField rowField = pivotTable.getRowFields().get(0);
// ラベルフィルターを適用する - 指定されたプレフィックスで始まるラベルの行項目のみを表示する
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// フィルターが反映されるようにピボットテーブルのデータを更新して再計算する
pivotTable.refreshData();
// ワークブックをディスクに保存する
workbook.save(fileName);
```

## **Date Filter**
日付フィルタを使用すると、今日、先週、今月、次の四半期、または特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日時情報を格納するフィールドに対してのみ機能する特殊なフィルタです。

{{% alert color="primary" %}}
日付フィルタは、行または列領域に日時セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルタは期待された結果を生成しません。このフィルタを適用する前に、フィールドが日付として書式設定されており、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}

Aspose.Cells は、日付フィルタリングを `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを通じて公開しています。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用の日付値が含まれます。選択したフィルタタイプに応じて、1つまたは2つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを持つワークブックを読み込み、特定の日付範囲に表示されるアイテムを制限する日付フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook(inputPath);
// ピボットテーブルを含むワークシートにアクセスする（インデックス指定）
Worksheet worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// 行エリアから日付のPivotFieldを取得する
// （日付フィルタは行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します）
PivotField dateField = pivotTable.getRowFields().get(0);
// Betweenフィルタの日付条件を指定する
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// ピボットフィールドに日付フィルタを適用する
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// フィルタを反映させるためにピボットテーブルを更新して再計算する
pivotTable.refreshData();
// ワークブックを保存する
workbook.save(outputPath);
```

## **Value Filter**
値フィルタは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的な使用例には、売上合計が目標額を超える製品のみを表示する、またはトランザクション数が範囲内にある地域のみを表示するなどがあります。
Aspose.Cells は、値フィルタリングを `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` メソッドを通じて公開しています。`filterType` パラメータは、`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価されるデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを持つワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// PivotFieldCollection に IndexOf がないため、データフィールドのインデックスを手動で見つけます
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
pivotTable.refreshData();
workbook.save("output.xlsx");
```

## **Top 10 Filter**
トップ10フィルタは、選択した値フィールドに基づいて最高または最低のN個のアイテムのみを保持する、値フィルタの特殊な形式です。「売上によるトップ10製品」や「販売数によるワースト5地域」などのランキングレポートによく使用されます。

{{% alert color="primary" %}}
トップ10フィルタは、データ領域に1つ以上の値ピボットフィールドがある場合にのみ有効です。少なくとも1つの値フィールドがないと、アイテムのランク付けに使用する集計された指標がなく、フィルタを適用できません。
{{% /alert %}}

Aspose.Cells は、トップ10フィルタリングを `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じて公開しています。`itemCount` パラメータは保持するアイテムの数を定義し、`isTop` は上位アイテムを保持する（true）か下位アイテムを保持するか（false）を示し、`valueField` はランク付けに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` も可能です）。
次の例では、値フィールドを含むピボットテーブルを持つワークブックを読み込み、売上の合計による上位10個のアイテムのみを保持するトップ10フィルタを適用し、ピボットテーブルを更新してワークブックを保存します。

```java
import com.aspose.cells.*;
// ピボットテーブルを含む既存のワークブックを読み込む
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// ピボットテーブルを含むワークシートにアクセスする(インデックス0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// データ領域に少なくとも1つの値PivotFieldがあることを確認する
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// 対象の行PivotFieldを取得する(Top 10を適用するフィールド)
PivotField rowField = pivotTable.getRowFields().get(0);
// 最初(かつ唯一の)データフィールドはインデックス0にあります。Top 10はこれでランク付けします。
int valueFieldIndex = 0;
// 行フィールドにTop 10フィルターを適用する:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (上位N件; falseの場合は下位N件)
//   - valueFieldIndex = アイテムのランク付けに使用されるデータフィールドのインデックス
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);
// ピボットテーブルのデータを更新し、フィルターが適用されるように再計算する
pivotTable.refreshData();
// ワークブックを保存する
workbook.save(outputPath);
```

## **Filter by Hiding or Unhiding Pivot Items**
構造化されたフィルタ API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御することもできます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルタを適用せずに特定のアイテムを選択的に非表示にできます。`IsHidden = true` を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false` を設定するとアイテムの非表示が解除されて再び表示されるようになります。
このアプローチは、フィルタリングルールが不規則またはアイテム固有である場合、特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にする場合などに便利です。以下の例では、ピボットテーブルを読み込み、名前で特定のアイテムを非表示にし、非表示を解除する方法を示し、ピボットテーブルを更新してワークブックを保存します。

```java
import com.aspose.cells.*;
// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// ピボットテーブルを含む最初のワークシートにアクセスする
Worksheet sheet = workbook.getWorksheets().get(0);
// インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
PivotTable pivotTable = sheet.getPivotTables().get(0);
// 対象のPivotFieldを取得する（項目を非表示/再表示する最初の行ラベルフィールド）
PivotField pivotField = pivotTable.getRowFields().get(0);
// 選択したPivotFieldのPivotItemsコレクションを反復処理する
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // 特定の名前/条件に一致するピボット項目を非表示にする
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }
    // 再表示のデモ：以前に非表示にしたピボット項目を再度表示する
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}
// 変更を有効にするためにピボットテーブルを更新して再計算する
pivotTable.refreshData();
// ワークブックを保存する - 非表示項目は基となるデータには残る
// ただし表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx");
```

## **Summary**
Aspose.Cells for Java は、Microsoft Excel で利用可能なものと同等の完全なピボットテーブルフィルタリング機能を提供します。ラベル、値、および日付フィルタは最も一般的な分析シナリオをカバーし、トップ10フィルタはランキングレポートを処理します。フィルタリングルールが不規則な場合、`PivotItem.IsHidden` プロパティは柔軟なアイテムレベルの代替手段を提供します。これらの戦略を組み合わせること（たとえば、ラベルフィルタを適用してから特定のアイテムを非表示にする）により、完全にコードから正確にターゲットを絞ったピボットテーブルレポートを構築できます。

## Related Articles
- [ピボットテーブルの挿入](/cells/ja/java/pivot-tables/)
- [Aspose.Cells for Java でピボットテーブルの行と列フィールドを追加する](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加する](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルの値フィールドを管理する](/cells/ja/java/manage-value-fields/)
- [Aspose.Cells for Java でピボットテーブルとピボットキャッシュを更新する](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}