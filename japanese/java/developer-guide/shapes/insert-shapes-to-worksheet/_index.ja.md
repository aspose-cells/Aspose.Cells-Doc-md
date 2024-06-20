---
title: Aspose.Cellsでワークシートに形状を挿入する
type: docs
weight: 5
url: /ja/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

時々、ワークシートに必要な形状を挿入する必要があります。ワークシートの異なる位置に同じ形状を挿入する必要があったり、ワークシートに複数の形状を一括挿入する必要があるかもしれません。

心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)はこれらの操作をすべてサポートしています。

{{% /alert %}}

Excelの形状は主に以下の種類に分かれています：
- **直線**
- **四角形**
- **基本図形**
- **ブロック矢印**
- **数式図形**
- **フローチャート**
- **星とバナー**
- **吹き出し**

このガイド文書では、各タイプから1つか2つの図形を選択してサンプルを作成します。これらの例を通じて、指定の形状をワークシートに挿入する方法を学ぶことができます。[Aspose.Cells](https://products.aspose.com/cells/)を使用しています。



## **ワークシートに線を挿入する**

線の形状は**線**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 線を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線を選択します

![](line.png)

***Aspose.Cells を使用***

ワークシートに線を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに線を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](line2.png)



## **ワークシートに矢印を挿入する**

直線矢印の形状は**直線**のカテゴリに属します。これは直線の特別な場合です。

***Microsoft Excel（例: 2007年）***

- 矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から直線矢印を選択します

![](line_arrow1.png)

***Aspose.Cells を使用***

ワークシートに直線矢印を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに直線矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](line_arrow2.png)



## **ワークシートに四角形を挿入する**

長方形の形状は**矩形**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 長方形を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した形」または「長方形」から長方形を選択します。

![](rectangle.png)

***Aspose.Cells を使用***

ワークシートに長方形を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに長方形を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](rectangle2.png)



## **ワークシートに立方体を挿入する**

キューブの形は**Basic Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- キューブを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「基本形」からキューブを選択します

![](cube.png)

***Aspose.Cells を使用***

ワークシートにキューブを挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにキューブを挿入する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](cube2.png)



## **ワークシートにスピーチバブルを挿入する**

コールアウト四角矢印の形は**Block Arrows**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- コールアウト四角矢印を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「ブロック矢印」からコールアウト四角矢印を選択します

![](callout_quad_arrow.png)

***Aspose.Cells を使用***

ワークシートにコールアウト四角矢印を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにコールアウト四角矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](callout_quad_arrow2.png)



## **ワークシートに乗算記号を挿入する**

乗算記号の形は**Equation Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 乗算記号を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**数式図形**から乗算記号を選択します

![](multiplication_sign.png)

***Aspose.Cells を使用***

次の方法を使用してワークシートに乗算記号を挿入できます。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに乗算記号を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](multiplication_sign2.png)



## **ワークシートにマルチドキュメントを挿入する**

多重ドキュメントの形状は**フローチャート**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 多重ドキュメントを挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**フローチャート**から多重ドキュメントを選択します

![](multidocument.png)

***Aspose.Cells を使用***

次の方法を使用してワークシートに多重ドキュメントを挿入できます。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに多重ドキュメントを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](multidocument2.png)



## **ワークシートに五角星を挿入する**

五角星の形状は**星とバナー**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 五角星を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**星とバナー**から五角星を選択します

![](star_5_points.png)

***Aspose.Cells を使用***

この方法は [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

上記のコードを実行すると、次の結果が得られます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](star_5_points2.png)



## **ワークシートに思考バブルクラウドを挿入する**

思考バブルクラウドの形状は**吹き出し**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 思考バブルクラウドを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、**吹き出し** から思考バブルクラウドを選択します。

![](thought_bubble_cloud.png)

***Aspose.Cells を使用***

ワークシートに思考バブルクラウドを挿入するために次の方法を使用できます。

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

この方法は、[Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに思考バブルクラウドを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](thought_bubble_cloud2.png)
