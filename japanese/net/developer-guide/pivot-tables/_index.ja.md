---
title: ピボットテーブルの挿入
linktitle: ピボットテーブルの挿入
description: Excel スプレッドシートファイルでピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定.
type: docs
weight: 160
url: /ja/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは何ですか？**
ピボットテーブルは、対話型のサマリーレポートです。行ごとに記録された大量の生データを、数式を一切使用せずにコンパクトなマトリックスへまとめられます。どの列を行ラベルや列ラベルにするか、どの列を値として集計するかを指定すると、グループ化と計算はピボットテーブルが行います。
- **要約** — 長い数式の連鎖を必要とせず、製品別、地域別、四半期別などの売上合計を求められます。
- **比較** — 行にカテゴリ、列に期間を配置すると、平坦なリストを一目で傾向を把握できるクロスレポートに変換されます。
- **ドリルダウン** — 任意の集計値をダブルクリックして、その集計値に対応する元の行を確認できます。
- **更新** — ソースデータが変更されたとき、1 回の更新でレポート全体を再計算できます。
代表的な利用場面は、販売ダッシュボード、費用の内訳、在庫分析です。「カテゴリや時期ごとにこれらの数値をどのように内訳するか」という形式の質問に対応できます。Aspose.Cells for .NET は同じピボットテーブルをプログラムで構築できるため、アプリケーションが生成するワークブックには、生データだけでなくすぐに利用できるレポートを含めることができます。

### **ピボットテーブルのオブジェクトモデル**
Aspose.Cells は、ピボットテーブルの作成と制御に使用される一連の特殊なクラスを [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namespace に提供しています。これらのクラスは、ピボットテーブルの構成要素となる [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) オブジェクトを作成および設定するために使用されます。以下のオブジェクトが対象です。
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 内のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) は、[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) 内のすべての [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) は、ワークシート上のピボットテーブルを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) は、ワークシート上のすべての [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) オブジェクトのコレクションを表します。

### **Aspose.Cells を使用してピボットテーブルを作成する方法**
ピボットテーブルは、ソースデータをワークシートのセルに書き込み、指定した位置にピボットテーブルを追加して、ピボットフィールドを行、列、データ各領域に配置することで作成できます。
1. [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) オブジェクトの [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) メソッドを使用して、ワークシートのセルにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) コレクションの [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) メソッドを呼び出して、ワークシートにピボットテーブルを追加します: `Add(sourceData, row, column)`。`sourceData` はソース範囲です（例: "A1:C8"）。`row` と `column` は、ピボットテーブルの左上角となる宛先セルの 0 始まりの座標です（セル E3 は row 2、column 4 を意味します）。このメソッドは、新しく作成した [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) オブジェクトを直接返します。
3. [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) オブジェクトの `AddFieldToArea` メソッドでピボットフィールドを配置します。フィールド名を、行領域 (`PivotFieldType.Row`)、列領域 (`PivotFieldType.Column`)、またはデータ領域 (`PivotFieldType.Data`) に指定します。
4. ワークブックを保存すると、ピボットテーブルが保存されたファイルに書き込まれます。
サンプルコードを実行すると、ワークシートにピボットテーブルが追加されます。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 新しいワークブックを作成し、最初のワークシートを取得します
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// ソースデータを書き込みます: スポーツ別の四半期販売数
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// A1:C8 をソースとして、宛先セル E3 にピボットテーブルを追加します
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// ピボットフィールドを割り当てます: Sport を Rows に、Quarter を Columns に、Sales を Data に配置します
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// ワークブックを保存します
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
セル範囲をデータソースとして指定する場合、範囲は左上端から右下端への順で指定する必要があります。たとえば、"A1:C3" は有効ですが、"C3:A1" は無効です。
{{% /alert %}}

## 関連記事
- [Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更](/cells/ja/net/change-page-field-layout/)
- [ラベルまたは値によるピボットテーブルのフィルタリング](/cells/ja/net/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルの値フィールドを管理](/cells/ja/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}