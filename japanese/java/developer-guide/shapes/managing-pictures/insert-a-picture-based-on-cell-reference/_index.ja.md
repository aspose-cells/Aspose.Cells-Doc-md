---
title: Cell 参照に基づいて画像を挿入する
type: docs
weight: 90
url: /ja/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

空白の画像があり、数式バーでセル参照を設定して画像にデータやコンテンツを表示する必要がある場合があります。 Aspose.Cells はこの機能をサポートしています (Microsoft Excel 2010)。

{{% /alert %}}

## Cell 参照に基づく画像の挿入

Aspose.Cells は、ワークシート セルの内容を画像の形で表示することをサポートします。表示するデータを含むセルに画像をリンクできます。セルまたはセル範囲がグラフィック オブジェクトにリンクされているため、データへの変更は自動的にグラフィック オブジェクトに表示されます。を呼び出して、ワークシートに画像を追加します。[**画像を追加**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) の方法[**シェイプコレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)物体）。を使用してセル範囲を指定します。[**set式**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)の方法[**写真**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)物体。

以下は、以下のコードが生成するファイルのスクリーンショットです。

**セル参照に基づく画像の挿入**

![todo:画像_代替_文章](insert-a-picture-based-on-cell-reference_1.png)

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
