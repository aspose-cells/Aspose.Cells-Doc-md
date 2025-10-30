---
title: シェイプ内のテクスチャとして画像をタイル状に配置
type: docs
weight: 1700
url: /ja/python-net/tile-picture-as-a-texture-inside-the-shape/
---

## **可能な使用シナリオ**

画像が小さく、品質を失うことなく形状の全体の表面をカバーしない場合、タイリングするオプションがあります。タイリングは、タイルであるかのように小さな画像で形状の表面を埋めるものです。

## **画像を形状の内部にテクスチャとしてタイル状にする**

形状表面を画像で塗りつぶしてタイルにする場合は、[**Shape.fill.texture_fill.is_tiling**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/texturefill/is_tiling) プロパティを使用して **true** に設定します。参照用のサンプルコード、[サンプルエクセルファイル](46465050.xlsx)、スクリーンショットをご覧ください。

## **スクリーンショット**

![todo:image_alt_text](tile-picture-as-a-texture-inside-the-shape_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Options-TilePictureAsTextureInsideShape.py" >}}
{{< app/cells/assistant language="python-net" >}}
