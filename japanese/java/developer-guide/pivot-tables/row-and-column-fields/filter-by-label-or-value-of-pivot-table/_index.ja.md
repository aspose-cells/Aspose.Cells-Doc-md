---
title: ピボットテーブルのラベルまたは値によるフィルター処理
linktitle: ピボットテーブルのラベルまたは値によるフィルター処理
description: Aspose.Cells for Java は包括的なピボットテーブルのフィルター機能をサポートしています。この記事では、ラベルフィルター、日付フィルター、値フィルター、トップ10フィルター、およびピボットアイテムの表示/非表示によるピボットデータのフィルター方法を説明します。
keywords: Aspose.Cells, Javaライブラリ, スプレッドシート, ピボットテーブル, フィルター, ラベルフィルター, 値フィルター, 日付フィルター, トップ10フィルター, ピボットアイテム, ピボットアイテムの非表示
type: docs
weight: 10
url: /ja/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells は、ピボットテーブルに表示されるデータをフィルター処理するための 5 つの実用的な戦略を提供します。テキストベースの行または列フィールドにラベルフィルターを適用したり、フィールドに日付時刻セルまたは空白のみが含まれる場合に日付フィルターを使用したり、集計数値に対して値フィルターを適用したり、値フィールドによるランキングのためにトップ10フィルターを使用したり、`IsHidden` プロパティを使用して個々のピボットアイテムを手動で非表示または再表示したりすることができます。各戦略は、`PivotField` クラスと `PivotItem` クラスの専用 API を通じて公開されています。
{{% /alert %}}
## **はじめに**
ピボットテーブルは強力な分析ツールですが、生の概要には、特定のレポートで提示する必要がある情報をはるかに超える情報が含まれていることがよくあります。フィルター処理は、特定のレポートにとって重要な行、列、または値にピボットテーブルを絞り込むための主要なメカニズムです。Aspose.Cells for Java は、Microsoft Excel で利用可能なフィルター機能を反映し、レポート生成を完全に自動化できるようにプログラム的に公開しています。
この記事で扱うフィルター戦略は次のとおりです。
1. **ラベルフィルター** — テキストラベルに基づいて行または列フィールドのアイテムをフィルターします。
2. **日付フィルター** — 日付時刻値（または空白）のみを含む行または列フィールドをフィルターします。
3. **値フィルター** — データフィールドの集計値に基づいてアイテムをフィルターします。
4. **トップ10フィルター** — 値フィールドによるランキングで上位または下位 N 個のアイテムのみを表示します。
5. **ピボットアイテムの表示/非表示** — フィールド内の各アイテムの表示を手動で制御します。
各アプローチは `PivotField` クラスの異なるメソッド、または `PivotItem` クラスのプロパティを使用します。フィルターを適用した後、ピボットテーブルで `refreshData()` と `calculateData()` を呼び出して、キャッシュされたデータと計算値が新しいフィルター状態を反映するようにする必要があります。
## **ラベルフィルター**
ラベルフィルターを使用すると、テキストキャプションをパターンと比較して、行または列フィールドのアイテムをフィルターできます。これは、特定の文字で始まる名前、特定の単語を含む名前、または他のキャプションベースの基準に一致する商品のみを表示したい場合に役立ちます。
Aspose.Cells は、`PivotField.filterByLabel(PivotFilterType, String)` メソッドを通じてラベルフィルターを公開しています。`PivotFilterType` 列挙型には、`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` などの値が含まれます。2 番目の引数は比較に使用されるラベル文字列を提供します。
次の例では、既存のピボットテーブルを含むワークブックを読み込み、キャプションが指定されたプレフィックスで始まるアイテムのみが表示されるようにラベルフィルターを適用し、ピボットテーブルを更新して結果を保存します。
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

// 最初の行の PivotField を取得する
PivotField rowField = pivotTable.getRowFields().get(0);

// ラベルフィルターを適用する - 指定された接頭辞で始まるラベルの行項目のみを表示する
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// フィルターを有効にするためにピボットテーブルのデータを更新して再計算する
pivotTable.refreshData();

