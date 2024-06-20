---
title: DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject および Bound を取得
type: docs
weight: 70
url: /ja/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **可能な使用シナリオ**

Aspose.Cellsは、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)抽象クラスを提供しており、[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)メソッドがあります。ユーザーは[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)を実装し、ExcelをPDFや画像にレンダリングする際に[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)メソッドを利用して[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)とバウンドを取得できます。以下に、[**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)メソッドのパラメータの簡単な説明を示します。

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)は初期化され、レンダリング時に返されます

- x: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) の左端

- y: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) の上端

- width: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) の幅

- height: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) の高さ

ExcelファイルをPDFにレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)クラスと[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)と組み合わせて使用できます。同様に、Excelファイルをイメージにレンダリングする場合は、[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)クラスと[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler)と組み合わせて使用できます。

## **DrawObjectEventHandler クラスを使用して PDF にレンダリングする際の DrawObject と Bound を取得**

以下のサンプルコードをご覧ください。[サンプルExcelファイル](64716821.xlsx)をロードし、[出力PDF](64716822.pdf)として保存します。PDFにレンダリングする際に、[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)プロパティを使用し、既存のセルやオブジェクト（画像など）の[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)とバウンドをキャプチャします。もし[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)タイプがセルであれば、そのバウンドとStringValueを出力します。そしてもし[**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)タイプが画像であれば、そのバウンドとシェイプ名を出力します。下記のサンプルコードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **コンソール出力**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
