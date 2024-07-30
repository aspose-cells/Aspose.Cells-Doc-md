---
title: ワークシート間でシェイプをコピーする
linktitle: シェイプをコピーする
type: docs
weight: 200
url: /ja/python-net/copy-shapes-between-worksheets/
description: この記事では、Aspose.Cells for Python via .NET APIを介してワークシート間で図形をコピーする方法を示しています。
keywords: Python Excelライブラリ、Pythonワークシート間で図形をコピー、Pythonでワークシート間で画像をコピーする方法、Pythonでワークシート間でグラフをコピーする方法、Pythonでワークシート間でコントロールや他の描画オブジェクトをコピーする方法。
---

{{% alert color="primary" %}}

時には、ワークシート間で要素（例：画像、グラフ、その他の描画オブジェクト）をコピーする必要があります。Aspose.Cells for Python via .NETはこの機能をサポートしています。チャート、画像、その他のオブジェクトは、最高の精度でコピーされます。

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
