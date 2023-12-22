---
title: グラフのデータラベルの形状タイプを設定する
description: Aspose.Cells for .NET を使用してグラフのデータ ラベルの形状タイプを設定する方法を学びます。このガイドでは、利用可能なさまざまな形状タイプについて説明し、グラフの表示と使いやすさを向上させるためにデータ ラベルに適切な形状を選択する方法を示します。
keywords: Aspose.Cells for .NET, charting, data labels, shape types, presentation, usability.
type: docs
weight: 110
url: /ja/net/set-the-shape-type-of-data-labels-of-chart/
---
##  **考えられる使用シナリオ**
DataLabels.ShapeType プロパティを使用して、グラフのデータ ラベルの形状タイプを変更できます。 DataLabelShapeType 列挙体の値を取得し、それに応じてデータ ラベルの形状タイプを変更します。その値の一部は次のとおりです。

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
##  **グラフのデータラベルの形状タイプを設定する**
次のサンプル コードでは、グラフのデータ ラベルの形状タイプを DataLabelShapeType.WedgeEllipseCallout に変更します。をご覧ください。[サンプル Excel ファイル](60489778.xlsx)このコードで使用されている、[Excelファイルを出力](60489779.xlsx)それによって生み出されたもの。スクリーンショットは、サンプル Excel ファイルに対するコードの効果を示しています。

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
