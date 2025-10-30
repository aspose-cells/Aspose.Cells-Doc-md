---
title: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/python-net/formatting-pivot-table/
description: Aspose.Cells for Python via .NETでピボットテーブルの書式設定方法
keywords: ピボットテーブルのフォーマット。
---

## **ピボットテーブルの外観**

ピボットテーブルの外観をカスタマイズする方法については、「ピボットテーブルの作成」でシンプルなピボットテーブルの作成方法が説明されています。この記事では、さまざまなプロパティを設定してピボットテーブルの外観をカスタマイズする方法について説明します:

- ピボットテーブルの書式オプション
- ピボットフィールドの書式オプション
- データフィールドの書式オプション

### **ピボットテーブルフォーマットオプションの設定方法**

[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) クラスは、全体のピボットテーブルを制御し、さまざまな方法で書式設定できます。

#### **自動フォーマットタイプの設定方法**

Microsoft Excelにはさまざまなプリセットのレポートフォーマットがあります。Aspose.Cells for Python via .NETもこれらの書式設定オプションをサポートしています。アクセスするためには:

1. [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) を **true** に設定します。
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/) 列挙型から書式設定オプションを割り当てます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **フォーマットオプションの設定方法**

以下のコードサンプルは、ピボットテーブルを書式設定して行と列の合計を表示する方法、およびレポートのフィールド順序を設定する方法を示しています。また、null 値にカスタム文字列を設定する方法も示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **見た目と手触りの書式設定**

事前設定されたレポート形式を使用せずに、ピボットテーブルレポートの外観を手動でフォーマットする場合、[**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) メソッドと [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/) メソッドを使用します。所望のフォーマットのためのスタイルオブジェクトを作成します。たとえば：

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **ピボットフィールドのフォーマットオプションの設定方法**

[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) クラスは、ピボットテーブルのフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次のように行います:

- 行フィールドへのアクセス。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

#### **行/列/ページフィールドのフォーマット設定方法**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **データフィールドのフォーマット設定方法**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **ピボットフィールドをクリアする方法**

[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) には、ピボットフィールドをクリアするための [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) メソッドがあります。たとえば、ページ、列、行、またはデータなど、領域内のすべてのピボットフィールドをクリアしたい場合に使用します。
以下のコードサンプルは、データ領域内のすべてのピボットフィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
