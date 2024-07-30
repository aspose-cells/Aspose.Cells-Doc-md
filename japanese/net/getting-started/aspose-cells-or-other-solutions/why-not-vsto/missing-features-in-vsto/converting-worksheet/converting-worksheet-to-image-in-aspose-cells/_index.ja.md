---
title: Aspose.Cellsでワークシートを画像に変換する
type: docs
weight: 20
url: /ja/net/converting-worksheet-to-image-in-aspose-cells/
---

このドキュメントは、ワークシートを画像ファイルに変換する方法について、詳細な理解を開発者に提供するよう設計されています。また、ワークシートをページごとの画像ファイルに変換する方法も説明しています。
時々、アプリケーションやウェブページで使用するためにワークシートを画像として表示する必要があります。画像をワードドキュメント、**PDF**ファイル、パワーポイントプレゼンテーションに挿入したり、他のシナリオで使用したりする必要があります。単純に言えば、ワークシートを画像としてレンダリングしたいということです。Aspose.Cellsは、Microsoft Excelファイルのワークシートを画像に変換することをサポートしています。また、**Aspose.Cells**は、ワークブックを複数の画像ファイルに変換することもサポートしています。

これを達成するためには、Office Automationを使用することができますが、Office Automationには独自の欠点があります。セキュリティ、安定性、拡張性/処理速度、価格、機能など、いくつかの理由や問題があります。簡単に言えば、多くの理由がありますが、その中でも主な理由の1つは、Microsoft自体がOffice Automationを強く推奨していないことです。

この記事では、Visual Studio.Netでコンソールアプリケーションを作成し、Aspose.Cells APIを使用して少数のコード行でワークシートを画像に変換し、ワークブックをワークシートごとに1枚の画像に変換する方法を示しています。プログラム/プロジェクトにAspose.Cells.Rendering名前空間をインポートする必要があります。SheetRender、ImageOrPrintOptions、WorkbookRenderなど、いくつかの貴重なクラスが含まれています。Aspose.Cells.Rendering.SheetRenderクラスは、ワークシートの画像をレンダリングするためのクラスであり、ワークシートを画像ファイルに直接変換する**ToImage**メソッドがオーバーロードされており、希望する属性やオプションで指定された画像ファイル（複数可）に変換することができます。System.Drawing.Bitmap**オブジェクトを返し、画像ファイルをディスク/ストリームに保存することができます。.bmp、.png、.gif、.jpg、.jpeg、.tiff、.emfなど、いくつかの画像形式がサポートされています。

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
