---
title: セル参照に基づいて画像を挿入する
type: docs
weight: 90
url: /ja/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

時々、空の画像があり、Formula Barでセル参照を設定して画像内のデータや内容を表示する必要があります。 Aspose.Cellsはこの機能（Microsoft Excel 2010）をサポートしています。

{{% /alert %}}

## セル参照に基づいて画像を挿入する

Aspose.Cellsはワークシートセルの内容を画像形状で表示することをサポートしています。表示したいデータを含むセルに画像をリンクすることができます。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、データの変更が自動的にグラフィックオブジェクトに反映されます。ワークシートに画像を追加するには、[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)オブジェクトでカプセル化された[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)コレクションの[**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream))メソッドを呼び出します。[**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)オブジェクトの[**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)メソッドを使用してセル範囲を指定します。

以下は、下記のコードによって生成されるファイルのスクリーンショットです。

**セル参照に基づいて画像を挿入する**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## サンプルコード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
