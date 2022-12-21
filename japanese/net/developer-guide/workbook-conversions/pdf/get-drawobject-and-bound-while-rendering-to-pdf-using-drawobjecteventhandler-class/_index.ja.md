---
title: DrawObjectEventHandler クラスを使用して PDF へのレンダリング中に DrawObject と Bound を取得する
type: docs
weight: 70
url: /ja/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **考えられる使用シナリオ**

 Aspose.Cells は抽象クラスを提供します[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)を持っている[**描く（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法。ユーザーが実装できる[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)を利用し、[**描く（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)を取得する方法[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)Excel を PDF または画像にレンダリングする際にバインドされます。のパラメータを簡単に説明します。[**描く（）**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)方法。

- 描画オブジェクト:[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)レンダリング時に初期化されて返されます

- x: 左[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: 上[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- 幅: の幅[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- 高さ: の高さ[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

ExcelファイルをPDFにレンダリングする場合は、利用できます[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)クラス[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler).同様に、Excel ファイルを画像にレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)クラス[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **DrawObjectEventHandler クラスを使用して Pdf へのレンダリング中に DrawObject と Bound を取得する**

以下のサンプルコードをご覧ください。それは[サンプル Excel ファイル](64716821.xlsx)そしてそれをとして保存します[PDF出力](64716822.pdf)PDFにレンダリングしながら、それは利用します[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)プロパティとキャプチャ[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)既存のセルとオブジェクト (画像など) の境界。[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type は Cell で、その Bound と StringValue を出力します。そしてもし[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type は Image で、境界と形状の名前を出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
