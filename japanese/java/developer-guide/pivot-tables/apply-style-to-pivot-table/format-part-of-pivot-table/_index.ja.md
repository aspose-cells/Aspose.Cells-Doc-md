---
title: ピボットテーブルの一部をフォーマットする
linktitle: ピボットテーブルの一部をフォーマットする
description: Aspose.Cells for Java を使用して、PivotTable.format により意味的な PivotArea 領域または CellArea 四角形にスタイルを適用し、PivotTable.getPivotFormats に保存された書式設定をピボットテーブルが更新されても保持します。
keywords: Aspose.Cells for Java, ピボットテーブル, フォーマット, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /ja/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
`PivotTable.formatAll` はピボットテーブル全体に単一のスタイルを適用し、親ページで説明されています。ラベル、値、合計、またはレポートの特定領域を区別しません。実務では、ピボットテーブルの一部だけを目立たせることが一般的です。対象としては、特定の行フィールドに属するラベル、あるフィールドによって生成された値セル、総計行、または最初の 2 行のような任意の四角形が挙げられます。ピボットテーブルのワークシートセルに直接スタイルを適用することは同等ではありません。Excel はピボットテーブルの書式設定を普通のセルスタイルレコードではなく、意味的な `PivotArea` 領域として保存します。`PivotArea` の書式設定はフィールドのラベルやデータ値などの領域に結び付けられ、ピボットテーブルが再計算、更新、拡張されると再解決されます。一方、セルに直接書き込んだスタイルはそのセル位置に属し、ピボットモデルによって追跡されません。Aspose.Cells は完全な `PivotTable.format` オーバーロード族を提供しており、両方の書式設定方法が利用可能です。
- `format(PivotArea, Style)` は `PivotArea.select` または `PivotArea.selectField` で構築した意味的領域にスタイルを固定します。
- `format(CellArea, Style)` はピボットテーブル内のワークシート四角形にスタイルを固定します。
- `format(int row, int column, Style)` は単一セルを対象とします。
- `formatAll(Style)` はピボットテーブル全体を書式設定します。

## **PivotArea の書式設定**
フィールドやレポート領域にハイライトを付け続けたい場合は、意味領域のワークフローが推奨されます。
1. `new PivotArea(pivotTable)` で `PivotArea` を作成します。このオブジェクトは対象ピボットテーブルに属する意味的領域を表します。
2. `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` で、指定軸上のゼロベース位置にあるフィールドを選択します。  
   - `PivotTableSelectionType.DATA_AND_LABEL` はラベルとデータの両方を選択します。  
   - `PivotTableSelectionType.LABEL_ONLY` はフィールドのラベルのみを選択します。  
   - `PivotTableSelectionType.DATA_ONLY` はフィールドのデータセルのみを選択します。
3. `PivotArea.selectField(PivotFieldType axisType, String fieldName)` で名前によりフィールドを選択します。行フィールドを名前で選択した場合、その領域はフィールド項目が生成する値セルに解決されます。
4. `Workbook.createStyle()` で `Style` を作成し、フォント、前景色、単色背景パターンを設定し、`PivotTable.format(area, style)` に渡します。
5. `PivotArea` のオーバーロードを呼び出すたびに、`PivotTable.getPivotFormats()` に `PivotTableFormat` エントリが 1 つ追加されます。
6. フィールドに紐付いた書式はピボットデータが計算される際に描画されます。そのため、書式を適用した後に `PivotTable.calculateData()` を呼び出し、スタイルが表示されるようにします。  
以下の例では、フルーツ販売の小規模ピボットテーブルを作成し、`Fruit` 行ラベルを `PivotArea.select` と `PivotTableSelectionType.LABEL_ONLY` で、同じ行フィールドが生成する値セルを `PivotArea.selectField` でスタイル設定し、最後にピボットテーブルを再計算して両方のスタイルを描画します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
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
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **ピボットテーブルの CellArea の書式設定**
対象領域が意味的ピボット領域ではなく、単純なワークシート四角形である場合は `PivotTable.format(CellArea, Style)` を使用します。`CellArea` は `getStartRow()`, `getStartColumn()`, `getEndRow()`, `getEndColumn()` プロパティで記述され、値はゼロベースのワークシート座標です。終了座標は四角形に含まれる最後の行と列を示すため、開始位置から終了位置までのセルがすべて対象になります。フィールドに紐付いた書式とは異なり、`CellArea` の書式設定は即座にセルに適用され、スタイルを表示させるために `calculateData()` を再度呼び出す必要はありません。`CellArea` 四角形はラベルセルと値セルを同時に含むことができます。次の節では、Aspose.Cells と Excel がその四角形を内部的にどのように表現しているかを説明します。以下の例では、ピボットテーブルの矩形 `E4:F5` をイタリック体の薄青スタイルで書式設定し、再計算なしでワークブックを保存します。

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **PivotArea と CellArea のマッピング**
Excel はピボットテーブルの書式設定を普通のワークシートセルスタイルレコードではなく `pivotArea` レコードとして保存します。Aspose.Cells でも同じモデルが使用されており、書式設定要求は記録時にピボット領域に変換されます。ユーザーが指定した `CellArea` と内部で保持されるピボット領域との関係は、多対多の双方向です。
- 1 つの `CellArea` が複数のピボット領域を生成することがあります。四角形がラベルセルと値セルの両方を跨ぐ場合、ラベル用とデータ用に別々のルールに分割されます。ピボットモデルはラベル書式とデータ書式を独立して扱うためです。
- 1 つのピボット領域が複数の分離した `CellArea` インスタンスに解決されることがあります。総計行や項目が連続していないフィールドなど、意味的領域が複数の矩形にまたがる場合です。そのため `PivotArea.getCellAreas()` は単一の四角形ではなくコレクションを返します。  
`PivotTable.format` を通じて行われたすべての書式操作は `PivotTable.getPivotFormats()` に記録されます。各 `PivotTableFormat` エントリは関連付けられた `PivotArea` と適用された `Style` を公開します。`PivotArea` のオーバーロードは呼び出しごとにちょうど 1 つのエントリを追加しますが、異なる意味領域を含む `CellArea` は複数のエントリを追加する可能性があります。保存された領域を区別するために、各 `PivotArea` は `getOnlyLabel()` と `getOnlyData()` フラグを公開します。以下の例はラベルと値の両方をカバーする単一矩形を書式設定し、`PivotTable.getPivotFormats()` を検査して、各保存されたピボット領域が解決する `CellArea` 座標を表示します。

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
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
書式がピボット領域として保存されるため、普通のセルスタイルとしてではなく、再計算や更新、保存後の再読み込み時にも保持されます。ピボットテーブルが `PivotTable.refreshData` で更新されたり、`calculateData` で再計算されたり、保存後に再ロードされたりすると、すべての保存されたピボット領域が現在の位置に再解決され、スタイルが再適用されます。
{{% /alert %}}

ハイライトをフィールドや意味的領域に付け続けたい場合は `select` または `selectField` で構築した `PivotArea` を使用し、固定された矩形を書式設定したい場合は `CellArea` を使用します。単一セルを対象にしたいときは `format(int row, int column, Style)` を、ピボットテーブル全体を一括で再スタイル化したいときは親ページで説明されている `formatAll` を使用してください。

## **関連記事**
- [ピボットテーブルへのスタイル適用](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルの行および列フィールドの追加](/cells/ja/java/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルの値フィールドの管理](/cells/ja/java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}