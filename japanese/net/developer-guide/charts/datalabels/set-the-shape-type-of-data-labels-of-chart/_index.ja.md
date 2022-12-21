---
title: グラフのデータ ラベルの形状タイプを設定する
type: docs
weight: 110
url: /ja/net/set-the-shape-type-of-data-labels-of-chart/
---
## **考えられる使用シナリオ**
DataLabels.ShapeType プロパティを使用して、チャートのデータ ラベルの形状タイプを変更できます。 DataLabelShapeType 列挙の値を取得し、それに応じてデータ ラベルの形状の種類を変更します。その値のいくつかは

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **グラフのデータ ラベルの形状タイプを設定する**
次のサンプル コードは、チャートのデータ ラベルの形状タイプを DataLabelShapeType.WedgeEllipseCallout に変更します。をご覧ください[サンプル Excel ファイル](60489778.xlsx)このコードと[出力エクセルファイル](60489779.xlsx)それによって生成されます。スクリーンショットは、サンプル Excel ファイルに対するコードの効果を示しています。

![todo:画像_代替_文章](set-the-shape-type-of-data-labels-of-chart_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
