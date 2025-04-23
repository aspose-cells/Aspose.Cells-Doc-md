---
title: Excelのテーブルをデータの範囲に変換する
type: docs
weight: 10
url: /ja/java/convert-an-excel-table-to-a-range-of-data/
---

{{% alert color="primary" %}}

Microsoft Excelでテーブルを作成し、その機能を使用せずにテーブルのデータを保持したい場合があります。代わりに、テーブルのように見えるものが欲しい場合があります。フォーマットを失わずにテーブル内のデータを保持するには、テーブルを通常のデータの範囲に変換します。

Aspose.CellsはテーブルとリストオブジェクトのMicrosoft Excelのこの機能をサポートしています。

{{% /alert %}}

## **Microsoft Excel の使用**

表をフォーマットを保持したまま範囲に素早く変換するには、**範囲に変換** 機能を使用します。Microsoft Excel 2007/2010では:

1. 表内のどこかをクリックして、アクティブなセルが表の列内にあることを確認します。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_1.gif)

1. **デザイン** タブの **ツール** グループで、**範囲に変換** をクリックします。

![todo:image_alt_text](convert-an-excel-table-to-a-range-of-data_2.gif)

{{% alert color="primary" %}}

表を範囲に変換した後は、表の機能は利用できなくなります。たとえば、行ヘッダーにはソートとフィルターの矢印が含まれなくなり、数式で使用されたテーブル名を参照する構造化参照は通常のセル参照に変わります。

{{% /alert %}}

## **Aspose.Cellsの使用**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-ConvertTableToRange-ConvertTableToRange.java" >}}

## **オプションで範囲にテーブルを変換**

Aspose.Cellsは[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)クラスを介してテーブルを範囲に変換する際に追加のオプションを提供します。[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions)クラスは[**LastRow**](https://reference.aspose.com/cells/java/com.aspose.cells/tabletorangeoptions#LastRow)プロパティを提供し、テーブル行の最後のインデックスを設定できます。指定された行インデックスまでテーブルの書式が保持され、その後の書式は削除されます。

以下のサンプルコードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TableToRangeOptions) クラスの使用例を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Tables-ConvertTableToRangeWithOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
