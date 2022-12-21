---
title: テーブルと範囲
type: docs
weight: 50
url: /ja/net/tables-and-ranges/
---
## **序章**

場合によっては、Microsoft Excel でテーブルを作成し、付属のテーブル機能を使い続けたくないことがあります。代わりに、テーブルのようなものが必要です。書式設定を失わずにテーブル内のデータを保持するには、テーブルを通常のデータ範囲に変換します。
Aspose.Cells は、Microsoft Excel のテーブルおよびリスト オブジェクトのこの機能をサポートしています。

## **Microsoft エクセルを使う**

使用**範囲に変換**書式設定を失うことなくテーブルを範囲にすばやく変換する機能。 Microsoft Excel 2007/2010:

1. テーブル内の任意の場所をクリックして、アクティブ セルがテーブルの列にあることを確認します。
1. 上で**デザイン**タブの**ツール**グループ、クリック**範囲に変換**.

## **Aspose.Cells を使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

テーブルが範囲に変換されると、テーブルの機能は使用できなくなります。たとえば、行ヘッダーには並べ替え矢印とフィルター矢印が含まれなくなり、数式で使用されていた構造化参照 (テーブル名を使用する参照) は通常のセル参照に変わります。

{{% /alert %}}

## **オプションを使用してテーブルを範囲に変換する**

Aspose.Cells は、[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)クラス。の[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)クラスが提供する[**最後の行**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow)テーブル行の最後のインデックスを設定できるプロパティ。テーブルの書式設定は、指定された行インデックスまで保持され、残りの書式設定は削除されます。

以下のサンプル コードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions)クラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
