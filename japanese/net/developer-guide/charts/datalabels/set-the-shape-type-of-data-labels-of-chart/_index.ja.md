---
title: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for .NETを使用して、チャートのデータラベルのシェイプタイプを設定する方法を学習してください。当ガイドでは、使用可能なさまざまなシェイプタイプを説明し、データラベルに適切なシェイプを選択する方法を示します。
keywords: Aspose.Cells for .NET、チャート作成、データラベル、シェイプタイプ、プレゼンテーション、使いやすさ。
type: docs
weight: 110
url: /ja/net/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
データラベルのシェイプタイプを変更するには、DataLabels.ShapeTypeプロパティを使用します。これはDataLabelShapeType列挙型の値を取り、それに応じてデータラベルのシェイプタイプを変更します。

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプをDataLabelShapeType.WedgeEllipseCalloutに変更します。このコードで使用される[サンプルExcelファイル](60489778.xlsx)とそれによって生成される[出力Excelファイル](60489779.xlsx)をご覧ください。スクリーンショットは、サンプルExcelファイルへのコードの影響を示しています。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
