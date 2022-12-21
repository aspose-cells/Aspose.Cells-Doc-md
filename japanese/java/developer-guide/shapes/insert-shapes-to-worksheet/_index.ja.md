---
title: Aspose.Cells のワークシートに図形を挿入
type: docs
weight: 5
url: /ja/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

必要な図形をワークシートに挿入する必要がある場合があります。ワークシートの異なる位置に同じ図形を挿入する必要がある場合があります。または、ワークシートに図形を一括挿入する必要がある場合もあります。

心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)これらすべての操作をサポートします。

{{% /alert %}}

Excel の図形は、主に次の種類に分類されます。
- **ライン**
- **長方形**
- **基本形**
- **ブロック矢印**
- **方程式の形**
- **フローチャート**
- **星と旗**
- **吹き出し**

このガイド ドキュメントでは、各タイプから 1 つまたは 2 つの形状を選択してサンプルを作成します。これらの例を通じて、使用方法を学習します。[Aspose.Cells](https://products.aspose.com/cells/)指定した形状をワークシートに挿入します。



## **ワークシートへの行の挿入**

線の形はに属します**行**カテゴリー。

***Microsoft Excel (例: 2007):***

- 行を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線を選択します

![](line.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに行を挿入できます。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、ワークシートに行を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](line2.png)



## **ワークシートに線矢印を挿入する**

線矢印の形状は、**ライン**カテゴリ。ラインの特殊なケースです。

***Microsoft Excel (例: 2007):***

- 線の矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線の矢印を選択します

![](line_arrow1.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに線の矢印を挿入できます。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、ワークシートに線矢印を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](line_arrow2.png)



## **ワークシートへの長方形の挿入**

長方形の形状は、**長方形**カテゴリー。

***Microsoft Excel (例: 2007):***

- 四角形を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した形状」または「長方形」から長方形を選択します

![](rectangle.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに四角形を挿入できます。

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、四角形をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](rectangle2.png)



## **ワークシートへのキューブの挿入**

立方体の形状は、**基本形**カテゴリー。

***Microsoft Excel (例: 2007):***

- 立方体を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、からキューブを選択します**基本形**

![](cube.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートにキューブを挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、キューブをワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](cube2.png)



## **Worksheet への四角形吹き出し矢印の挿入**

吹き出しの四角形矢印の形状は、**ブロック矢印**カテゴリー。

***Microsoft Excel (例: 2007):***

- 吹き出しの四角形矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、吹き出しのクワッド矢印を選択します。**ブロック矢印**

![](callout_quad_arrow.png)

***Aspose.Cells を使用***

次の方法を使用して、ワークシートに四角形吹き出し矢印を挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、吹き出し四角形矢印をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](callout_quad_arrow2.png)



## **ワークシートへの乗算記号の挿入**

乗算記号の形状は、**方程式の形**カテゴリー。

***Microsoft Excel (例: 2007):***

- 乗算記号を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、から乗算記号を選択します**方程式の形**

![](multiplication_sign.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに乗算記号を挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、乗算記号をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](multiplication_sign2.png)



## **ワークシートへのマルチドキュメントの挿入**

multidocument の形状は、**フローチャート**カテゴリー。

***Microsoft Excel (例: 2007):***

- マルチドキュメントを挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、マルチドキュメントを選択します**フローチャート**

![](multidocument.png)

***Aspose.Cells を使用***

次のメソッドを使用して、マルチドキュメントをワークシートに挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、マルチドキュメントをワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](multidocument2.png)



## **ワークシートに五芒星を挿入する**

五芒星の形状は、**星と旗**カテゴリー。

***Microsoft Excel (例: 2007):***

- 五芒星を挿入したいセルを選択
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に五芒星を選択します。**星と旗**

![](star_5_points.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに五芒星を挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、ワークシートに五芒星を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](star_5_points2.png)



## **ふきだし雲をワークシートに挿入する**

思考の泡の雲の形は、**吹き出し**カテゴリー。

***Microsoft Excel (例: 2007):***

- ふきだし雲を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、から思考の泡の雲を選択します**吹き出し**

![](thought_bubble_cloud.png)

***Aspose.Cells を使用***

次の方法を使用して、ワークシートに吹き出しの雲を挿入できます。

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

メソッドは[形](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)物体。

{{% /alert %}}

次の例は、吹き出しの雲をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

上記のコードを実行すると、次の結果が得られます。

![](thought_bubble_cloud2.png)
