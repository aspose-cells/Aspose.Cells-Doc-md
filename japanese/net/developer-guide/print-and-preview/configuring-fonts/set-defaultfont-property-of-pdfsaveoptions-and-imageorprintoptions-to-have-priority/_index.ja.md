---
title: PdfSaveOptions と ImageOrPrintOptions の DefaultFont プロパティを優先するように設定する
type: docs
weight: 30
url: /ja/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **考えられる使用シナリオ**

を設定しながら**デフォルトフォント**のプロパティ**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**と**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**、PDF または画像に保存すると、その DefaultFont が、不足している (インストールされていない) フォントを持つブック内のすべてのテキストに設定されると予想される場合があります。

通常、PDF または画像に保存する場合、Aspose.Cells は最初に Workbook のデフォルト フォント (Workbook.DefaultStyle.Font) を設定しようとします。ワークブックの既定のフォントでもテキストを適切に表示/レンダリングできない場合、Aspose.Cells は DefaultFont 属性に対して指定されたフォントでレンダリングを試みます。**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**.

あなたの期待に応えるために、「」という名前のブール型プロパティがあります。**CheckWorkbookDefaultFont** " の**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** .あなたはそれを設定することができます**間違い**ワークブックのデフォルト フォントの試行を無効にするか、**デフォルトフォント**で設定**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**優先すること。

## **PdfSaveOptions/ImageOrPrintOptions の DefaultFont プロパティを設定します**

次のサンプル コードは、Excel ファイルを開きます。 A1 セル (最初のワークシート内) には、"Christmas Time Font text" に設定されたテキストがあります。マシンにインストールされていないフォント名は「Christmas Time Personal Use」です。設定しました***デフォルトフォント***の属性**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**「タイムズニューローマン」へ。私たちも設定しました**CheckWorkbookDefaultFont**ブール値のプロパティ**"間違い"**これにより、A1 セルのテキストが "Times New Roman" フォントでレンダリングされ、ワークブックの既定のフォント (この場合は "Calibri") を使用しないようになります。このコードは、最初のワークシートを PNG および TIFF 画像形式にレンダリングします。最終的に PDF ファイル形式にレンダリングされます。

{{% alert color="primary" %}}

のデフォルト値***CheckWorkbookDefaultFont***属性は**真実**.

{{% /alert %}}

これはのスクリーンショットです[テンプレートファイル](49446913.xlsx)サンプルコードで使用されます。

![todo:画像_代替_文章](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

これは、設定後の出力 PNG イメージです。**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**「Times New Roman」へのプロパティ。

![todo:画像_代替_文章](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

出力を見る[TIFF](48496672.tiff)設定後のイメージ**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**「Times New Roman」へのプロパティ。

出力を見る[PDF](48496673.pdf)設定後のファイル**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**「Times New Roman」へのプロパティ。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
