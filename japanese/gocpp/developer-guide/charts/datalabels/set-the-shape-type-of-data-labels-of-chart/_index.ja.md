---
title: GolangからC++を使ってチャートのデータラベルの形状タイプを設定する
linktitle: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for C++を使用してチャートのデータラベルのシェイプタイプを設定する方法を学びます。さまざまなシェイプタイプと、データラベルのプレゼンテーションと使いやすさを向上させる最適なシェイプ選択方法を説明します。
keywords: Aspose.Cells for C++、チャート作成、データラベル、シェイプタイプ、プレゼンテーション、使いやすさ。
type: docs
weight: 110
url: /ja/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
`DataLabels.ShapeType`プロパティを使用して、チャートのデータラベルのシェイプタイプを変更できます。これは`DataLabelShapeType`列挙型の値を受け取り、適切なシェイプタイプに設定します。

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプを`DataLabelShapeType.WedgeEllipseCallout`に変更します。コードで使用されたサンプルExcelファイル（60489778.xlsx）と、それによって生成された出力Excelファイル（60489779.xlsx）をご覧ください。スクリーンショットは、このコードの効果を示すサンプルExcelファイルの様子です。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
