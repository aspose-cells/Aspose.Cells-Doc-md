---
title: テーブルおよび範囲
type: docs
weight: 50
url: /ja/net/tables-and-ranges/
---

## **紹介**

Microsoft Excelでテーブルを作成し、その機能を使用せずにテーブルのデータを保持したい場合があります。代わりに、テーブルのように見えるものが欲しい場合があります。フォーマットを失わずにテーブル内のデータを保持するには、テーブルを通常のデータの範囲に変換します。
Aspose.Cellsは、テーブルやリストオブジェクトのMicrosoft Excelのこの機能をサポートしています。

## **Microsoft Excel の使用**

表をフォーマットを保持したまま範囲に素早く変換するには、**範囲に変換** 機能を使用します。Microsoft Excel 2007/2010では:

1. 表内のどこかをクリックして、アクティブなセルが表の列内にあることを確認します。
1. **デザイン** タブの **ツール** グループで、**範囲に変換** をクリックします。

## **Aspose.Cellsの使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRange-1.cs" >}}

{{% alert color="primary" %}}

表を範囲に変換した後は、表の機能は利用できなくなります。たとえば、行ヘッダーにはソートとフィルターの矢印が含まれなくなり、数式で使用されたテーブル名を参照する構造化参照は通常のセル参照に変わります。

{{% /alert %}}

## **オプションで範囲にテーブルを変換**

Aspose.Cellsは、[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) クラスを介してテーブルを範囲に変換する際に追加のオプションを提供します。[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) クラスは、テーブル行の最後のインデックスを設定できる [**LastRow**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions/properties/lastrow) プロパティを提供します。指定した行インデックスまでテーブルの書式設定が保持され、その後の書式設定が削除されます。

以下のサンプルコードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/net/aspose.cells.tables/tabletorangeoptions) クラスの使用例を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Tables-ConvertTableToRangeWithOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
