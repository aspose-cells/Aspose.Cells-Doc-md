---
title: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **可能な使用シナリオ**

Aspose.Cellsは、ギアタイプのスマートアートシェイプからテキストを抽出することができます。そのためには、まずスマートアートシェイプを[**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art)メソッドを使用してグループ形状に変換する必要があります。次に、[**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes)メソッドを使用してグループ形状を構成する個々の形状の配列を取得します。最後に、個々の形状をループで一つずつ取得し、[**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text)プロパティを使用してそのテキストを抽出することができます。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、上記で説明したように、Gear Type Smart Art Shapeを含む[sample Excel file](67338483.xlsx)をロードし、その個々の形状からテキストを抽出します。以下は、サンプルコードのコンソール出力です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **コンソール出力**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
