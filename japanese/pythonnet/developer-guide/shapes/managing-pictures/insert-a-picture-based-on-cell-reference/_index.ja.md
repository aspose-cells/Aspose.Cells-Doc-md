---
title: セル参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

時には、空の画像があり、その画像にセル参照を設定してデータや内容を表示したい場合があります。Aspose.Cells for Python via .NETはこの機能をサポートしています（Microsoft Excel 2010対応）。

{{% /alert %}}

## セル参照に基づいて画像を挿入する

Aspose.Cells for Python via .NETは、ワークシートのセルの内容を画像の形に表示できる機能をサポートしています。画像を表示したいセルのデータを含むセルとリンクさせることができます。セルやセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、その変更が自動的にグラフィックオブジェクトに反映されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)のメソッド([**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)コレクションを[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)オブジェクトにカプセル化)を呼び出して、ワークシートに画像を追加します。セル範囲は[**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula)属性で指定します。

### コード例

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
