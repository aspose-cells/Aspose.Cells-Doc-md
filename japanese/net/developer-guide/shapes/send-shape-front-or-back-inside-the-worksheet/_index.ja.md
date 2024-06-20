---
title: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 3400
url: /ja/net/send-shape-front-or-back-inside-the-worksheet/
---

## **可能な使用シナリオ**

同じ位置に複数の形状がある場合、それらの表示順序位置によって表示されるかどうかが決まります。 Aspose.Cellsは、形状のz-オーダーの位置を変更する[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) メソッドを提供します。形状を背面に送信する場合は、-1、-2、-3などの負の数を使用し、形状を前面に送信する場合は、1、2、3などの正の数を使用します。

## **ワークシート内でShape FrontまたはBackを送信する**

次のサンプルコードは、[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) メソッドの使用方法を説明しています。コード内で使用される[sample Excelファイル](50528330.xlsx)と、それによって生成された[output Excelファイル](50528331.xlsx)をご覧ください。スクリーンショットは、サンプルExcelファイルにコードの実行結果の影響を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
