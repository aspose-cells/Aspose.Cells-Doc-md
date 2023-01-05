---
title: ワークシート内の形状を前面または背面に送信
type: docs
weight: 600
url: /ja/java/send-shape-front-or-back-inside-the-worksheet/
---
## **考えられる使用シナリオ**

同じ場所に複数の形状が存在する場合、それらがどのように表示されるかは、Z オーダーの位置によって決まります。 Aspose.Cells提供[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) 形状の z オーダー位置を変更するメソッド。形状を背面に送りたい場合は、-1、-2、-3 などの負の数を使用します。形状を前面に送りたい場合は、1、2、3、などの正の数を使用します。等

## **ワークシート内の形状を前面または背面に送信**

次のサンプル コードは、[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)） 方法。をご覧ください[サンプル Excel ファイル](50528362.xlsx)コード内で使用され、[出力エクセルファイル](50528361.xlsx)それによって生成されます。スクリーンショットは、実行時のサンプル Excel ファイルに対するコードの効果を示しています。

![todo:画像_代替_文章](send-shape-front-or-back-inside-the-worksheet_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
