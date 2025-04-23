---
title: DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject および Bound を取得
type: docs
weight: 60
url: /ja/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能な使用シナリオ**

Aspose.Cells は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) という抽象クラスを提供しており、[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) メソッドがあります。ユーザーは [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) を実装し、[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) メソッドを利用して Excel を PDF や画像にレンダリングする際に [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) と **Bound** を取得できます。以下に、[**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) メソッドのパラメータの簡単な説明を示します。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) が初期化され、レンダリング時に返されます

- x: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) の左端

- y: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) の上端

- width: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) の幅

- height: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) の高さ

Excel ファイルを PDF にレンダリングする場合、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) クラスと [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) を利用できます。同様に、Excel ファイルを画像にレンダリングする場合、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) クラスと [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler) を利用できます。

## **DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject と Bound を取得**

以下はサンプルコードです。[サンプル Excel ファイル](64716843.xlsx) を読み込み、それを[出力 PDF](64716842.pdf) として保存します。PDF へのレンダリング時に、[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) プロパティを利用して既存のセルや画像などの [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) と **Bound** をキャプチャします。drawObject タイプが Cell の場合、その Bound と StringValue が表示されます。drawObject タイプが Image の場合、その Bound と Shape 名が表示されます。詳細については、以下のサンプルコードのコンソール出力をご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **コンソール出力**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
