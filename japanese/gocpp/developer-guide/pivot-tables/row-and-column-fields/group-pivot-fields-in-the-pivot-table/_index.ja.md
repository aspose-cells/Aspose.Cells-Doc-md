---
title: Go via C++ を使用してピボットテーブル内のピボットフィールドをグループ化する
linktitle: Go via C++ を使用してピボットテーブル内のピボットフィールドをグループ化する
description: Aspose.Cells for Go via C++ で PivotField.Group および PivotFieldGroupOptions を使用して、ピボットテーブル内の行および列のピボットフィールドを、月や四半期などの期間および数値範囲にグループ化する方法を学びます。
keywords: Aspose.Cells, Aspose.Cells for Go via C++, ピボットテーブル, ピボットフィールド, ピボットフィールドのグループ化, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, 日付のグループ化, 数値範囲, Go
type: docs
weight: 80
url: /ja/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる利用シナリオ**
- ピボットフィールドのグループ化は、日付が数百件含まれる日付フィールドや、値が多数散在する数値フィールドなど、ピボットテーブルの行または列フィールドに異なる項目が多数含まれている場合に便利です。グループ化によって、これらの項目は意味のある単位にまとめられます。日付は月、四半期、年へ、数値は 0-1、2-3、4-5 などの範囲へまとめられます。これにより、大きなピボットテーブルがコンパクトになり、分析しやすくなります。Aspose.Cells は、`PivotField.Group()` メソッド（データ型による自動グループ化）と `PivotField.Group(PivotFieldGroupOptions)`（カスタムグループ化オプション）を通じてこの機能を提供します。
- 日付のグループ化は、個々の日付を日、月、四半期、年などの大きな単位にまとめ、時間階層（例：年、四半期、月）を作成します。時間の推移が一目でわかり、各期間のレベルがピボットテーブルの行領域または列領域に独自のピボットフィールドとして追加されます。
- グループ化は、ピボットテーブルの行領域または列領域に配置されたフィールドでのみ利用できます。データ（値）フィールドを直接グループ化することはできません。そのフィールドをグループ化するには、まずピボットテーブルの行領域または列領域に追加する必要があります。

## **ピボットフィールドを自動的にグループ化する**
引数なしの `PivotField.Group()` オーバーロードは、フィールドのデータ型を確認して、自動的にグループ化します。日付と空白のみを含むフィールドは、月単位にグループ化されます。数値と空白のみを含むフィールドは、自動的な間隔を使用して数値範囲にグループ化されます。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **カスタムオプションを使用してピボットフィールドをグループ化する**
`PivotFieldGroupOptions` クラスは、カスタムなグループ化設定を提供します。日付フィールドでは `StartDate`、`EndDate`、`GroupTypes` を設定します（日付は Go の `time.Time` 値として渡されます）。数値フィールドでは `StartNumber`、`EndNumber`、`Interval` を設定します。`newPivotField` の動作は、グループ化によって元のフィールドの横に新しいピボットフィールドが作成されるかを制御します（gee article末尾の「注意」セクションを参照してください）。

### **日付フィールドを月と四半期でグループ化する**
次の例では、サンプルピボットテーブルの日付行フィールドを、指定した開始日から終了日までの月および四半期でグループ化します。コードは [サンプル Excel ファイル](sampleGroupPivotFieldsInPivotTable.xlsx) を読み込み、グループ化を適用して、ピボットテーブルのデータを計算し、グループ化した結果を保存します。スクリーンショットで結果を確認できます。日付行フィールドは四半期と月でグループ化されています。
`GroupTypes` 内の値の順序は無視されます。グループタイプを記述した順序にかかわらず、グループ化されたフィールドは常に、期間の大きい方から小さい方へ（年、四半期、月、日、時、分、秒の順）で表示されます。この例では `GroupTypes` で月が四半期より先に指定されていますが、四半期が外側のレベル、月が内側のレベルとして表示されます。

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![月と四半期でグループ化したピボットテーブル](group-pivot-fields-in-the-pivot-table_1.png)

### **数値フィールドを範囲にグループ化する**
サンプルピボットテーブルの `FieldTwo` は、初めはデータ（値）フィールドです。グループ化できるのは行または列フィールドのみであるため、コードはまず `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` を呼び出して `FieldTwo` を行領域に移動し、ピボットテーブルを更新してから、`StartNumber = 0`、`EndNumber = 5`、`Interval = 2` を使用して数値フィールドを 0-1、2-3、4-5 の範囲にグループ化します。

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **注意**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` メソッドのオーバーロードは非推奨で、公開 API から削除されています。`PivotField.Group()` と `PivotField.Group(PivotFieldGroupOptions)` が代替手段となります。
- Microsoft Excel では、数値フィールドをグループ化すると、元のピボットフィールドがグループ化された範囲に置き換えられます。一方、日付フィールドをグループ化すると、元のフィールドの横に新しいピボットフィールド（グループレベルごとに 1 つ、たとえば四半期や月）が作成されます。Aspose.Cells 26.10 以降、`PivotField.Group()` メソッドは Excel と同じ動作に従います。
- `PivotFieldGroupOptions.Interval` プロパティは、数値フィールドのグループ化と、日付を日単位でグループ化する場合（例：日付を 7 日単位にグループ化する場合）にのみ適用されます。日付を月、四半期、または年単位でグループ化する場合は無視されます。
{{% /alert %}}

## **関連記事**
- [ピボットテーブルで上位 10 件を表示またはフィルターする](/cells/ja/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [ピボットテーブルで値を表示する形式を設定する](/cells/ja/go-cpp/show-values-as-in-pivot-table/)
- [ピボットテーブルの一部に書式を適用する](/cells/ja/go-cpp/format-part-of-pivot-table/)
- [ピボットテーブルに条件付き書式を追加する](/cells/ja/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}