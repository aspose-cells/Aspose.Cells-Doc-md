---
title: ワークシート内のコメントまたは図形の余白を設定する
type: docs
weight: 1500
url: /ja/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NET を使用すると、任意の図形またはコメントの余白を [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment) プロパティを使って設定できます。このプロパティは [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) クラスのオブジェクトを返し、[**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt)、[**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt)、[**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt)、[**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt) などのさまざまなプロパティを持ち、上下左右の余白を設定できます。

## **ワークシート内のコメントまたは図形の余白を設定する**

次のサンプルコードをご覧ください。二つの図形を含む[サンプルエクセルファイル](61767851.xlsx)をロードし、コードでそれぞれの図形にアクセスし、それらの上部、左側、下部、右側の余白を設定します。コードによって生成された[出力エクセルファイル](61767852.xlsx)と、出力エクセルファイルに対するコードの効果を示したスクリーンショットをご覧ください。

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
