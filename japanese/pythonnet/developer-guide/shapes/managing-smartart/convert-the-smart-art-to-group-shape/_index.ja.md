---
title: スマートアートをグループ形状に変換
type: docs
weight: 200
url: /ja/python-net/convert-the-smart-art-to-group-shape/
---

## **可能な使用シナリオ**

Smart Art ShapeをGroup Shapeに変換するには、[**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art/#)メソッドを使用します。これにより、スマートアートの形状をグループ形状として扱えるようになります。それにより、グループ形状の個々の部分または形状にアクセスできるようになります。

## **スマートアートをグループシェイプに変換する**

以下のサンプルコードは、スマートアートシェイプを含む[sample Excel file](55541793.xlsx)をロードし、画像のスクリーンショットに示されているように、スマートアートシェイプをグループ形状に変換し、Shape.IsGroupプロパティを出力します。以下は、サンプルコードのコンソール出力です。

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ConvertSmartArtToGroupShape.py" >}}

## **コンソール出力**

{{< highlight java >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
