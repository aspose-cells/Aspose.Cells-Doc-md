---
title: DrawObjectEventHandler クラスを使用して PDF へのレンダリング中に DrawObject と Bound を取得する
type: docs
weight: 60
url: /ja/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **考えられる使用シナリオ**

Aspose.Cells は抽象クラスを提供します[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)を持っている[**描く（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)） 方法。ユーザーが実装できる[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)を利用し、[**描く（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) メソッドを取得する[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)と**バウンド**Excel を PDF またはイメージにレンダリングしている間。のパラメータを簡単に説明します。[**描く（）**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)） 方法。

- 描画オブジェクト:[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)レンダリング時に初期化されて返されます

- x: 左[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: 上[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- 幅: の幅[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- 高さ: の高さ[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

ExcelファイルをPDFにレンダリングしている場合は、利用できます[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)クラス[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler).同様に、Excel ファイルを画像にレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)クラス[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **DrawObjectEventHandler クラスを使用して Pdf へのレンダリング中に DrawObject と Bound を取得する**

以下のサンプルコードをご覧ください。それは[サンプル Excel ファイル](64716843.xlsx)そしてそれをとして保存します[出力 PDF](64716842.pdf)PDFにレンダリングしながら、それは利用します[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)プロパティとキャプチャ[**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)と**バウンド**画像などの既存のセルとオブジェクトの。 drawObject タイプが Cell の場合、その Bound と StringValue を出力します。また、drawObject タイプが Image の場合、その Bound および Shape Name を出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
