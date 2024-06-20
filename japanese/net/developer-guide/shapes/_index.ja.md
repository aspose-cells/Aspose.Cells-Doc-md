---
title: Excelファイルの画像と図形を挿入する
linktitle: シェイプ
type: docs
weight: 140
url: /ja/net/insert-shapes/
description: Excelファイルに写真、OLEオブジェクト、図形を管理する
---

{{% alert color="primary" %}}

時々、ワークシートに必要な形状を挿入する必要があります。ワークシートの異なる位置に同じ形状を挿入する必要があったり、ワークシートに複数の形状を一括挿入する必要があるかもしれません。

心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)はこれらの操作をすべてサポートしています。

{{% /alert %}}

Excelの形状は主に以下の種類に分かれています：
- **写真**
- **OLEオブジェクト**
- **直線**
- **四角形**
- **基本図形**
- **ブロック矢印**
- **数式図形**
- **フローチャート**
- **星とバナー**
- **吹き出し**

このガイド文書では、各タイプから1つか2つの図形を選択してサンプルを作成します。これらの例を通じて、指定の形状をワークシートに挿入する方法を学ぶことができます。[Aspose.Cells](https://products.aspose.com/cells/)を使用しています。

## **C#でExcelワークシートに画像を追加する**

スプレッドシートに写真を追加するのは非常に簡単です。わずかなコード行だけで済みます:
単純に、[**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)コレクション（[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)オブジェクトでカプセル化）の[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドを呼び出します。[**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドには以下のパラメータが必要です:

- **左上の行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **C#でExcelワークシートにOLEオブジェクトを挿入する**

Aspose.Cellsはワークシート内のOLEオブジェクトの追加、抽出、および操作をサポートしています。そのため、Aspose.Cellsには新しいOLEオブジェクトをコレクションリストに追加するために使用される[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)クラスがあります。また、[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)という別のクラスはOLEオブジェクトを表します。いくつかの重要なメンバーがあります。

- [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)プロパティはバイト配列型の画像（アイコン）データを指定します。画像はOLEオブジェクトを示すために表示されます。
- [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)プロパティはバイト配列形式のオブジェクトデータを指定します。このデータは、OLEオブジェクトアイコンをダブルクリックすると関連するプログラムに表示されます。

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **C#でExcelワークシートに行を挿入する**

線の形状は**線**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 線を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線を選択します

![](line.png)

***Aspose.Cells を使用***

ワークシートに線を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

このメソッドは[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに線を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](line2.png)



## **C#でExcelワークシートに矢印の形の直線を挿入する**

直線矢印の形状は**直線**のカテゴリに属します。これは直線の特別な場合です。

***Microsoft Excel（例: 2007年）***

- 矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から直線矢印を選択します

![](line_arrow1.png)

***Aspose.Cells を使用***

ワークシートに直線矢印を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

このメソッドは[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに直線矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](line_arrow2.png)



## **C#でExcelワークシートに長方形を挿入する**

長方形の形状は**矩形**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 長方形を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した形」または「長方形」から長方形を選択します。

![](rectangle.png)

***Aspose.Cells を使用***

ワークシートに長方形を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

このメソッドは、[RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに長方形を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](rectangle2.png)



## **C# で Excel ワークシートに立方体を挿入する**

キューブの形は**Basic Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- キューブを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「基本形」からキューブを選択します

![](cube.png)

***Aspose.Cells を使用***

ワークシートにキューブを挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにキューブを挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](cube2.png)



## **C# で Excel ワークシートに吹き出し四角矢印を挿入する**

コールアウト四角矢印の形は**Block Arrows**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- コールアウト四角矢印を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「ブロック矢印」からコールアウト四角矢印を選択します

![](callout_quad_arrow.png)

***Aspose.Cells を使用***

ワークシートにコールアウト四角矢印を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにコールアウト四角矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](callout_quad_arrow2.png)



## **C# で Excel ワークシートに掛け算記号を挿入する**

乗算記号の形は**Equation Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 乗算記号を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**数式図形**から乗算記号を選択します

![](multiplication_sign.png)

***Aspose.Cells を使用***

次の方法を使用してワークシートに乗算記号を挿入できます。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに乗算記号を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](multiplication_sign2.png)



## **C#でExcelワークシートに多重ドキュメントを挿入する**

多重ドキュメントの形状は**フローチャート**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 多重ドキュメントを挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**フローチャート**から多重ドキュメントを選択します

![](multidocument.png)

***Aspose.Cells を使用***

次の方法を使用してワークシートに多重ドキュメントを挿入できます。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに多重ドキュメントを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](multidocument2.png)



## **C#でExcelワークシートに五角星を挿入する**

五角星の形状は**星とバナー**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 五角星を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**星とバナー**から五角星を選択します

![](star_5_points.png)

***Aspose.Cells を使用***

この方法は [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

上記のコードを実行すると、次の結果が得られます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](star_5_points2.png)



## **C#でExcelワークシートに思考バブルクラウドを挿入する**

思考バブルクラウドの形状は**吹き出し**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 思考バブルクラウドを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、**吹き出し** から思考バブルクラウドを選択します。

![](thought_bubble_cloud.png)

***Aspose.Cells を使用***

ワークシートに思考バブルクラウドを挿入するために次の方法を使用できます。

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

このメソッドは[Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに思考バブルクラウドを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](thought_bubble_cloud2.png)

## **高度なトピック**
- [図形の調整値を変更](/cells/ja/net/change-adjustment-values-of-the-shape/)
- [ワークシート間で図形をコピーする](/cells/ja/net/copy-shapes-between-worksheets/)
- [非プリミティブ形状のデータ](/cells/ja/net/data-in-non-primitive-shape/)
- [ワークシート内の形状の絶対位置を検索する](/cells/ja/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [形状から接続ポイントを取得する](/cells/ja/net/get-connection-points-from-shape/)
- [コントロールの管理](/cells/ja/net/managing-controls/)
- [ワークシートにアイコンを追加する](/cells/ja/net/insert-svg-to-excel/)
- [OLE オブジェクトの管理](/cells/ja/net/managing-ole-objects/)
- [画像の管理](/cells/ja/net/managing-pictures/)
- [Smart Art の管理](/cells/ja/net/managing-smartart/)
- [テキストボックスの管理](/cells/ja/net/managing-textbox-of-excel/)
- [Aspose.Cells にワードアートウォーターマークを追加](/cells/ja/net/add-wordart-watermark-to-worksheet/)
- [リンクされた図形の値を更新する](/cells/ja/net/refresh-values-of-linked-shapes/)
- [ワークシート内でShape FrontまたはBackを送信する](/cells/ja/net/send-shape-front-or-back-inside-the-worksheet/)
- [形状オプションを管理する](/cells/ja/net/managing-shape-options/)
- [形状テキストオプションの管理](/cells/ja/net/managing-shape-text-options/)
- [Web拡張 - Office アドイン](/cells/ja/net/web-extensions-office-add-ins/)