// ワークブックをディスクに保存する
workbook.save(fileName);
```
## **日付フィルター**
日付フィルターを使用すると、今日、先週、今月、次の四半期、または特定の日付範囲などの日付ベースの基準でピボットテーブルを絞り込むことができます。これらは、日付時刻情報を格納するフィールドに対してのみ機能する特殊なフィルターです。
{{% alert color="primary" %}}
日付フィルターは、行または列領域に日付時刻セルまたは空白値のみが含まれている場合にのみ機能します。基になるフィールドに数値やテキストなどの他のデータ型が含まれている場合、日付フィルターは期待どおりの結果を生成しません。このフィルターを適用する前に、フィールドが日付として書式設定され、すべての値が有効な `DateTime` インスタンスまたは空のセルであることを確認してください。
{{% /alert %}}
Aspose.Cells は、`PivotField.filterByDate(PivotFilterType, params DateTime[] values)` メソッドを通じて日付フィルターを公開しています。`PivotFilterType` 列挙型には、`Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear`、`Between` などの専用日付値が含まれます。選択したフィルタータイプに応じて、1 つまたは 2 つの `DateTime` 値を渡します（`Between` の場合は開始日と終了日を渡します）。
次の例では、行領域に日付フィールドを含むピボットテーブルを含むワークブックを読み込み、表示可能なアイテムを特定の日付範囲に制限する日付フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// ピボットテーブルを含む既存のワークブックを読み込みます
Workbook workbook = new Workbook(inputPath);

// ピボットテーブルを保持するワークシートに（インデックスで）アクセスします
Worksheet worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスします
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// 行エリアから日付のPivotFieldを取得します
// (日付フィルターは行/列エリアに日時セルまたは空白のみが含まれている場合にのみ機能します)
PivotField dateField = pivotTable.getRowFields().get(0);

// Betweenフィルターの日付基準を定義します
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// ピボットフィールドに日付フィルターを適用します
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// フィルターを有効にするためにピボットテーブルを更新して再計算します
pivotTable.refreshData();

// ワークブックを保存します
workbook.save(outputPath);
```
## **値フィルター**
値フィルターは、ピボットテーブルがデータ領域で計算する集計値に対して機能します。テキストラベルを照合する代わりに、数値の合計をしきい値と比較します。典型的なユースケースには、売上合計が目標額を超える製品のみを表示する、またはトランザクション数が範囲内に収まる地域のみを表示するなどが含まれます。
Aspose.Cells は、`PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` メソッドを通じて値フィルターを公開しています。`filterType` パラメータは `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual`、`ValueLessThanOrEqual` などの値を使用します。`valueField` パラメータは評価されるデータフィールドを指定し、最後の引数はしきい値を提供します。
次の例では、ピボットテーブルを含むワークブックを読み込み、集計された売上が数値のしきい値を超えるアイテムのみを保持する値フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// PivotFieldCollectionにIndexOfがないため、データフィールドのインデックスを手動で検索する
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
## **トップ10フィルター**
トップ10フィルターは、選択した値フィールドに基づいて最高または最低の N 個のアイテムのみを保持する、値フィルターの特殊な形式です。「収益別トップ10製品」や「売上数別ワースト5地域」などのランキングレポートで一般的に使用されます。
{{% alert color="primary" %}}
トップ10フィルターは、ピボットテーブルのデータ領域に 1 つ以上の値ピボットフィールドがある場合にのみ効果的です。少なくとも 1 つの値フィールドがないと、アイテムをランキングするための集計メジャーがないため、フィルターを適用できません。
{{% /alert %}}
Aspose.Cells は、`PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` メソッドを通じてトップ10フィルターを公開しています。`itemCount` パラメータは保持するアイテム数を定義し、`isTop` は上位アイテムを保持するかどうかを示し（true で上位、false で下位）、`valueField` はランキングに使用されるデータフィールドを参照し、`filterType` は値の計算方法を制御します（通常は `Sum` ですが、`Count` や `Percent` もあります）。
次の例では、値フィールドを含むピボットテーブルを含むワークブックを読み込み、売上の合計で上位 10 個のアイテムのみを保持するトップ10フィルターを適用し、ピボットテーブルを更新してワークブックを保存します。
```java
import com.aspose.cells.*;

// ピボットテーブルを含む既存のワークブックを読み込む
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// ピボットテーブルを保持するワークシートにアクセスする (インデックス0)
Worksheet worksheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// データ領域に少なくとも1つの値PivotFieldがあることを確認する
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// 対象の行PivotFieldを取得する (Top 10を適用するフィールド)
PivotField rowField = pivotTable.getRowFields().get(0);

// 最初(かつ唯一の)データフィールドはインデックス0にある。Top 10はこれによってランク付けされる。
int valueFieldIndex = 0;

// 行フィールドにTop 10フィルターを適用する:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (上位N件; falseは下位N件を意味する)
//   - valueFieldIndex = アイテムをランク付けするために使用されるデータフィールドのインデックス
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// ピボットテーブルのデータを更新し、再計算してフィルターを有効にする
pivotTable.refreshData();

// ワークブックを保存する
workbook.save(outputPath);
```
## **ピボットアイテムの表示/非表示によるフィルター**
構造化されたフィルター API に加えて、Aspose.Cells では各ピボットアイテムの表示を直接制御できます。`PivotField` の `PivotItems` コレクションを反復処理し、`IsHidden` プロパティを切り替えることで、数式ベースのフィルターを適用せずに特定のアイテムを選択的に除外できます。`IsHidden = true` を設定するとアイテムがピボットテーブルから非表示になり、`IsHidden = false` を設定すると再表示されて再び表示されるようになります。
このアプローチは、フィルター規則が不規則であるか、アイテム固有である場合（特定のレポートに表示すべきでない少数の名前付きカテゴリを非表示にするなど）に役立ちます。以下の例では、ピボットテーブルを読み込み、特定のアイテムを名前で非表示にし、再表示する方法を実証し、ピボットテーブルを更新してワークブックを保存します。
```java
import com.aspose.cells.*;

// ピボットテーブルを含む既存のワークブックを読み込む
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// ピボットテーブルを含む最初のワークシートにアクセスする
Worksheet sheet = workbook.getWorksheets().get(0);

// インデックスでピボットテーブルにアクセスする（シート上の最初のピボットテーブル）
PivotTable pivotTable = sheet.getPivotTables().get(0);

// 対象のPivotFieldを取得する（アイテムの表示/非表示を切り替える最初の行ラベルフィールド）
PivotField pivotField = pivotTable.getRowFields().get(0);

// 選択したPivotFieldのPivotItemsコレクションを反復処理する
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // 特定の名前/条件に一致するピボットアイテムを非表示にする
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // 非表示解除のデモ: 非表示にしていたピボットアイテムを再表示する
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// 変更を反映するためピボットテーブルを更新して再計算する
pivotTable.refreshData();

// ワークブックを保存 - 非表示アイテムは元データに残る
// ただし、表示されるピボットテーブルの出力からは除外される
workbook.save("output_pivot_filtered.xlsx");
```
## **まとめ**
Aspose.Cells for Java は、Microsoft Excel にあるものと同等の完全なピボットテーブルフィルター機能を提供します。ラベルフィルター、日付フィルター、値フィルターは最も一般的な分析シナリオをカバーし、トップ10フィルターはランキングレポートを処理します。フィルター規則が不規則な場合、`PivotItem.IsHidden` プロパティは柔軟なアイテムレベルのフォールバックを提供します。これらの戦略を組み合わせる（たとえば、ラベルフィルターを適用してから特定のアイテムを非表示にする）ことで、完全にコードから正確にターゲットを絞ったピボットテーブルレポートを構築できます。
## 関連記事
- [ピボットテーブルの挿入](/cells/ja/java/pivot-tables/)
- [Aspose.Cells for Java でピボットテーブルの行と列フィールドを追加](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルの値フィールドを管理](/cells/ja/java/manage-value-fields/)
- [Aspose.Cells for Java でピボットテーブルとピボットキャッシュを更新](/cells/ja/java/refresh-pivot-table/)
{{< app/cells/assistant language="java" >}}