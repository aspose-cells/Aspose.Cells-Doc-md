---
title: ワークシートを異なる画像形式に変換
type: docs
weight: 90
url: /ja/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ブックからワークシートをエクスポートして異なる画像形式に変換することができます。 この記事では、ワークシートを異なる画像形式に変換する方法について説明します。

{{% /alert %}}

## **ワークシートをイメージに変換**

ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。例えば、アプリケーションやWebページでワークシートの画像を利用したい場合です。Microsoft Word文書やPDFファイル、PowerPointプレゼンテーション、その他のドキュメントに画像を挿入したい場合です。要するに、ワークシートを画像にレンダリングして、他の場所で利用したいということです。

 Aspose.CellsはExcelワークシートを画像に変換する機能をサポートしています。この機能を使用するには、プログラムまたはプロジェクトに [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) 名前空間をインポートする必要があります。レンダリングと印刷に役立つさまざまなクラスがあります。例えば、[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) 等です。

`Aspose.Cells.Rendering.ISheetRender`クラスは、画像としてレンダリングするシートを表します。オーバーロードされたメソッド [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) を使用して、シートを異なる属性やオプションで画像ファイルに変換できます。対応する画像フォーマットには BMP、PNG、GIF、JPG、JPEG、TIFF、EMF があります。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。

### **PNGフォーマット**

次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力PNGイメージ](67338401.zip)をご覧ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **TIFFフォーマット**

次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力TIFFイメージ](67338419.zip)をご覧ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **ワークシートをSVGに変換**

SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

バージョン24.12.0以降、Aspose.Cells for Go via C++はシートをSVG画像に変換できるようになっています。

この機能を使用するには、プログラムまたはプロジェクトに`Aspose.Cells.Rendering`名前空間をインポートする必要があります。 レンダリングと印刷用の価値あるクラスが含まれており、例えば`ISheetRender`、`IImageOrPrintOptions`などがあります。

`Aspose.Cells.Rendering.IImageOrPrintOptions`クラスは、ワークシートをSVG形式で保存することを指定します。 次のコードスニペットは、ExcelファイルのワークシートをSVGイメージファイルに変換する方法を示しています。

次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力SVGイメージ](67338403.zip)をご覧ください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
