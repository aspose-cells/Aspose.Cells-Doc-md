---
title: Smart Artをグループシェイプに変換する方法をGo言語とC++を経由して学ぶ
linktitle: スマートアートをグループ形状に変換
type: docs
weight: 200
url: /ja/go-cpp/convert-the-smart-art-to-group-shape/
description: Aspose.Cells for C++を使用して、Smart Art ShapeをGroup Shapeに変換し、グループシェイプの個々の部分にアクセスする方法を学びます。
---

## **可能な使用シナリオ**

Smart Art ShapeをGroup Shapeに変換するには、[**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/shape/getresultofsmartart/)メソッドを使用します。これにより、スマートアートの形状をグループ形状として扱えるようになります。それにより、グループ形状の個々の部分または形状にアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

以下のサンプルコードは、Smart Art Shapeを含む[sample Excelファイル](55541793.xlsx)を読み込み、スクリーンショットのような表示をします。その後、Smart Art Shapeをグループシェイプに変換し、Shape::IsGroupプロパティを出力します。サンプルコードのコンソール出力例は以下です。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertTheSmartArtToGroupShape.go" >}}
## **コンソール出力**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
