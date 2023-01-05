---
title: Excel ファイルの画像と図形を挿入します。
linktitle: 形
type: docs
weight: 140
url: /ja/net/insert-shapes/
description: 写真、オブジェクト、図形を Excel ファイルで管理します。
---
{{% alert color="primary" %}}

必要な図形をワークシートに挿入する必要がある場合があります。ワークシートの異なる位置に同じ図形を挿入する必要がある場合があります。または、ワークシートに図形を一括挿入する必要がある場合もあります。

心配しないでください！[Aspose.Cells](https://products.aspose.com/cells/)これらすべての操作をサポートします。

{{% /alert %}}

Excel の図形は、主に次の種類に分類されます。
- **ピクチャー**
- **OleObjects**
- **ライン**
- **長方形**
- **基本形状**
- **ブロック矢印**
- **方程式の形**
- **フローチャート**
- **星と旗**
- **吹き出し**

このガイド ドキュメントでは、各タイプから 1 つまたは 2 つの形状を選択してサンプルを作成します。これらの例を通じて、使用方法を学習します。[Aspose.Cells](https://products.aspose.com/cells/)指定した形状をワークシートに挿入します。

## **C# の Excel ワークシートに画像を追加する**

スプレッドシートに画像を追加するのはとても簡単です。数行のコードしか必要ありません。
単純に[**追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)の方法[**ピクチャー**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)コレクション ([**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)物体）。の[**追加**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)メソッドは次のパラメータを取ります。

- **左上行インデックス**、左上の行のインデックス。
- **左上の列インデックス**、左上の列のインデックス。
- **画像ファイル名**、パスを含む画像ファイルの名前。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **C# の Excel ワークシートに OLE オブジェクトを挿入する**

Aspose.Cells は、ワークシートでの OLE オブジェクトの追加、抽出、および操作をサポートしています。このため、Aspose.Cells には[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection)コレクション リストに新しい OLE オブジェクトを追加するために使用されるクラス。別のクラス、[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject)、OLE オブジェクトを表します。いくつかの重要なメンバーがあります。

- の[**画像データ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)プロパティは、バイト配列型のイメージ (アイコン) データを指定します。画像が表示され、ワークシートに OLE オブジェクトが表示されます。
- の[**オブジェクトデータ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)プロパティは、バイト配列の形式でオブジェクト データを指定します。このデータは、OLE オブジェクト アイコンをダブルクリックすると、関連するプログラムに表示されます。

次の例は、OLE オブジェクトをワークシートに追加する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **C# の Excel ワークシートに行を挿入する**

線の形はに属します**行**カテゴリー。

***Microsoft Excel (例: 2007):***

- 行を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線を選択します

![](line.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに行を挿入できます。

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

メソッドは[線の形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)物体。

{{% /alert %}}

次の例は、ワークシートに行を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](line2.png)



## **C# の Excel ワークシートに線矢印を挿入する**

線矢印の形状は、**ライン**カテゴリ。ラインの特殊なケースです。

***Microsoft Excel (例: 2007):***

- 線の矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線の矢印を選択します

![](line_arrow1.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに線の矢印を挿入できます。

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

メソッドは[線の形状](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape)物体。

{{% /alert %}}

次の例は、ワークシートに線矢印を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](line_arrow2.png)



## **C# の Excel ワークシートに四角形を挿入する**

長方形の形状は、**長方形**カテゴリー。

***Microsoft Excel (例: 2007):***

- 四角形を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した形状」または「長方形」から長方形を選択します

![](rectangle.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに四角形を挿入できます。

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

メソッドは[長方形の形](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape)物体。

{{% /alert %}}

次の例は、四角形をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](rectangle2.png)



## **C# の Excel ワークシートにキューブを挿入する**

立方体の形状は、**基本形状**カテゴリー。

***Microsoft Excel (例: 2007):***

- 立方体を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、からキューブを選択します**基本形状**

![](cube.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートにキューブを挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、キューブをワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](cube2.png)



## **C# の Excel ワークシートに吹き出し四角矢印を挿入する**

吹き出しの四角形矢印の形状は、**ブロック矢印**カテゴリー。

***Microsoft Excel (例: 2007):***

- 吹き出しの四角形矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、吹き出しのクワッド矢印を選択します。**ブロック矢印**

![](callout_quad_arrow.png)

***Aspose.Cells を使用***

次の方法を使用して、ワークシートに四角形吹き出し矢印を挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、吹き出し四角形矢印をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](callout_quad_arrow2.png)



## **C# の Excel ワークシートに乗算記号を挿入する**

乗算記号の形状は、**方程式の形**カテゴリー。

***Microsoft Excel (例: 2007):***

- 乗算記号を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、から乗算記号を選択します**方程式の形**

![](multiplication_sign.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに乗算記号を挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、乗算記号をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](multiplication_sign2.png)



## **マルチドキュメントを C# の Excel ワークシートに挿入する**

multidocument の形状は、**フローチャート**カテゴリー。

***Microsoft Excel (例: 2007):***

- マルチドキュメントを挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、マルチドキュメントを選択します**フローチャート**

![](multidocument.png)

***Aspose.Cells を使用***

次のメソッドを使用して、マルチドキュメントをワークシートに挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、マルチドキュメントをワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](multidocument2.png)



## **C# の Excel ワークシートに五芒星を挿入する**

五芒星の形状は、**星と旗**カテゴリー。

***Microsoft Excel (例: 2007):***

- 五芒星を挿入したいセルを選択
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に五芒星を選択します。**星と旗**

![](star_5_points.png)

***Aspose.Cells を使用***

次のメソッドを使用して、ワークシートに五芒星を挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、ワークシートに五芒星を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](star_5_points2.png)



