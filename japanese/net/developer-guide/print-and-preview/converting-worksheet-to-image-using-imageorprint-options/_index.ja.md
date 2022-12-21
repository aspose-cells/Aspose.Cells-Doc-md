---
title: ImageOrPrint オプションを使用してワークシートを画像に変換する
type: docs
weight: 90
url: /ja/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

このドキュメントは、ワークシートを画像ファイルに変換し、画像にさまざまな画像と印刷オプション、解像度、TIFF 圧縮、画像形式、ページ品質などのオプションを適用する方法を詳細に理解できるように設計されています。

{{% /alert %}}

## **ワークシートを画像に保存する - さまざまなアプローチ**

場合によっては、ワークシートを絵で表したものとして提示する必要がある場合があります。ワークシート イメージをアプリケーションまたは Web ページに表示する必要があります。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。他の場所で使用できるように、ワークシートを画像としてレンダリングしたいだけです。 Aspose.Cells は、Excel ファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cells は、画像形式、解像度 (縦と横の両方)、画質、その他の画像および印刷オプションなど、さまざまなオプションの設定をサポートしています。

Office オートメーションを試すこともできますが、Office オートメーションには独自の欠点があります。関連する理由と問題はいくつかあります。たとえば、セキュリティ、安定性、スケーラビリティと速度、価格、機能などです。簡単に言えば、多くの理由がありますが、一番の理由は、Microsoft 自身がソフトウェア ソリューションによる Office オートメーションを強く推奨していないことです。

この記事では、Visual Studio .NET でコンソール アプリケーションを作成し、Aspose.Cells API.

インポートする必要があります[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)名前空間をプログラム/プロジェクトに追加します。いくつかの貴重なクラスがあります。たとえば、[**シートレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)等

の[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスは、ワークシートの画像をレンダリングするためのワークシートを表し、オーバーロードされた[**イメージへ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)ワークシートを、必要な属性またはオプションで指定された画像ファイルに直接変換できるメソッド。 System.Drawing.Bitmap オブジェクトを返すことができ、イメージ ファイルをディスク/ストリームに保存できます。 BMP、PNG、GIFF、JPEG、TIFF、EMF など、いくつかの画像フォーマットがサポートされています。

## **Aspose.Cells を使用して、ImageOrPrint オプションを使用してワークシートを画像に変換します。**

### **Microsoft Excel でテンプレート ブックを作成する**

MS Excel で新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。ここで、テンプレート ファイルのワークシート「Sheet1」を画像ファイル「SheetImage.tiff」に変換し、水平解像度と垂直解像度、TiffCompression などのさまざまな画像オプションを適用します。

### **Aspose.Cells をダウンロードしてインストールします**

まず、あなたがする必要があります[ダウンロード](https://downloads.aspose.com/cells/net).Net の場合は Aspose.Cells。開発用コンピューターにインストールします。全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。

### **プロジェクトを作成する**

Visual Studio を起動します。ネットして、新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを示していますが、VB.NET も使用できます。

### **参照を追加**

このプロジェクトは Aspose.Cells を使用します。そのため、プロジェクトに Aspose.Cells コンポーネントへの参照を追加する必要があります。たとえば、….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll への参照を追加します。

### **ワークシートを画像ファイルに変換する**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **変換オプション**

特定のページを画像として保存することができます。次のコードは、ワークブックの 1 番目と 2 番目のワークシートを JPG 画像に変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **WorkbookRender を使用した画像変換**

ワークブックを循環して、その中の各ワークシートを個別の画像にレンダリングできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

