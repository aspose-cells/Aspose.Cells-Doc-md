---
title: PdfSaveOptions と ImageOrPrintOptions の DefaultFont プロパティを優先するように設定する
type: docs
weight: 30
url: /ja/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **考えられる使用シナリオ**

を設定しながら**デフォルトフォント**のプロパティ[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)、PDFまたは画像に保存するとそれが設定されると予想するかもしれません**デフォルトフォント**不足している (インストールされていない) フォントを持つブック内のすべてのテキストに。

通常、PDF またはイメージに保存する場合、Aspose.Cells は最初に Workbook のデフォルト フォントを設定しようとします (つまり、[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ）。ワークブックの既定のフォントでもテキストを適切に表示/レンダリングできない場合、Aspose.Cells は言及されたフォントでレンダリングを試みます。**デフォルトフォント**の属性[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

あなたの期待に応えるために、「」という名前のブール型プロパティがあります。**CheckWorkbookDefaultFont** " の[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) false に設定して、ワークブックの既定のフォントの試行を無効にするか、**デフォルトフォント**で設定[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)優先すること。

## **PdfSaveOptions/ImageOrPrintOptions の DefaultFont プロパティを設定します**

次のサンプル コードは、Excel ファイルを開きます。 A1 セル (最初のワークシート内) には、"Christmas Time Font text" に設定されたテキストがあります。マシンにインストールされていないフォント名は「Christmas Time Personal Use」です。設定しました**デフォルトフォント**の属性[**PDF保存オプション**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)「タイムズニューローマン」へ。私たちも設定しました**CheckWorkbookDefaultFont**" へのブール値プロパティ**間違い**" これにより、A1 セルのテキストが "Times New Roman" フォントでレンダリングされ、ワークブックの既定のフォント (この場合は "Calibri") を使用しないことが保証されます。最終的に PDF ファイル形式にレンダリングされます。

{{% alert color="primary" %}}

のデフォルト値***CheckWorkbookDefaultFont***属性は**真実**.

{{% /alert %}}

これはのスクリーンショットです[テンプレートファイル](49446914.xlsx)サンプルコードで使用されます。

![todo:画像_代替_文章](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

これは、設定後の出力 PNG 画像です。[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)「Times New Roman」へのプロパティ。

![todo:画像_代替_文章](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

出力を見る[TIFF](out1_imageTIFF.tiff)設定後のイメージ[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)「Times New Roman」へのプロパティ。

出力を見る[PDF](out1_pdf.pdf)設定後のファイル[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)「Times New Roman」へのプロパティ。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
