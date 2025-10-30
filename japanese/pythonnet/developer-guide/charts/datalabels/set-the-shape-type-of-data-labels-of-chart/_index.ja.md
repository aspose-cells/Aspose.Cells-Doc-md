---
title: チャートのデータラベルのシェイプタイプを設定する
description: Aspose.Cells for Python via .NETを使ったチャートのデータラベルの形状タイプ設定方法を学びます。利用可能なさまざまな形状タイプの説明と、データラベルに適した形状選択によるチャートの見栄えや使いやすさの向上方法を示します。
keywords: Aspose.Cells for Python via .NET、チャート、データラベル、形状タイプ、プレゼンテーション、使いやすさ。
type: docs
weight: 110
url: /ja/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **可能な使用シナリオ**
データラベルのシェイプタイプを変更するには、DataLabels.ShapeTypeプロパティを使用します。これはDataLabelShapeType列挙型の値を取り、それに応じてデータラベルのシェイプタイプを変更します。

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **チャートのデータラベルの形状タイプを設定する**
以下のサンプルコードは、チャートのデータラベルのシェイプタイプをDataLabelShapeType.WedgeEllipseCalloutに変更します。このコードで使用される[サンプルExcelファイル](60489778.xlsx)とそれによって生成される[出力Excelファイル](60489779.xlsx)をご覧ください。スクリーンショットは、サンプルExcelファイルへのコードの影響を示しています。 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
{{< app/cells/assistant language="python-net" >}}
