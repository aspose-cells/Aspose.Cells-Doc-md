---
title: Aspose.Cells でワークシートを画像に変換する
type: docs
weight: 20
url: /ja/net/converting-worksheet-to-image-in-aspose-cells/
---
このドキュメントは、ワークシートを画像ファイルに変換する方法と、複数のページを含むワークシートをページごとに画像ファイルに変換する方法について、開発者が詳細に理解できるようにすることを目的としています。
たとえば、ワークシートをアプリケーションや Web ページで使用するために、ワークシートを画像として表示する必要がある場合があります。画像を Word 文書に挿入する必要がある場合があります。**PDF**ファイル、PowerPoint プレゼンテーション、または他のシナリオでそれらを使用します。単純に、ワークシートを画像としてレンダリングしたいだけです。 Aspose.Cells は、Microsoft Excel ファイルのワークシートを画像に変換することをサポートしています。また、**Aspose.Cells**ワークブックを複数の画像ファイル (ページごとに 1 つ) に変換することをサポートしています。

Office オートメーションを使用してこれを実現することもできますが、Office オートメーションには独自の欠点があります。関連するいくつかの理由と問題があります。たとえば、セキュリティ、安定性、スケーラビリティ/速度、価格、および機能です。要するに、多くの理由がありますが、主な理由は、Microsoft 自身が Office オートメーションを強く推奨していないことです。

この記事では、Aspose.Cells API を使用して数行の最も単純なコード行を使用して、Visual Studio.Net でコンソール アプリケーションを作成し、ワークシートを画像に変換し、ワークシートを各ワークシートの 1 つの画像に変換する方法を示します。Aspose.Cells をインポートする必要があります。名前空間をプログラム/プロジェクトに追加します。たとえば、SheetRender、ImageOrPrintOptions、WorkbookRender など、いくつかの価値のあるクラスがあります。**イメージへ**ワークシートを、必要な属性またはオプションで指定された画像ファイルに直接変換できるメソッド。それは戻ることができます**System.Drawing.Bitmap**オブジェクトであり、画像ファイルをディスク/ストリームに保存できます。 .bmp、.png、.gif、.jpg、.jpeg、.tiff、.emf など、いくつかの画像フォーマットがサポートされています。

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
