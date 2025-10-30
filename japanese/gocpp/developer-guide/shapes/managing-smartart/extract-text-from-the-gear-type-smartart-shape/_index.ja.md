---
title: GearタイプのSmartArt Shapeからテキストを抽出する方法をGo言語とC++を経由して学ぶ
linktitle: ギア型スマートアート形状からテキストを抽出
type: docs
weight: 500
url: /ja/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Aspose.Cells for C++を使用して、ExcelのGearタイプSmartArt Shapeからテキストを抽出する方法をステップバイステップガイドとコード例付きで学びます。
---

## **可能な使用シナリオ**

Aspose.Cells for C++は、GearタイプのSmartArt Shapeからテキストを抽出できます。これを行うためには、以下の手順に従います：
1. SmartArt Shapeを[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/)メソッドを用いてグループシェイプに変換します。
2. [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/)メソッドを使って、グループシェイプを構成するすべての個別シェイプを取得します。
3. 各個別シェイプをループしながら、[**GetText()**](https://reference.aspose.com/cells/go-cpp/)メソッドを用いてテキストを抽出します。

## **ギアタイプのスマートアートシェイプからテキストを抽出する**

以下のサンプルコードは、GearタイプのSmartArt Shapeを含む[サンプルExcelファイル](67338483.xlsx)を読み込み、その個別シェイプからテキストを抽出します。結果はコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **コンソール出力**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
