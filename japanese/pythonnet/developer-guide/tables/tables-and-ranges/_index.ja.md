---
title: テーブルおよび範囲
type: docs
weight: 50
url: /ja/python-net/tables-and-ranges/
---

## **紹介**

Microsoft Excelでテーブルを作成し、その機能を使用せずにテーブルのデータを保持したい場合があります。代わりに、テーブルのように見えるものが欲しい場合があります。フォーマットを失わずにテーブル内のデータを保持するには、テーブルを通常のデータの範囲に変換します。
Aspose.Cells for Python via .NETは、このMicrosoft Excelのテーブルとリストオブジェクトの機能をサポートしています。

## **Microsoft Excel の使用**

表をフォーマットを保持したまま範囲に素早く変換するには、**範囲に変換** 機能を使用します。Microsoft Excel 2007/2010では:

1. 表内のどこかをクリックして、アクティブなセルが表の列内にあることを確認します。
1. **デザイン** タブの **ツール** グループで、**範囲に変換** をクリックします。

## **Aspose.Cells for Python via .NETを使用して**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRange-1.py" >}}

{{% alert color="primary" %}}

表を範囲に変換した後は、表の機能は利用できなくなります。たとえば、行ヘッダーにはソートとフィルターの矢印が含まれなくなり、数式で使用されたテーブル名を参照する構造化参照は通常のセル参照に変わります。

{{% /alert %}}

## **オプションで範囲にテーブルを変換**

Aspose.Cells for Python via .NETは、[**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions)クラスを通じてテーブルを範囲に変換する際の追加オプションを提供します。[**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions)クラスは[**last_row**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions/last_row/)プロパティを提供し、これを使用してテーブルの最後の行インデックスを設定できます。指定された行インデックスまでテーブルのフォーマットが維持され、それ以降のフォーマットは削除されます。

以下のサンプルコードは、[**TableToRangeOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/tabletorangeoptions) クラスの使用例を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-ConvertTableToRangeWithOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
