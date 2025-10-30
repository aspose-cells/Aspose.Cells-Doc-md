---
title: ワークシート間でシェイプをコピーする
linktitle: シェイプをコピーする
type: docs
weight: 200
url: /ja/python-net/copy-shapes-between-worksheets/
description: この記事では、Aspose.Cells for Python via .NET APIを通じてワークシート間でShapeをコピーする方法を示します。
keywords: Python Excelライブラリ、ワークシート間でShapeをコピーする方法、Pythonで画像を一つのワークシートからもう一つにコピーする方法、Pythonでチャートを一つのワークシートからもう一つにコピーする方法、Pythonでコントロールやその他の描画オブジェクトをコピーする方法。
---

{{% alert color="primary" %}}

時には、ワークシート間で画像やチャート、その他の描画オブジェクトをコピーする必要があります。Aspose.Cells for Python via .NETはこの機能をサポートしています。チャート、画像、およびその他のオブジェクトは高精度でコピー可能です。

この記事では、ワークシート間でシェイプをコピーする方法について詳しく説明します。

{{% /alert %}}

## **ワークシート間での画像のコピー**

ワークシート間での画像のコピーには、以下のサンプルコードに示すように [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) メソッドを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **ワークシート間でのグラフのコピー**

次のコードは、[**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) メソッドを使用して、ワークシート間でのチャートのコピーを示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **ワークシート間でのコントロールおよびその他の図形オブジェクトのコピー**

コントロールやその他の図形オブジェクトをコピーするには、次の例に示すように [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) メソッドを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
{{< app/cells/assistant language="python-net" >}}
