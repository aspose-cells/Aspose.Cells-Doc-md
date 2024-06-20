---
title: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/net/formatting-pivot-table/
---

## **ピボットテーブルの外観**

ピボットテーブルの外観をカスタマイズする方法については、「ピボットテーブルの作成」でシンプルなピボットテーブルの作成方法が説明されています。この記事では、さまざまなプロパティを設定してピボットテーブルの外観をカスタマイズする方法について説明します:

- ピボットテーブルの書式オプション
- ピボットフィールドの書式オプション
- データフィールドの書式オプション

### **ピボットテーブルの書式オプションの設定**

[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) クラスは、全体のピボットテーブルを制御し、さまざまな方法で書式設定できます。

#### **AutoFormat タイプの設定**

Microsoft Excel はさまざまなプリセットレポート形式を提供しています。Aspose.Cells もこれらの書式オプションをサポートしています。これらにアクセスするには:

1. [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) を **true** に設定します。
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype) 列挙型から書式設定オプションを割り当てます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **書式オプションの設定**

以下のコードサンプルは、ピボットテーブルを書式設定して行と列の合計を表示する方法、およびレポートのフィールド順序を設定する方法を示しています。また、null 値にカスタム文字列を設定する方法も示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **見た目と手触りの書式設定**

事前設定されたレポート形式を使用せずに、ピボットテーブルレポートの見た目を手動で書式設定するには、[**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) と [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall) メソッドを使用します。必要な書式設定のスタイルオブジェクトを作成します。たとえば:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **ピボットフィールドの書式オプションの設定**

[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) クラスは、ピボットテーブルのフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次のように行います:

- 行フィールドへのアクセス。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

#### **行/列/ページフィールドの書式の設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **データフィールドの書式の設定**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **ピボットフィールドのクリア**

[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) には、ピボットフィールドをクリアするための [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) メソッドがあります。たとえば、ページ、列、行、またはデータなど、領域内のすべてのピボットフィールドをクリアしたい場合に使用します。
以下のコードサンプルは、データ領域内のすべてのピボットフィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
