---
title: セル参照に基づいて画像を挿入する
type: docs
weight: 150
url: /ja/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

時々、空の画像があり、Formula Barでセル参照を設定して画像内のデータや内容を表示する必要があります。 Aspose.Cellsはこの機能（Microsoft Excel 2010）をサポートしています。

{{% /alert %}}

## セル参照に基づいて画像を挿入する

Aspose.Cellsは、ワークシートのセルの内容を画像形状で表示する機能をサポートしています。指定のセルまたはセル範囲をリンクして、データを表示したい画像に紐付けることができます。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトにも反映されます。[**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)メソッドを呼び出してワークシートに画像を追加します。このメソッドは[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)コレクションの[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトでカプセル化されています。[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)属性を使用してセル範囲を指定します。この属性は[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトのものです。

### コード例

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
