---
title: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 3400
url: /ja/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **可能な使用シナリオ**

同じ場所に複数のシェイプが存在する場合、それらがどのように表示されるかはzオーダー位置によって決まります。Aspose.Cells for Python via .NETは、形状のzオーダー位置を変更する[**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back)メソッドを提供します。形状を背面に送る場合は負の数（-1、-2、-3など）を使用し、前面に送る場合は正の数（1、2、3など）を使用します。

## **ワークシート内でShape FrontまたはBackを送信する**

次のサンプルコードは、[**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) メソッドの使用方法を説明しています。コード内で使用される[sample Excelファイル](50528330.xlsx)と、それによって生成された[output Excelファイル](50528331.xlsx)をご覧ください。スクリーンショットは、サンプルExcelファイルにコードの実行結果の影響を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
