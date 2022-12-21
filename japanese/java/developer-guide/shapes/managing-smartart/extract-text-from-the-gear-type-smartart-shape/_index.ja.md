---
title: 歯車の種類の SmartArt 図形からテキストを抽出する
type: docs
weight: 130
url: /ja/java/extract-text-from-the-gear-type-smartart-shape/
---
## **考えられる使用シナリオ**

Aspose.Cells は、歯車型スマート アート シェイプからテキストを抽出できます。そのためには、まず、Smart Art Shape を Group Shape に変換する必要があります。[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()） 方法。次に、グループ シェイプを形成するすべての個々のシェイプの配列を取得する必要があります。[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()） 方法。最後に、すべての個々のシェイプをループで 1 つずつ反復し、[**シェイプ.テキスト**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)財産。

## **歯車の種類の SmartArt 図形からテキストを抽出する**

次のサンプル コードは、[サンプル Excel ファイル](67338510.xlsx)ギアタイプのスマートアートシェイプを収録。次に、上記のように個々の形状からテキストを抽出します。以下のコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
