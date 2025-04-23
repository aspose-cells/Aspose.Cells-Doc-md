---
title: スマートアートをグループ形状に変換
type: docs
weight: 80
url: /ja/java/convert-the-smart-art-to-group-shape/
---

## **可能な使用シナリオ**

Smart Art ShapeをGroup Shapeに変換するには、[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--)メソッドを使用します。これにより、スマートアートの形状をグループ形状として扱えるようになります。それにより、グループ形状の個々の部分または形状にアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

以下のサンプルコードは、このスクリーンショットに示すようなスマートアート形状を含む[sample Excel file](55541806.xlsx)をロードします。その後、スマートアート形状をグループ形状に変換し、[Shape.IsGroup](https://reference.aspose.com/cells/java/com.aspose.cells/shape#IsGroup)プロパティを出力します。以下に示したサンプルコードのコンソール出力をご覧ください。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-ConvertSmartArtToGroupShape.java" >}}

## **コンソール出力**

{{< highlight java >}}

Is Smart Art Shape: true

Is Group Shape: false

Is Group Shape: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
