---
title: Excelファイルの画像と図形を挿入する
linktitle: シェイプ
type: docs
weight: 140
url: /ja/python-net/insert-shapes/
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
単純に、[**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)コレクション（[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)オブジェクトでカプセル化）の[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)メソッドを呼び出します。[**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)メソッドには以下のパラメータが必要です:

- **upper_left_row**、左上の行のインデックス。
- **upper_left_column**、左上の列のインデックス。
- **file_name**、画像ファイルの名前（パスを含む）。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-Pictures-AddingPictures-1.py" >}}


## **C#でExcelワークシートにOLEオブジェクトを挿入する**

Aspose.Cells for Python via .NET は、ワークシート内のOLEオブジェクトの追加、抽出、操作をサポートします。そのため、`[**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection)`クラスを使用して新しいOLEオブジェクトをコレクションリストに追加します。もう一つのクラス、`[**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject)`はOLEオブジェクトを表し、いくつかの重要なメンバーを持ちます：

- [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data)プロパティはバイト配列型の画像（アイコン）データを指定します。画像はOLEオブジェクトを示すために表示されます。
- [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data)プロパティはバイト配列形式のオブジェクトデータを指定します。このデータは、OLEオブジェクトアイコンをダブルクリックすると関連するプログラムに表示されます。

以下の例は、ワークシートにOLEオブジェクトを追加する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-OLE-InsertingOLEObjects-1.py" >}}

## **C#でExcelワークシートに行を挿入する**

線の形状は**線**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 線を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から線を選択します

![](line.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートに線を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

このメソッドは[LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに線を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Line.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](line2.png)



## **C#でExcelワークシートに矢印の形の直線を挿入する**

直線矢印の形状は**直線**のカテゴリに属します。これは直線の特別な場合です。

***Microsoft Excel（例: 2007年）***

- 矢印を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した図形」または「線」から直線矢印を選択します

![](line_arrow1.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートに直線矢印を挿入するために以下の方法を使用できます。

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

このメソッドは[LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに直線矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-LineArrow.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](line_arrow2.png)



## **C#でExcelワークシートに長方形を挿入する**

長方形の形状は**矩形**のカテゴリに属します。

***Microsoft Excel（例: 2007年）***

- 長方形を挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「最近使用した形」または「長方形」から長方形を選択します。

![](rectangle.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートに長方形を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)

このメソッドは[RectangleShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートに長方形を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Rectangle.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](rectangle2.png)



## **C# で Excel ワークシートに立方体を挿入する**

キューブの形は**Basic Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- キューブを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「基本形」からキューブを選択します

![](cube.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートにキューブを挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**public Shape add_auto_shape(type, upper_left_row, top, upper_left_column, left, height, width)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにキューブを挿入する方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Cube.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](cube2.png)



## **C# で Excel ワークシートに吹き出し四角矢印を挿入する**

コールアウト四角矢印の形は**Block Arrows**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- コールアウト四角矢印を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、「ブロック矢印」からコールアウト四角矢印を選択します

![](callout_quad_arrow.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートにコールアウト四角矢印を挿入するには、次のメソッドを使用できます。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例では、ワークシートにコールアウト四角矢印を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](callout_quad_arrow2.png)



## **C# で Excel ワークシートに掛け算記号を挿入する**

乗算記号の形は**Equation Shapes**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 乗算記号を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**数式図形**から乗算記号を選択します

![](multiplication_sign.png)

***Aspose.Cells for Python via .NET の使用例***

次の方法を使用してワークシートに乗算記号を挿入できます。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに乗算記号を挿入する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](multiplication_sign2.png)



## **C#でExcelワークシートに多重ドキュメントを挿入する**

多重ドキュメントの形状は**フローチャート**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 多重ドキュメントを挿入するセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**フローチャート**から多重ドキュメントを選択します

![](multidocument.png)

***Aspose.Cells for Python via .NET の使用例***

次の方法を使用してワークシートに多重ドキュメントを挿入できます。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに多重ドキュメントを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Multidocument.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](multidocument2.png)



## **C#でExcelワークシートに五角星を挿入する**

五角星の形状は**星とバナー**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 五角星を挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- その後、**星とバナー**から五角星を選択します

![](star_5_points.png)

***Aspose.Cells for Python via .NET の使用例***

この方法は [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) オブジェクトを返します。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

上記のコードを実行すると、次の結果が得られます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-FivePointedStar.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](star_5_points2.png)



## **C#でExcelワークシートに思考バブルクラウドを挿入する**

思考バブルクラウドの形状は**吹き出し**カテゴリに属しています。

***Microsoft Excel（例: 2007年）***

- 思考バブルクラウドを挿入したいセルを選択します
- [挿入] メニューをクリックし、[図形] をクリックします。
- 次に、**吹き出し** から思考バブルクラウドを選択します。

![](thought_bubble_cloud.png)

***Aspose.Cells for Python via .NET の使用例***

ワークシートに思考バブルクラウドを挿入するために次の方法を使用できます。

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

このメソッドは[Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape)オブジェクトを返します。

{{% /alert %}}

次の例は、ワークシートに思考バブルクラウドを挿入する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.py" >}}

上記のコードを実行すると、次の結果が得られます。

![](thought_bubble_cloud2.png)

## **高度なトピック**
- [図形の調整値を変更](/cells/ja/python-net/change-adjustment-values-of-the-shape/)
- [ワークシート間で図形をコピーする](/cells/ja/python-net/copy-shapes-between-worksheets/)
- [非プリミティブ形状のデータ](/cells/ja/python-net/data-in-non-primitive-shape/)
- [ワークシート内の形状の絶対位置を検索する](/cells/ja/python-net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [形状から接続ポイントを取得する](/cells/ja/python-net/get-connection-points-from-shape/)
- [コントロールの管理](/cells/ja/python-net/managing-controls/)
- [ワークシートにアイコンを追加する](/cells/ja/python-net/insert-svg-to-excel/)
- [OLE オブジェクトの管理](/cells/ja/python-net/managing-ole-objects/)
- [画像の管理](/cells/ja/python-net/managing-pictures/)
- [Smart Art の管理](/cells/ja/python-net/managing-smartart/)
- [テキストボックスの管理](/cells/ja/python-net/managing-textbox-of-excel/)
- [Aspose.Cells にワードアートウォーターマークを追加](/cells/ja/python-net/add-wordart-watermark-to-worksheet/)
- [リンクされた図形の値を更新する](/cells/ja/python-net/refresh-values-of-linked-shapes/)
- [ワークシート内でShape FrontまたはBackを送信する](/cells/ja/python-net/send-shape-front-or-back-inside-the-worksheet/)
- [形状オプションを管理する](/cells/ja/python-net/managing-shape-options/)
- [形状テキストオプションの管理](/cells/ja/python-net/managing-shape-text-options/)
- [Web拡張 - Office アドイン](/cells/ja/python-net/web-extensions-office-add-ins/)

