---
title: ピボットテーブルに条件付き書式を追加する
linktitle: ピボットテーブルに条件付き書式を追加する
description: Aspose.Cells for Java でピボットテーブルに条件付き書式を追加します - applyTo と PivotConditionFormatScopeType スコープでデータ領域にルールをアンカーするか、addCellArea と getPivotAreas で対象を定義し、次に FormatConditions.addCondition を使用してルールとスタイルを付与します。
keywords: Aspose.Cells for Java, ピボットテーブル, 条件付き書式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /ja/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
親ページおよび兄弟ページで説明されているスタイルは静的です。`PivotArea` または `CellArea` 領域は一度塗りつぶされ、値がどう変わってもそのスタイルが保持されます。条件付き書式はルール駆動型の対応物であり、200 を超える金額をハイライトしたり、中央値の 50% をシェードしたり、下位ランクの項目にフラグを付けたりします。ハイライトはピボットテーブルが再計算または再更新されるたびに値に合わせて変化します。  
Aspose.Cells では、ピボットテーブルの条件付き書式は `PivotTable.getConditionalFormats()` コレクションに格納されます。各エントリは `PivotConditionalFormat` で、次の 2 つの質問に独立して答えます。
- **ルールはどこに適用されますか？** 対象領域は `applyTo(int row, int column, PivotConditionFormatScopeType scope)` で指定する方法（Excel の UI のスコープ選択に相当）または `addCellArea(CellArea)` と `getPivotAreas()` コレクションで明示的に領域名を付ける方法があります。
- **ルールは何をテストしますか？** `getFormatConditions()` に対して `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` で 1 つ以上の条件を追加し、各条件に独自の `Style` を付与します。

{{% alert color="primary" %}}
`PivotConditionalFormat` の `getFormatConditions()` コレクションに対して `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` または `FormatConditionCollection.addArea(CellArea)` を呼び出さないでください。これら 2 つのオーバーロードは通常のワークシート条件付き書式 API から継承されたもので、ピボットテーブルでは機能しません。セル領域はピボット領域に変換されず、要求は黙って無視されます。必ず `PivotConditionalFormat` 自体で領域を定義（`applyTo`、`addCellArea`、または `getPivotAreas()`）し、`addCondition` のいずれかのオーバーロードでルールを追加してください。
{{% /alert %}}

## **スコープでルールを適用する（Excel UI の方法）**
最初の方法は、Excel ユーザーインターフェイスと同じ方法でルールを配置します。ピボットテーブルのセルは 0 ベースのワークシート座標で名前付けされ、`PivotConditionFormatScopeType` スコープが Aspose.Cells に対してそのセルからどれだけの範囲にルールを適用するかを指示します：
- `PivotConditionFormatScopeType.DATA` - ピボットテーブルが生成するすべての値セル（合計行を含む）。
- `PivotConditionFormatScopeType.FIELD` - セルが識別するフィールドに属する値セル（合計行は除外）。セルは行フィールドラベルなどのフィールドセルである必要があり、値セルを渡すと例外がスローされます。
- `PivotConditionFormatScopeType.SELECTION` - セルが選択する交差点の値セルのみで、通常は単一の値セルです。
以下の例では、E3 を左上隅としたフルーツ販売のピボットテーブルを作成し、`DATA` スコープでセル F4（行 3、列 5）に条件付き書式をアンカーし、200 を超える金額を赤色の背景に白文字の太字でハイライトします。Apple が 220、Banana が 330、Cherry が 200、合計が 750 の場合、ルールは F4、F5、F7 に適用され、解決された領域はデータ列全体の F4:F7 となり、条件を満たすセルだけがハイライトされます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Anchor the conditional format at F4 (row 3, column 5) with the Data scope
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Rule - highlight amounts greater than 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

同じルールを行フィールドラベル E4（行 3、列 4）に `FIELD` スコープでアンカーすると、解決された領域は F4:F6 になります。これは合計行を除いた同じデータ列になるためです。`SELECTION` スコープを F4 にアンカーした場合は、解決領域は F4 のみとなります。

## **領域を手動で定義する**
スコープ選択を省略し、`PivotConditionalFormat` に対して領域を明示的に名前付けする第 2 の方法です。

### **addCellArea を使用したワークシートの矩形**
`addCellArea(CellArea)` は、指定された矩形をルールの対象として記録します。座標は 0 ベースのワークシート座標であり、領域は提供された矩形そのものです。データ列への拡張や合計行のロジックはありません。現在のピボットレイアウトで対象セルが既知の固定矩形である場合に使用してください。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **getPivotAreas を使用した意味的なピボット領域**
`getPivotAreas()` は、兄弟ページで静的スタイルに使用されているのと同じ意味的領域モデルを返します。`PivotArea` を作成し、`select` または `selectField` でフィールドや領域を選択し、`getPivotAreas().addPivotArea(PivotArea)` で追加します。意味的領域はフィールドに紐付いているため、ピボットテーブルが再更新されレイアウトが変わっても条件付き書式はそのフィールドに追随します。`getPivotAreas().add(PivotArea)` のオーバーロードはまだコンパイルできますが、非推奨とマークされているため `addPivotArea` を使用してください。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **ルールの保存場所と再読み込み後の持続性**
`getConditionalFormats().add()` 呼び出しは、ピボットテーブルに 1 つの `PivotConditionalFormat` を追加します。条件、数式、スタイルはワークブックに保存されます。下の例でファイルを再度開くと、同じルールがタイプ、演算子、数式が保持されたまま表示され、`getCellAreas()` も同じ領域を報告します。条件がまったく設定されていないエントリは、ワークブックが保存される際に削除されます。これは Excel がルールのない条件付き書式を破棄するのと同じ動作です。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// This prints:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **関連項目**
- [ピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルの一部をフォーマットする](/cells/ja/java/format-part-of-pivot-table/)
- [ピボットテーブルで上位10件の表示またはフィルタリング](/cells/ja/java/top-10-show-or-filter-in-pivot-table/)
- [ラベルまたは値でピボットテーブルをフィルタリング](/cells/ja/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}