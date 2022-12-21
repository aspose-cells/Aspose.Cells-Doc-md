---
title: Cell 参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

空白の画像があり、数式バーでセル参照を設定して画像にデータやコンテンツを表示する必要がある場合があります。 Aspose.Cells はこの機能をサポートしています (Microsoft Excel 2010)。

{{% /alert %}}

## Cell 参照に基づく画像の挿入

Aspose.Cells は、ワークシート セルの内容を画像の形で表示することをサポートします。表示するデータを含むセルに画像をリンクできます。セルまたはセル範囲はグラフィック オブジェクトにリンクされているため、そのセルまたはセル範囲のデータに加えた変更は、グラフィック オブジェクトに自動的に反映されます。を呼び出して、ワークシートに画像を追加します。[**画像を追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)の方法[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体）。を使用してセル範囲を指定します。[**方式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)の属性[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。

### コード例

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
