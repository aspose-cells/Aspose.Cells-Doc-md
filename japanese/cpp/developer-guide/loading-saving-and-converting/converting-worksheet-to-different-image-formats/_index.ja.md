---
title: ワークシートを別の画像形式に変換する
type: docs
weight: 90
url: /ja/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ワークブックからワークシートをエクスポートして、別の画像形式に変換できます。この記事では、ワークシートを別の画像形式に変換する方法について説明します。

{{% /alert %}} 
## **ワークシートを画像に変換する**
ワークシートには、分析するデータが含まれています。たとえば、ワークシートには、パラメーター、合計、パーセンテージ、例外、および計算を含めることができます。

開発者は、ワークシートを画像として表示する必要がある場合があります。たとえば、アプリケーションまたは Web ページでワークシートの画像を使用する必要がある場合があります。 Microsoft Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他の文書タイプに画像を挿入したい場合があります。簡単に言えば、別の場所で使用できるように、ワークシートを画像としてレンダリングする必要があります。

Aspose.Cells は、Excel ワークシートの画像への変換をサポートしています。この機能を使用するには、インポートする必要があります[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)名前空間をプログラムまたはプロジェクトに追加します。レンダリングと印刷に役立ついくつかのクラスがあります。たとえば、[ISheetRender](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrintOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)その他。

`Aspose.Cells.Rendering.ISheetRender` クラスは、画像としてレンダリングするワークシートを表します。オーバーロードされたメソッドがあり、[イメージへ](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5)、さまざまな属性またはオプションを使用してワークシートを画像ファイルに変換できます。 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF など、いくつかの画像形式がサポートされています。

次のコード スニペットは、Excel ファイルのワークシートを画像ファイルに変換する方法を示しています。
### **PNG形式**
次のサンプル コードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力PNG画像](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **TIFF形式**
次のサンプル コードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力TIFF画像](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **ワークシートを SVG に変換する**
SVG はスケーラブル ベクター グラフィックスの略です。 SVG は、2 次元ベクター グラフィックスの XML 標準に基づく仕様です。これは、1999 年から World Wide Web Consortium (W3C) によって開発されているオープン標準です。

Aspose.Cells for C++ は、バージョン 18.5.0 からワークシートを SVG 画像に変換できるようになりました。

この機能を使用するには、`Aspose.Cells.Rendering` 名前空間をプログラムまたはプロジェクトにインポートします。 `ISheetRender`、`IImageOrPrintOptions` など、レンダリングと印刷に役立つクラスがいくつかあります。

`Aspose.Cells.Rendering.IImageOrPrintOptions` クラスは、ワークシートが SVG 形式で保存されることを指定します。次のコード スニペットは、Excel ファイルのワークシートを SVG イメージ ファイルに変換する方法を示しています。

次のサンプル コードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力SVG画像](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}
