---
title: ImageOrPrint オプションを使用したワークシートの画像への変換
type: docs
weight: 90
url: /ja/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

このドキュメントは、ワークシートを画像ファイルに変換し、さまざまな画像とその画像の印刷オプション、解像度、TIFF 圧縮、画像形式、ページ品質などのオプションを適用する方法を詳細に理解できるように設計されています。

{{% /alert %}}

##  **ワークシートを画像に保存 - さまざまなアプローチ**

場合によっては、ワークシートを図で表現することが必要になる場合があります。ワークシートの画像をアプリケーションまたは Web ページに表示する必要はありません。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。ワークシートを画像としてレンダリングして、他の場所で使用できるようにしたいだけです。 Aspose.Cells は、Excel ファイルのワークシートの画像への変換をサポートしています。また、Aspose.Cells は、画像形式、解像度 (垂直方向と水平方向の両方)、画質、その他の画像および印刷オプションなどのさまざまなオプションの設定をサポートしています。

Office Automation を試してみることもできますが、Office Automation には独自の欠点があります。セキュリティ、安定性、拡張性と速度、価格、機能など、いくつかの理由と問題が関係しています。要するに、多くの理由がありますが、その最大の理由は、Microsoft 自身がソフトウェア ソリューションによる Office 自動化を強く推奨していることです。

この記事では、Visual Studio .NET でコンソール アプリケーションを作成し、Aspose.Cells API を使用した数行の最も単純なコードで、さまざまな画像と印刷オプションを使用してワークシートを画像に変換する方法を示します。

インポートする必要があります[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)名前空間をプログラム/プロジェクトに追加します。これには、いくつかの貴重なクラスがあります。たとえば、[**シートレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**画像または印刷オプション**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**ワークブックレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)等

の[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスはワークシートの画像をレンダリングするワークシートを表し、オーバーロードされた[**画像へ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)ワークシートを、希望の属性またはオプションで指定された画像ファイルに直接変換できるメソッド。 System.Drawing.Bitmap オブジェクトを返すことができ、画像ファイルをディスク/ストリームに保存することができます。サポートされている画像形式はいくつかあります (例: BMP、PNG、GIF、JPEG、TIFF、EMF など)。

##  **Aspose.Cells を使用して、ImageOrPrint オプションを使用してワークシートを画像に変換します。**

###  **Microsoft Excel でテンプレート ワークブックを作成する**

MS Excel で新しいワークブックを作成し、最初のワークシートにデータを追加しました。次に、テンプレート ファイルのワークシート「Sheet1」を画像ファイル「SheetImage.tiff」に変換し、水平解像度と垂直解像度、TiffCompression などのさまざまな画像オプションを適用します。

###  **ダウンロードしてインストール Aspose.Cells**

まず、次のことを行う必要があります。[ダウンロード](https://downloads.aspose.com/cells/net).Net の場合は Aspose.Cells。開発用コンピューターにインストールします。全て[Aspose](http://www.aspose.com/)コンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限がなく、作成されたドキュメントにウォーターマークが挿入されるだけです。

###  **プロジェクトを作成する**

Visual Studio を起動します。 Net を作成し、新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを示しますが、VB.NET も使用できます。

###  **参照の追加**

このプロジェクトは Aspose.Cells を使用します。そのため、プロジェクトに Aspose.Cells コンポーネントへの参照を追加する必要があります。たとえば、….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。

###  **ワークシートを画像ファイルに変換する**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **変換オプション**

特定のページを画像として保存することが可能です。次のコードは、ワークブック内の最初と 2 番目のワークシートを JPG 画像に変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **WorkbookRender を使用した画像変換**

TIFF 画像には複数のフレームを含めることができます。ワークブック全体を複数のフレームまたはページを含む 1 つの TIFF 画像に保存できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

