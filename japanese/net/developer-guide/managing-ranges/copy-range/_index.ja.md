---
title: Excelの範囲をコピーする
linktitle: 範囲をコピー
type: docs
weight: 105
url: /ja/net/copy-ranges-of-Excel/
---
## **序章**

Excel では、範囲を選択して範囲をコピーし、特定のオプションを指定して同じワークシート、他のワークシート、または他のファイルに貼り付けることができます。

## **Aspose.Cells を使用して範囲をコピーする**

Aspose.Cells はオーバーロードを提供します[範囲.コピー](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy)範囲をコピーするメソッド。
と[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/)範囲のコピー スタイルのみ。[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/)範囲のコピー値のみ

## **コピー範囲**

ソース範囲とターゲット範囲の 2 つの範囲を作成し、Range.Copy メソッドを使用してソース範囲をターゲット範囲にコピーします。

次のコードを参照してください。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **オプションで範囲を貼り付け**

Aspose.Cells は、特定のタイプの範囲の貼り付けをサポートしています。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **範囲のデータのみをコピーします。**
また、Range.CopyData メソッドを次のコードとして使用してデータをコピーすることもできます。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **先行トピック**
- [ソース範囲の行の高さをコピー先範囲にコピー](/cells/ja/net/copy-row-heights-of-source-range-to-destination-range/)


