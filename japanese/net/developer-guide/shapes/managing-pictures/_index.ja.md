---
title: 画像の管理
type: docs
weight: 10
url: /ja/net/managing-pictures/
---

Aspose.Cellsを使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の位置を実行時に制御することができます。これについては後のセクションで詳しく説明します。

この記事では、画像の追加方法と特定のセルの内容を示す画像の挿入方法について説明します。

## **画像の追加**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:
単純に、[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)コレクション（[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトでカプセル化）の[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドを呼び出します。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドには以下のパラメータが必要です:

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **写真の位置合わせ**

Aspose.Cellsを使用して写真の位置合わせを制御する方法には2つの方法があります:

- 比例位置合わせ：行の高さと幅に比例した位置を定義します。
- 絶対位置合わせ：ページ上の画像の挿入位置を正確に定義します。例：セルの左から40ピクセル、上から20ピクセル。

### **比例位置合わせ**

開発者は、[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトの[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax)および[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay)プロパティを使用して、行の高さと列の幅に比例した位置に写真を配置できます。[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)コレクションからその写真のインデックスを渡すことで[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトを取得できます。この例では、F6セルに画像を配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **絶対位置づけ**

開発者は、[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトの[**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left)および[**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top)プロパティを使用して、絶対位置に写真を配置することもできます。この例では、セルF6に画像を配置し、左から60ピクセル、上から10ピクセルに配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **セル参照に基づいて画像を挿入**

Aspose.Cellsを使用すると、ワークシートのセルの内容を画像形状で表示できます。画像は、データを表示したいセルにリンクされています。セルまたはセル範囲がグラフィックオブジェクトにリンクされているため、そのセルまたはセル範囲のデータを変更すると、自動的にグラフィックオブジェクトに変更が反映されます。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトでカプセル化された[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)コレクションの[**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)メソッドを呼び出すことで、ワークシートに画像を追加します。[**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトの[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)属性を使用してセル範囲を指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/net/add-conditional-icons-set-with-the-cell-text/)
- [Webアドレスからリンクされた画像の挿入](/cells/ja/net/insert-a-linked-picture-from-web-address/)
- [セル参照に基づく画像の挿入](/cells/ja/net/insert-a-picture-based-on-cell-reference/)
- [Web画像のURLをExcelワークシートに読み込む](/cells/ja/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

