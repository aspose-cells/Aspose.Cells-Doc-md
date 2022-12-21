---
title: 歯車の種類の SmartArt 図形からテキストを抽出する
type: docs
weight: 500
url: /ja/net/extract-text-from-the-gear-type-smartart-shape/
---
## **考えられる使用シナリオ**

Aspose.Cells は、歯車型スマート アート シェイプからテキストを抽出できます。そのためには、まず、Smart Art Shape を Group Shape に変換する必要があります。[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart)方法。次に、グループ シェイプを形成するすべての個々のシェイプの配列を取得する必要があります。[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes)方法。最後に、すべての個々のシェイプをループで 1 つずつ反復し、[**シェイプ.テキスト**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)財産。

## **歯車の種類の SmartArt 図形からテキストを抽出する**

次のサンプル コードは、[サンプル Excel ファイル](67338483.xlsx)ギアタイプのスマートアートシェイプを収録。次に、上記のように個々の形状からテキストを抽出します。以下のコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
