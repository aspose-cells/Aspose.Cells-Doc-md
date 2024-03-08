---
title: ワークシートを別の画像形式に変換する
type: docs
weight: 90
url: /ja/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells を使用すると、ワークブックからワークシートをエクスポートし、異なる画像形式に変換できます。この記事では、ワークシートをさまざまな画像形式に変換する方法について説明します。

{{% /alert %}} 
##  **ワークシートを画像に変換する**
ワークシートには、分析するデータが含まれています。たとえば、ワークシートにはパラメータ、合計、パーセンテージ、例外、計算を含めることができます。

開発者は、ワークシートを画像として表示する必要がある場合があります。たとえば、アプリケーションまたは Web ページでワークシートの画像を使用する必要がある場合があります。 Microsoft Word 文書、PDF ファイル、PowerPoint プレゼンテーション、またはその他の文書タイプに画像を挿入することができます。簡単に言うと、ワークシートを画像としてレンダリングして、他の場所で使用できるようにしたいと考えます。

Aspose.Cells は、Excel ワークシートの画像への変換をサポートしています。この機能を使用するには、[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)名前空間をプログラムまたはプロジェクトに追加します。これには、レンダリングと印刷のためのいくつかの貴重なクラスがあります。たとえば、[シートレンダリング](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [画像または印刷オプション](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)その他。

`Aspose.Cells.Rendering.ISheetRender` クラスは、画像としてレンダリングするワークシートを表します。オーバーロードされたメソッドがあり、[画像へ](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)、ワークシートをさまざまな属性またはオプションを持つ画像ファイルに変換できます。いくつかの画像形式がサポートされています (例: BMP、PNG、GIF、JPG、JPEG、TIFF、EMF)。

次のコード スニペットは、Excel ファイル内のワークシートを画像ファイルに変換する方法を示しています。
###  **PNG フォーマット**
次のサンプルコードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力 PNG 画像](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

###  **TIFF フォーマット**
次のサンプルコードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力 TIFF 画像](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

##  **ワークシートをSVGに変換中**
SVG はスケーラブル ベクター グラフィックスの略です。 SVG は、2 次元ベクトル グラフィックスの XML 標準に基づいた仕様です。これは、World Wide Web Consortium (W3C) によって 1999 年から開発が進められているオープン標準です。

Aspose.Cells for C++ は、バージョン 18.5.0 以降、ワークシートを SVG 画像に変換できるようになりました。

この機能を使用するには、`Aspose.Cells.Rendering` 名前空間をプログラムまたはプロジェクトにインポートします。これには、レンダリングと印刷のためのいくつかの貴重なクラス (`ISheetRender`、`IImageOrPrintOptions` など) があります。

`Aspose.Cells.Rendering.IImageOrPrintOptions` クラスは、ワークシートが SVG 形式で保存されることを指定します。次のコード スニペットは、Excel ファイル内のワークシートを SVG 画像ファイルに変換する方法を示しています。

次のサンプルコードを参照してください。[サンプル Excel ファイル](67338402.xlsx)、 そしてその[出力 SVG 画像](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
