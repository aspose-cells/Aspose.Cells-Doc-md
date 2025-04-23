---
title: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 130
url: /ja/java/extract-text-from-the-gear-type-smartart-shape/
---

## **可能な使用シナリオ**

Aspose.Cellsはギア型スマートアート形状からテキストを抽出できます。そのためには、まずSmart Art ShapeをGroup Shapeに変換し、[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--) メソッドを使用してグループ形状を形成するすべての個々の形状の配列を取得します。最後に、ループ内で個々の形状を一つずつ反復処理し、[**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)プロパティを使用してテキストを抽出します。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

次のサンプルコードでは、Gear Type Smart Art Shape を含む [サンプルExcelファイル](67338510.xlsx) を読み込み、その個々の図形からテキストを抽出します。参照のために、以下のコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **コンソール出力**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
