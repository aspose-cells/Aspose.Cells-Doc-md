---
title: Golang経由でC++を使ったピボットテーブルのフォーマット
linktitle: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/go-cpp/formatting-pivot-table/
description: Aspose.Cells for C++を使用したピボットテーブルの表示カスタマイズ方法を学習します。
---

## **ピボットテーブルの外観**

ピボットテーブルの外観をカスタマイズする方法については、「ピボットテーブルの作成」でシンプルなピボットテーブルの作成方法が説明されています。この記事では、さまざまなプロパティを設定してピボットテーブルの外観をカスタマイズする方法について説明します:

- ピボットテーブルの書式オプション
- ピボットフィールドの書式オプション
- データフィールドの書式オプション

### **ピボットテーブルの書式オプションの設定**

[**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/) クラスは、全体のピボットテーブルを制御し、さまざまな方法で書式設定できます。

#### **AutoFormat タイプの設定**

Microsoft Excel にはさまざまなプリセットレポート形式があります。Aspose.Cells もこれらの書式設定をサポートしています。アクセス方法は次のとおりです：

1. [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) を **true** に設定します。
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/) 列挙型から書式設定オプションを割り当てます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **書式オプションの設定**

以下のコード例は、行と列の合計を表示し、レポートのフィールド順序を設定し、null値に対するカスタム文字列を設定する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **見た目と手触りの書式設定**

プリズマトレイのレポートの見た目を手動で整形するには、事前設定されたレポート形式を使用する代わりに [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) と [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) メソッドを使用します。あなたが望む書式設定用のスタイルオブジェクトを作成してください：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **ピボットフィールドの書式オプションの設定**

[**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/) クラスは、ピボットテーブルのフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次のように行います:

- 行フィールドへのアクセス。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

#### **行/列/ページフィールドの書式の設定**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **データフィールドのフォーマットを設定する**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **ピボットフィールドのクリア**

[**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) には、ピボットフィールドをクリアするための [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) メソッドがあります。たとえば、ページ、列、行、またはデータなど、領域内のすべてのピボットフィールドをクリアしたい場合に使用します。
以下のコードサンプルは、データ領域内のすべてのピボットフィールドをクリアする方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
