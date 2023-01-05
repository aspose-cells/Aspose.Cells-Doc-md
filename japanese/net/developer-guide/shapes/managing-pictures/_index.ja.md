---
title: 画像の管理
type: docs
weight: 10
url: /ja/net/managing-pictures/
---
Aspose.Cells を使用すると、開発者は実行時にスプレッドシートに画像を追加できます。さらに、これらの画像の配置は実行時に制御できます。これについては、以降のセクションで詳しく説明します。

この記事では、画像を追加する方法と、特定のセルの内容を示す画像を挿入する方法について説明します。

## **写真を追加する**

スプレッドシートに画像を追加するのはとても簡単です。数行のコードしか必要ありません。
単純に[**追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)の方法[**ピクチャー**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体）。の[**追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドは次のパラメータを取ります。

- **左上行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **写真の配置**

Aspose.Cells を使用して画像の位置を制御するには、次の 2 つの方法があります。

- 比例配置: 行の高さと幅に比例した位置を定義します。
- 絶対配置: 画像が挿入されるページ上の正確な位置を定義します。たとえば、セルの端から左に 40 ピクセル、下に 20 ピクセルなどです。

### **プロポーショナルポジショニング**

開発者は、行の高さと列の幅に比例して画像を配置できます[**アッパーデルタX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax)と[**アッパーデルタY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay)のプロパティ[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。あ[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)オブジェクトはから取得できます[**ピクチャー**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)ピクチャ インデックスを渡すことでコレクションを取得します。この例では、画像を F6 セルに配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **絶対位置**

開発者は、を使用して写真を絶対に配置することもできます[**左**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left)と[**上**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top)のプロパティ[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。この例では、セル F6 にイメージを、セルの左から 60 ピクセル、上から 10 ピクセルの位置に配置します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Cell 参照に基づく画像の挿入**

Aspose.Cells では、ワークシート セルの内容を画像の形で表示できます。表示するデータを含むセルに画像をリンクできます。セルまたはセル範囲はグラフィック オブジェクトにリンクされているため、そのセルまたはセル範囲のデータに加えた変更は、グラフィック オブジェクトに自動的に反映されます。

を呼び出して、ワークシートに画像を追加します。[**画像を追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)の方法[**シェイプコレクション**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体）。を使用してセル範囲を指定します。[**方式**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)の属性[**写真**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)物体。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **先行トピック**
- [Cell テキストで設定された条件付きアイコンを追加する](/cells/ja/net/add-conditional-icons-set-with-the-cell-text/)
- [Web アドレスからリンクされた画像を挿入する](/cells/ja/net/insert-a-linked-picture-from-web-address/)
- [Cell 参照に基づいて画像を挿入する](/cells/ja/net/insert-a-picture-based-on-cell-reference/)
- [URL から Web 画像を Excel ワークシートに読み込む](/cells/ja/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

