---
title: 画像の管理
type: docs
weight: 10
url: /ja/python-net/managing-pictures/
---

Aspose.Cells for Python via .NETを使用すると、開発者はスプレッドシートに画像を実行時に追加できます。さらに、これらの画像の位置を実行時に制御できることについて詳細に解説します。

この記事では、画像の追加方法と特定のセルの内容を示す画像の挿入方法について説明します。

## **画像の追加**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:
単純に、[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)コレクション（[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)オブジェクトでカプセル化）の[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)メソッドを呼び出します。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)メソッドには以下のパラメータが必要です:

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **写真の位置合わせ**

Aspose.Cells for Python via .NETを使って画像の位置を制御する方法は二つあります：

- 比例位置合わせ：行の高さと幅に比例した位置を定義します。
- 絶対位置合わせ：ページ上の画像の挿入位置を正確に定義します。例：セルの左から40ピクセル、上から20ピクセル。

### **比例位置合わせ**

開発者は、[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)オブジェクトの[**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x)および[**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y)プロパティを使用して、行の高さと列の幅に比例した位置に写真を配置できます。[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)コレクションからその写真のインデックスを渡すことで[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)オブジェクトを取得できます。この例では、F6セルに画像を配置します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **絶対位置づけ**

開発者は、[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)オブジェクトの[**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left)および[**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top)プロパティを使用して、絶対位置に写真を配置することもできます。この例では、セルF6に画像を配置し、左から60ピクセル、上から10ピクセルに配置します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **セル参照に基づいて画像を挿入**

Aspose.Cells for Python via .NETは、ワークシートセルの内容を画像の形に表示でき、表示したいデータが含まれるセルにリンクさせることができます。セルまたはセル範囲をグラフィックオブジェクトにリンクさせると、そのセルまたはセル範囲のデータの変更が自動的にグラフィックオブジェクトに反映されます。

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)オブジェクトでカプセル化された[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)コレクションの[**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)メソッドを呼び出すことで、ワークシートに画像を追加します。[**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)オブジェクトの[**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula)属性を使用してセル範囲を指定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **高度なトピック**
- [セルのテキストと条件付きアイコンセットの追加](/cells/ja/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Webアドレスからリンクされた画像の挿入](/cells/ja/python-net/insert-a-linked-picture-from-web-address/)
- [セル参照に基づく画像の挿入](/cells/ja/python-net/insert-a-picture-based-on-cell-reference/)
- [Web画像のURLをExcelワークシートに読み込む](/cells/ja/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

