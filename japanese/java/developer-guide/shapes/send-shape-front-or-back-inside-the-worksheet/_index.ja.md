---
title: ワークシート内でShape FrontまたはBackを送信する
type: docs
weight: 600
url: /ja/java/send-shape-front-or-back-inside-the-worksheet/
---

## **可能な使用シナリオ**

同じ位置に複数の図形が存在する場合、それらがどのように表示されるかは、z-オーダー位置で決定されます。Aspose.Cellsは、図形のz-オーダー位置を変更する[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-)メソッドを提供します。形を後方に送りたい場合は、-1、-2、-3などの負の数を使用し、形を前方に送りたい場合は、1、2、3などの正の数を使用します。

## **ワークシート内でShape FrontまたはBackを送信する**

次のサンプルコードは、[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-)メソッドの使用方法を説明しています。コード内で使用される[sample Excel file](50528362.xlsx)とそれによって生成される[output Excel file](50528361.xlsx)をご覧ください。スクリーンショットは、コードのサンプルExcelファイルへの効果を示しています。

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