## **C# の Excel ワークシートに吹き出し雲を挿入する**

思考の泡の雲の形は、**吹き出し**カテゴリー。

***Microsoft Excel (例: 2007):***

- ふきだし雲を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、から思考の泡の雲を選択します**吹き出し**

![](thought_bubble_cloud.png)

***Aspose.Cells を使用***

次の方法を使用して、ワークシートに吹き出しの雲を挿入できます。

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType タイプ、
 int upperLeftRow、
整数トップ、
 int upperLeftColumn、
整数左、
整数の高さ、
整数幅
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

メソッドは[形](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)物体。

{{% /alert %}}

次の例は、吹き出しの雲をワークシートに挿入する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

上記のコードを実行すると、次の結果が得られます。

![](thought_bubble_cloud2.png)

## **先行トピック**
- [シェイプの調整値を変更する](/cells/ja/net/change-adjustment-values-of-the-shape/)
- [ワークシート間で図形をコピーする](/cells/ja/net/copy-shapes-between-worksheets/)
- [非プリミティブ形状のデータ](/cells/ja/net/data-in-non-primitive-shape/)
- [ワークシート内の形状の絶対位置を見つける](/cells/ja/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [シェイプから接続ポイントを取得する](/cells/ja/net/get-connection-points-from-shape/)
- [コントロールの管理](/cells/ja/net/managing-controls/)
- [ワークシートにアイコンを追加](/cells/ja/net/insert-svg-to-excel/)
- [OLE オブジェクトの管理](/cells/ja/net/managing-ole-objects/)
- [画像の管理](/cells/ja/net/managing-pictures/)
- [スマート アートの管理](/cells/ja/net/managing-smartart/)
- [テキストボックスの管理](/cells/ja/net/managing-textbox-of-excel/)
- [ワードアートの透かしをワークシートに追加する](/cells/ja/net/add-wordart-watermark-to-worksheet/)
- [リンクされた図形の値を更新](/cells/ja/net/refresh-values-of-linked-shapes/)
- [ワークシート内の形状を前面または背面に送信](/cells/ja/net/send-shape-front-or-back-inside-the-worksheet/)
- [形状オプションの管理](/cells/ja/net/managing-shape-options/)
- [シェイプ テキスト オプションの管理](/cells/ja/net/managing-shape-text-options/)
- [Web 拡張機能 - Office アドイン](/cells/ja/net/web-extensions-office-add-ins/)

