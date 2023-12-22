---
title: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/net/formatting-pivot-table/
description: Aspose.Cells for Python via .NET でピボット テーブルを書式設定する方法。
keywords: Format pivot table.
---
##  **ピボットテーブルの外観**

ピボット テーブルの作成方法では、簡単なピボット テーブルを作成する方法について説明します。この記事では、さまざまなプロパティを設定してピボット テーブルの外観をカスタマイズする方法について説明します。

- ピボットテーブル形式のオプション
- ピボットフィールドの形式オプション
- データフィールド形式のオプション

###  **ピボットテーブル形式オプションの設定**

の[**ピボットテーブル**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)クラスはピボット テーブル全体を制御し、さまざまな方法でフォーマットできます。

####  **オートフォーマットタイプの設定**

Microsoft Excel には、さまざまな事前設定されたレポート形式が用意されています。 Aspose.Cells for Python via .NET は、これらの書式設定オプションもサポートしています。アクセスするには:

1. セット[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)*本当**に。
1. から書式設定オプションを割り当てます。[**ピボットテーブルのオートフォーマットの種類**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)列挙。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **フォーマットオプションの設定**

以下のコード サンプルは、行と列の総計を表示するためにピボット テーブルを書式設定する方法と、レポートのフィールド順序を設定する方法を示しています。また、顧客文字列を NULL 値に設定する方法も示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **ルック アンド フィールを手動で書式設定する**

ピボット テーブル レポートの外観を手動で書式設定するには、事前設定されたレポート形式を使用する代わりに、[**PivotTable.format_all(スタイル)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/)そして[**PivotTable.format(行、列、スタイル)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)メソッド。希望する書式設定のスタイル オブジェクトを作成します。次に例を示します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **ピボットフィールド形式オプションの設定**

の[**ピボットフィールド**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)クラスはピボット テーブル内のフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次の方法を示しています。

- 行フィールドにアクセスします。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

####  **行/列/ページフィールドの形式の設定**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **データフィールド形式の設定**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **ピボットフィールドのクリア**

の[**ピボットフィールドコレクション**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/)という名前のメソッドがあります[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)これにより、ピボット フィールドをクリアできるようになります。ページ、列、行、データなどの領域内のすべてのピボット フィールドをクリアする場合に使用します。
以下のコード サンプルは、データ領域内のすべてのピボット フィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
