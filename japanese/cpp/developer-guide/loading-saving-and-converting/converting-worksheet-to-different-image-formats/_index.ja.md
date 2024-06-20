---
title: ワークシートを異なる画像形式に変換
type: docs
weight: 90
url: /ja/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cellsを使用すると、ブックからワークシートをエクスポートして異なる画像形式に変換することができます。 この記事では、ワークシートを異なる画像形式に変換する方法について説明します。

{{% /alert %}} 
## **ワークシートをイメージに変換**
ワークシートには分析したいデータが含まれています。 例えば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算などが含まれることがあります。

開発者として、ワークシートを画像として表示する必要があるかもしれません。 たとえば、ワークシートの画像をアプリケーションやWebページで使用する必要があるかもしれません。 Microsoft Word文書、PDFファイル、PowerPointプレゼンテーション、またはその他のドキュメントタイプに画像を挿入したいかもしれません。 要するに、ワークシートを他の場所で使用できるように画像として描画したいのです。

Aspose.CellsはExcelワークシートを画像に変換する機能をサポートしています。 この機能を使用するには、プログラムまたはプロジェクトに[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)名前空間をインポートする必要があります。 レンダリングと印刷用の価値あるクラスが含まれており、たとえば、[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)などがあります。

`Aspose.Cells.Rendering.ISheetRender`クラスは、画像としてレンダリングするワークシートを表します。 画像ファイルにワークシートを変換する[ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)などのオーバーロードされたメソッドがあり、BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなどのさまざまな画像形式がサポートされています。

次のコードスニペットは、Excelファイルのワークシートを画像ファイルに変換する方法を示しています。
### **PNGフォーマット**
次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力PNGイメージ](67338401.zip)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **TIFFフォーマット**
次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力TIFFイメージ](67338419.zip)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **ワークシートをSVGに変換**
SVGはScalable Vector Graphicsの略です。 SVGは、二次元ベクトルグラフィックのためのXML標準に基づいた仕様です。 1999年以来、World Wide Web Consortium（W3C）によって開発されてきたオープンな標準です。

バージョン18.5.0以降、Aspose.Cells for C++はワークシートをSVG画像に変換することができるようになりました。

この機能を使用するには、プログラムまたはプロジェクトに`Aspose.Cells.Rendering`名前空間をインポートする必要があります。 レンダリングと印刷用の価値あるクラスが含まれており、例えば`ISheetRender`、`IImageOrPrintOptions`などがあります。

`Aspose.Cells.Rendering.IImageOrPrintOptions`クラスは、ワークシートをSVG形式で保存することを指定します。 次のコードスニペットは、ExcelファイルのワークシートをSVGイメージファイルに変換する方法を示しています。

次のサンプルコードと、参照用の[サンプルExcelファイル](67338402.xlsx)、[出力SVGイメージ](67338403.zip)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
