---
title: ピボットテーブルの作成
linktitle: ピボットテーブルの作成
description: Aspose.Cells for Java を使用してピボットテーブルを作成し、書式を設定します。
keywords: ピボットテーブルの作成, ピボットテーブルの挿入, ピボットテーブルの書式設定。
type: docs
weight: 160
url: /ja/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ピボットテーブルとは？**
ピボットテーブルは、インタラクティブなサマリー レポートです。行ごとに並ぶ大量の生データを、数式を一切使わずにコンパクトなマトリックスにまとめられます。どの列を行ラベルとするか、どの列を列ラベルとするか、どの列を集計して値とするかを指定すると、グループ化と計算はピボットテーブルが行います。
- **要約** — 製品別、地域別、または四半期別の合計売上を表示し、長い数式チェーンを使わずに済むようにします。
- **比較** — 行にカテゴリ、列に期間を配置すると、フラットな一覧を、傾向が一目でわかるクロスレポートに変換できます。
- **詳細表示** — 任意の集計値をダブルクリックして、その元にあるソース行を確認できます。
- **更新** — ソースデータが変化した場合、1 回の更新でレポート全体を再計算できます。
代表的な使用シナリオには、売上ダッシュボード、経費内訳、在庫分析などがあり、いずれも「これらの数値をカテゴリと時間別にどのように分解するか」という種類の質問が対象となります。Aspose.Cells for Java を使用すると、同じピボットテーブルをプログラムで作成できます。そのため、アプリケーションが生成するワークブックには、生データだけでなく、すぐに使用できるレポートを含めることができます。

### **Aspose.Cells を使用してピボットテーブルを作成**

{{% alert color="primary" %}}
Aspose.Cells を使用すると、スプレッドシートにピボットテーブルを追加できます。Aspose.Cells には、ピボットテーブルの作成と制御用に用意された特殊なクラスがいくつかあります。これらのクラスは、ピボットテーブルの構成要素となる [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) オブジェクトを作成し、そのプロパティを設定するために使用されます。
ピボットテーブルオブジェクトは次のとおりです。
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): ピボットテーブル内のフィールドを表します。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): ピボットテーブル内のすべての [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) オブジェクトのコレクションを表します。
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): ピボットテーブルを表します。
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): ワークシート上のすべてのピボットテーブルオブジェクトのコレクションを表します。
{{% /alert %}}

### **簡単なピボットテーブルの作成**
ピボットテーブルの作成は、3 つの主要ステップで構成されます。ソースデータをワークシートのセルに書き込み、指定した位置にピボットテーブルを追加して、ピボットフィールドを行領域、列領域、およびデータ領域に配置します。
1. [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) オブジェクトの [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) メソッド（多くの例では `putValue`）を使用して、ワークシートのセルにデータを追加します。このデータはピボットテーブルのデータソースとして使用されます。
2. [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) クラスの [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) メソッドを呼び出して、ワークシートにピボットテーブルを追加します（`add(sourceData, row, column)`）。`sourceData` はソース範囲です（例: "A1:C8"）。`row` と `column` は、ピボットテーブルの左上隅にある配置先セルの 0 ベースの座標です（セル E3 の場合は行 2、列 4）。このメソッドは、新しい [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) オブジェクトを直接返します。
3. [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) オブジェクトの `addFieldToArea` メソッドを使用して、ピボットフィールドを配置します。フィールド名は、行領域 (`PivotFieldType.ROW`)、列領域 (`PivotFieldType.COLUMN`)、またはデータ領域 (`PivotFieldType.DATA`) に指定します。
4. ワークブックを保存します。ピボットテーブルは、保存されたファイルに書き込まれます。
以下のコード例は、上記の手順に従って、簡単なピボットテーブルを作成します。実行すると、ソースデータに基づくピボットテーブルがワークシートに追加されます。
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// 新しいワークブックを作成し、最初のワークシートを取得する
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// ソースデータを書き込む：スポーツ別および四半期別の売上
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// 宛先セル E3 に、A1:C8 をソースとするピボットテーブルを追加する
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// ピボットフィールドを割り当てる：Sport を Rows に、Quarter を Columns に、Sales を Data に
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// ワークブックを保存する
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
セルの範囲をデータソースとして割り当てる場合、範囲は左上隅から右下隅までに設定する必要があります。たとえば、"A1:C3" は有効ですが、"C3:A1" は無効です。
{{% /alert %}}

{{< app/cells/assistant language="java" >}}