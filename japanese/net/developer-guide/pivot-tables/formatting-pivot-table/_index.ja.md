---
title: ピボット テーブルの書式設定
type: docs
weight: 10
url: /ja/net/formatting-pivot-table/
---
## **ピボット テーブルの外観**

ピボット テーブルの作成方法では、単純なピボット テーブルの作成方法について説明しています。この記事では、さまざまなプロパティを設定してピボット テーブルの外観をカスタマイズする方法について説明します。

- ピボット テーブル形式のオプション
- ピボット フィールドのフォーマット オプション
- データ フィールド形式のオプション

### **ピボット テーブル形式オプションの設定**

の[**ピボットテーブル**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)クラスはピボット テーブル全体を制御し、さまざまな方法でフォーマットできます。

#### **オートフォーマットの種類の設定**

Microsoft Excel には、あらかじめ設定されたさまざまなレポート形式が用意されています。 Aspose.Cells もこれらの書式設定オプションをサポートしています。それらにアクセスするには:

1. セットする[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat)に**真実**.
1. から書式設定オプションを割り当てます[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)列挙。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **フォーマット オプションの設定**

次のコード サンプルは、ピボット テーブルをフォーマットして行と列の総計を表示する方法と、レポートのフィールドの順序を設定する方法を示しています。また、null 値の顧客文字列を設定する方法も示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **ルック アンド フィールを手動でフォーマットする**

事前設定されたレポート形式を使用する代わりに、ピボット テーブル レポートの外観を手動で書式設定するには、[**ピボットテーブル.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format)と[**ピボットテーブル.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)メソッド。目的のフォーマットのスタイル オブジェクトを作成します。次に例を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **ピボット フィールド形式オプションの設定**

の[**ピボットフィールド**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)クラスはピボット テーブルのフィールドを表し、さまざまな方法でフォーマットできます。以下のコード サンプルは、次の方法を示しています。

- 行フィールドにアクセスします。
- 小計の設定。
- オートソートの設定。
- 自動表示の設定。

#### **行/列/ページ フィールド フォーマットの設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **設定データフィールドのフォーマット**

次のコード サンプルは、データ フィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **ピボット フィールドのクリア**

の[**ピボットフィールド コレクション**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)という名前のメソッドがあります[**クリア（）**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)これにより、ピボット フィールドをクリアできます。ページ、列、行、データなど、領域内のすべてのピボット フィールドをクリアする場合に使用します。
以下のコード サンプルは、データ領域のすべてのピボット フィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
