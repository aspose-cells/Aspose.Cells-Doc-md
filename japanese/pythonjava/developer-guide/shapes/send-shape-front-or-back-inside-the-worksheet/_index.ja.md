---
title: シェイプを前面または背面に移動させる
type: docs
weight: 3400
url: /ja/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能な使用シナリオ**

同じ位置に複数の形状がある場合、それらの表示順序位置によって表示されるかどうかが決まります。 Aspose.Cellsは、形状のz-オーダーの位置を変更する[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) メソッドを提供します。形状を背面に送信する場合は、-1、-2、-3などの負の数を使用し、形状を前面に送信する場合は、1、2、3などの正の数を使用します。

## **ワークシート内でシェイプを前面または背面に移動させる**

次のサンプルコードは、[**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int))メソッドの使い方について説明しています。コード内で使用されている[サンプルExcelファイル](sampleToFrontOrBack.xlsx)と、その結果生成された[アウトプットExcelファイル](50528331.xlsx)を確認してください。スクリーンショットはコードの実行結果に対するExcelファイルの効果を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
