---
title: ImageOrPrintオプションを使用してワークシートを画像に変換する
type: docs
weight: 90
url: /ja/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

このドキュメントは、ワークシートを画像ファイルに変換し、画像と印刷オプションを適用し、解像度、TIFF圧縮、画像形式、ページ品質などのオプションを適用する方法について詳しく説明します。

{{% /alert %}}

## **ワークシートをイメージとして保存する - 異なるアプローチ**

時々、ワークシートを図解的に表示する必要があります。ワークシートの画像をアプリケーションやWebページに挿入する必要があります。画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があります。別の場所で使用するためにワークシートを画像としてレンダリングしたいと思うだけです。Aspose.CellsはExcelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは画像形式、解像度（縦と横の両方）、画像品質、およびその他の画像および印刷オプションを設定することをサポートしています。

Office Automationを試すことができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性、速度、価格、機能など、いくつかの理由や問題があります。要するに、Microsoft自身もソフトウェアソリューションからのOffice Automationを強く勧めていません。

この記事は、Aspose.Cells APIを使用して、C#コンソールアプリケーションを作成し、わずかなコード行でさまざまなイメージと印刷オプションを使用してワークシートをイメージに変換する方法を示しています。

あなたはあなたのプログラム/プロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)名前空間をインポートする必要があります。例えば、[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)などの価値のあるクラスがいくつかあります。

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスは、イメージを描画するためのワークシートを表し、あなたが望む属性やオプションでワークシートをイメージファイルに直接変換できるオーバーロードされた[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)メソッドを持っています。それはSystem.Drawing.Bitmapオブジェクトを返すことができ、イメージファイルをディスク/ストリームに保存することができます。サポートされるイメージ形式はいくつかあります、例えばBMP、PNG、GIFF、JPEG、TIFF、EMFなどです。

## **ImageOrPrintオプションを使用して、Aspose.Cellsを使用してワークシートをイメージに変換する。**

### **Microsoft Excelでテンプレートワークブックを作成する**

私はMS Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。これで、テンプレートファイルのワークシート **Sheet1** を画像ファイル **SheetImage.tiff** に変換し、水平および垂直解像度、TiffCompressionなどの異なるイメージオプションを適用します。

### **Aspose.Cellsをダウンロードしてインストールする**

まず、.Net向けのAspose.Cellsを[ダウンロード](https://downloads.aspose.com/cells/net)します。開発コンピューターにインストールします。すべてのAsposeコンポーネントはインストールされると評価モードで動作します。評価モードには時限がなく、生成されたドキュメントにのみ透かしを挿入します。

### **プロジェクトを作成する**

Visual Studio .Netを起動して、新しいコンソールアプリケーションを作成します。この例ではC#コンソールアプリケーションを示しますが、VB.NETも使用できます。

### **参照の追加**

このプロジェクトではAspose.Cellsを使用します。そのため、プロジェクトにAspose.Cellsコンポーネントへの参照を追加する必要があります。例えば、….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dllに参照を追加します。

### **ワークシートを画像ファイルに変換**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **変換オプション**

特定のページを画像に保存することが可能です。次のコードは、ワークブック内の最初と2番目のワークシートをJPG画像に変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **WorkbookRenderを使用した画像変換**

TIFF画像には複数のフレームを含めることができます。複数フレームまたはページを持つTIFF画像としてワークブック全体を保存できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
