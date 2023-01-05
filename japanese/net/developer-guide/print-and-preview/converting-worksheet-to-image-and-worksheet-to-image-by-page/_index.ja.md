---
title: ワークシートから画像へ、ワークシートから画像へのページ単位での変換
type: docs
weight: 80
url: /ja/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

このドキュメントは、開発者がワークシートを画像ファイルに変換する方法と、複数ページのワークシートをページごとに画像ファイルに変換する方法を詳細に理解できるように設計されています。

たとえば、ワークシートをアプリケーションや Web ページで使用するために、ワークシートを画像として表示する必要がある場合があります。画像を Word 文書、PDF ファイル、PowerPoint プレゼンテーションに挿入したり、他のシナリオで使用したりする必要がある場合があります。単純に、ワークシートを画像としてレンダリングしたいだけです。 Aspose.Cells は、Microsoft Excel ファイルのワークシートを画像に変換することをサポートしています。また、Aspose.Cells は、ワークブックを複数の画像ファイル (ページごとに 1 つ) に変換することをサポートしています。

Office オートメーションを使用してこれを実現することもできますが、Office オートメーションには独自の欠点があります。関連するいくつかの理由と問題があります。たとえば、セキュリティ、安定性、スケーラビリティ/速度、価格、および機能です。要するに、多くの理由がありますが、主な理由は、Microsoft 自身が Office オートメーションを強く推奨していないことです。

{{% /alert %}}

## **Aspose.Cells を使用してワークシートを画像ファイルに変換する**

この記事では、Aspose.Cells API.

をインポートする必要があります[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)名前空間をプログラム/プロジェクトに追加します。次のようないくつかの貴重なクラスがあります。[**シートレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)、 等々。の[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスは、ワークシートの画像をレンダリングするためのワークシートを表し、オーバーロードされた[**イメージへ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)任意の属性またはオプション セットを使用して、ワークシートを画像ファイルに直接変換できるメソッド。 System.Drawing.Bitmap オブジェクトを返すことができ、画像ファイルをディスク/ストリームに保存できます。 BMP、PNG、GIF、JPG、JPEG、TIFF、EMF など、いくつかの画像形式がサポートされています。

この記事では、次の方法について説明します。

- ワークシートを画像に変換する
- ワークシートのすべてのページを画像に変換する

このタスクでは、Aspose.Cells を使用してワークシートをテンプレート ワークブックからイメージ ファイルに変換する方法を示します。

### **プロジェクトのセットアップ**

1. 初め、[ダウンロード Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. 開発用コンピューターにインストールします。全て[Aspose](http://www.aspose.com/)コンポーネントがインストールされると、評価モードで動作します。評価モードには時間制限がなく、生成されたドキュメントに透かしを挿入するだけです。 Visual Studio.Net を起動し、新しいコンソール アプリケーションを作成します。この例では C# コンソール アプリケーションを使用していますが、VB.NET も使用できます。作成したプロジェクトに Aspose.Cells への参照を追加します。

### **ワークシートを画像ファイルに変換**

Microsoft Excel で新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。**テストブック.xlsx** (1 ワークシート)。次に、テンプレート ファイルのワークシート Sheet1 を SheetImage.jpg という画像ファイルに変換します。

以下は、タスクを実行するためにコンポーネントによって使用されるコードです。 Sheet1 を変換します**テストブック.xlsx**この変換がいかに簡単かを説明するために、画像ファイルに変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Aspose.Cells を使用してワークシートをページごとに画像ファイルに変換する**

この例では、Aspose.Cells を使用して、複数ページのテンプレート ワークブックからワークシートをページごとに 1 つのイメージ ファイルに変換する方法を示します。

### **ワークシートをページごとに画像に変換**

Microsoft Excel で新しいワークブックを作成し、最初のワークシートにいくつかのデータを追加しました。**Testbook2.xlsx** (1 ワークシート)。

次に、テンプレート ファイルのワークシート Sheet1 を画像ファイルに変換します (1 ページに 1 ファイル)。コピー タスクを実行するためのコンソール アプリケーションを既に作成しているので、それらのコンソール アプリケーションの作成手順をスキップして、ワークシートの変換手順に直接移動します。

以下は、タスクを実行するためにコンポーネントによって使用されるコードです。 Testbook2.xls の Sheet1 をページ単位で画像ファイルに変換します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

