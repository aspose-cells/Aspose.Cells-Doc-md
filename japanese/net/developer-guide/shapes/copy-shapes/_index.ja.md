---
title: ワークシート間でシェイプをコピーする
linktitle: シェイプをコピーする
type: docs
weight: 200
url: /ja/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

時々、ワークシート上の要素（例えば、画像、グラフ、その他の図形オブジェクト）を他のワークシート間でコピーする必要があります。Aspose.Cells はこの機能をサポートしています。チャート、画像、その他のオブジェクトは高度な精度でコピーすることができます。

この記事では、ワークシート間でシェイプをコピーする方法について詳しく説明します。

{{% /alert %}}

## **ワークシート間での画像のコピー**

ワークシート間での画像のコピーには、以下のサンプルコードに示すように [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) メソッドを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **ワークシート間でのグラフのコピー**

次のコードは、[**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) メソッドを使用して、ワークシート間でのチャートのコピーを示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **ワークシート間でのコントロールおよびその他の図形オブジェクトのコピー**

コントロールやその他の図形オブジェクトをコピーするには、次の例に示すように [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) メソッドを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
