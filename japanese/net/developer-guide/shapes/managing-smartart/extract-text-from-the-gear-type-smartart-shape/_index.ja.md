---
title: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/net/extract-text-from-the-gear-type-smartart-shape/
---

## **可能な使用シナリオ**

Aspose.Cellsは、ギアタイプのスマートアートシェイプからテキストを抽出することができます。そのためには、まずスマートアートシェイプを[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart)メソッドを使用してグループ形状に変換する必要があります。次に、[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes)メソッドを使用してグループ形状を構成する個々の形状の配列を取得します。最後に、個々の形状をループで一つずつ取得し、[**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)プロパティを使用してそのテキストを抽出することができます。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、上記で説明したように、Gear Type Smart Art Shapeを含む[sample Excel file](67338483.xlsx)をロードし、その個々の形状からテキストを抽出します。以下は、サンプルコードのコンソール出力です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
