---
title: ワークシートを画像に変換し、ページごとにワークシートを画像に変換
type: docs
weight: 80
url: /ja/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

このドキュメントは、開発者に、ワークシートを画像ファイルに変換する方法と、複数のページを持つワークシートを1ページごとに画像ファイルに変換する方法についての詳細な理解を提供するように設計されています。

時には、アプリケーションやWebページでワークシートを画像として表示する必要があります。たとえば、その画像をWord文書、PDFファイル、PowerPointプレゼンテーションに挿入したり、他のシナリオで使用する必要があるかもしれません。単純に言えば、ワークシートを画像としてレンダリングしたいと思います。Aspose.Cellsは、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cellsは、ワークブックを複数のページごとに1つの画像ファイルに変換することもサポートしています。

これを達成するためには、Office Automationを使用することができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性/処理速度、価格、機能など、いくつかの理由や問題があります。簡単に言えば、多くの理由がありますが、その中でも主な理由の1つは、Microsoft自体がOffice Automationを強く推奨していないことです。

{{% /alert %}}

## **Aspose.Cellsを使用してワークシートを画像ファイルに変換する方法**

この記事では、Visual Studioでコンソールアプリケーションを作成し、Aspose.Cells APIを使用してわずか数行のコードでワークシートを画像に変換し、複数のページを持つワークシートを1つの画像に変換する方法を示します。

プログラム/プロジェクトに[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)ネームスペースをインポートする必要があります。[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)などの貴重なクラスがいくつか含まれています。[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスは、ワークシートをレンダリングするためのクラスであり、オーバーロードされた[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)メソッドから直接ワークシートを画像ファイルに変換できます。System.Drawing.Bitmapオブジェクトを返し、イメージファイルをディスク/ストリームに保存できます。省略して、BMP、PNG、GIF、JPG、JPEG、TIFF、EMFなど、さまざまな画像形式がサポートされています。

この記事では以下の方法について説明します:

- ワークシートを画像に変換する
- ワークシートの各ページを画像に変換する

このタスクでは、Aspose.Cellsを使用して、テンプレートワークブックからワークシートを画像ファイルに変換する方法を示します。

### **プロジェクトのセットアップ**

1. まず、[Aspose.Cells for .NETをダウンロードして](https://downloads.aspose.com/cells/net)ください。
1. 開発コンピュータにインストールしてください。Asposeのすべてのコンポーネントは、インストールされると評価モードで動作します。評価モードには時間制限はなく、生成された文書にウォーターマークが注入されます。Visual Studio.Netを起動し、新しいコンソールアプリケーションを作成します。この例ではC#のコンソールアプリケーションを使用していますが、VB.NETも使用できます。作成したプロジェクトにAspose.Cellsへの参照を追加してください。

### **ワークシートを画像ファイルに変換**

Microsoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました：**Testbook.xlsx**（1つのワークシート）。次に、テンプレートファイルのワークシートSheet1をSheetImage.jpgという画像ファイルに変換します。

コンポーネントがタスクを達成するために使用したコードは以下の通りです。**Testbook.xlsx**のSheet1を画像ファイルに変換し、この変換がどれほど簡単であるかを説明します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Aspose.Cellsを使用して、ワークシートを画像ファイルにページごとに変換する**

この例では、Aspose.Cellsを使用して、複数のページを持つテンプレートワークブックからワークシートを1つの画像ファイルに変換する方法を示します。

### **ワークシートをページ毎に画像に変換する**

私はMicrosoft Excelで新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました: **Testbook2.xlsx** (1 ワークシート)。

これで、テンプレートファイルのワークシート Sheet1 を画像ファイルに変換します（1ページごとのファイル）。すでにコンソールアプリケーションを作成してコピー作業を行う準備ができているため、コンソールアプリケーションの作成手順をスキップして、直接ワークシートの変換手順に移ります。

以下は、そのコンポーネントがタスクを達成するために使用したコードです。それは Testbook2.xls の Sheet1 をページごとに画像ファイルに変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
