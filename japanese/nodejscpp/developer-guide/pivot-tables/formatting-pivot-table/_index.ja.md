---
title: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/nodejs-cpp/formatting-pivot-table/
description: Aspose.Cells for Node.js via C++を使ったピボットテーブルのフォーマット方法
keywords: ピボットテーブルのフォーマット。
---

## **ピボットテーブルの外観**

ピボットテーブルの外観をカスタマイズする方法については、「ピボットテーブルの作成」でシンプルなピボットテーブルの作成方法が説明されています。この記事では、さまざまなプロパティを設定してピボットテーブルの外観をカスタマイズする方法について説明します:

- ピボットテーブルの書式オプション
- ピボットフィールドの書式オプション
- データフィールドの書式オプション

### **ピボットテーブルフォーマットオプションの設定方法**

[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/) クラスは、全体のピボットテーブルを制御し、さまざまな方法で書式設定できます。

#### **自動フォーマットタイプの設定方法**

Microsoft Excelはさまざまなプリセットレポートフォーマットを提供しています。Aspose.Cells for Node.js via C++もこれらのフォーマットオプションをサポートしています。アクセス方法は次の通り：

1. [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) を **true** に設定します。
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/) 列挙型から書式設定オプションを割り当てます。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **フォーマットオプションの設定方法**

以下のコードサンプルは、ピボットテーブルを書式設定して行と列の合計を表示する方法、およびレポートのフィールド順序を設定する方法を示しています。また、null 値にカスタム文字列を設定する方法も示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **見た目と手触りの書式設定**

事前設定されたレポート形式を使用せずに、ピボットテーブルレポートの外観を手動でフォーマットする場合、[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) メソッドと [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) メソッドを使用します。所望のフォーマットのためのスタイルオブジェクトを作成します。たとえば：

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **ピボットフィールドのフォーマットオプションの設定方法**

[**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/) クラスは、ピボットテーブルのフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次のように行います:

- 行フィールドへのアクセス。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

#### **行/列/ページフィールドのフォーマット設定方法**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **データフィールドのフォーマット設定方法**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **ピボットフィールドをクリアする方法**

[**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) には、ピボットフィールドをクリアするための [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) メソッドがあります。たとえば、ページ、列、行、またはデータなど、領域内のすべてのピボットフィールドをクリアしたい場合に使用します。
以下のコードサンプルは、データ領域内のすべてのピボットフィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
