---
title: Excel テーブルをデータ範囲に変換する
type: docs
weight: 10
url: /ja/java/convert-an-excel-table-to-a-range-of-data/
---
{{% alert color="primary" %}}

場合によっては、Microsoft Excel でテーブルを作成し、付属のテーブル機能を使い続けたくないことがあります。代わりに、テーブルのようなものが必要です。書式設定を失わずにテーブル内のデータを保持するには、テーブルを通常のデータ範囲に変換します。

Aspose.Cells は、Microsoft Excel のテーブルおよびリスト オブジェクトのこの機能をサポートしています。

{{% /alert %}}

## **Microsoft エクセルを使う**

使用**範囲に変換**書式設定を失うことなくテーブルを範囲にすばやく変換する機能。 Microsoft Excel 2007/2010:

1. テーブル内の任意の場所をクリックして、アクティブ セルがテーブルの列にあることを確認します。

![todo:画像_代替_文章](convert-an-excel-table-to-a-range-of-data_1.gif)

1. 上で**デザイン**タブの**ツール**グループ、クリック**範囲に変換**.

![todo:画像_代替_文章](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

テーブルが範囲に変換されると、テーブルの機能は使用できなくなります。たとえば、行ヘッダーには並べ替え矢印とフィルター矢印が含まれなくなり、数式で使用されていた構造化参照 (テーブル名を使用する参照) は通常のセル参照に変わります。

{{% /alert %}}

## **Aspose.Cells を使用**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **オプションを使用してテーブルを範囲に変換する**

Aspose.Cells は、[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)クラス。の[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)クラスが提供する[**最後の行**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)テーブル行の最後のインデックスを設定できるプロパティ。テーブルの書式設定は、指定された行インデックスまで保持され、残りの書式設定は削除されます。

以下のサンプル コードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)クラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
