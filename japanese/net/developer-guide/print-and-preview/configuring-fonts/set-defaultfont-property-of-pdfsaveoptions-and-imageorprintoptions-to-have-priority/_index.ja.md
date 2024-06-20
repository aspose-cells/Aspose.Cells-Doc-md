---
title: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能な使用シナリオ**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) および [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) の **DefaultFont** プロパティを設定する際には、フォントが見つからない（インストールされていない）場合に、ワークブック全体のテキストにそのDefaultFontを設定すると期待されるかもしれません。

通常、PDFまたは画像に保存する際、Aspose.Cells はまずワークブックのデフォルトのフォント（すなわち、Workbook.DefaultStyle.Font ）を設定しようとします。ワークブックのデフォルトのフォントでもテキストを適切に表示/レンダリングできない場合は、[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)で指定されたDefaultFont属性で再度表示を試みます。

この期待に対処するために、[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) には "**CheckWorkbookDefaultFont**" というブール型のプロパティがあります。このプロパティを **false** に設定すると、ワークブックのデフォルトのフォントを試行しないようになり、また [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) のDefaultFont設定が優先されます。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

次のサンプルコードでは、Excelファイルを開きます。最初のワークシートのA1セルに"Christmas Time Font text"のテキストが設定されています。フォント名はマシンにインストールされていない"Christmas Time Personal Use"です。***DefaultFont***属性を[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)に"Times New Roman"に設定します。また、**CheckWorkbookDefaultFont** ブール型のプロパティを **"false"** に設定しており、A1セルのテキストが"Calibri"）ワークブックのデフォルトフォントを使用しないで"Times New Roman"フォントで表示され、PNGおよびTIFF画像形式にワークシートをレンダリングします。最終的には、PDFファイル形式にレンダリングします。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** 属性のデフォルト値は **true** です。

{{% /alert %}}

これは、例コードで使用されている [テンプレートファイル](49446913.xlsx)のスクリーンショットです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

これは、**DefaultFont** プロパティを "Times New Roman" に設定した後の出力PNGイメージです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

"Times New Roman" に[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/) プロパティを設定した後の出力 [TIFF](48496672.tiff) 画像をご覧ください。

"Times New Roman" に[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) プロパティを設定した後の出力 [PDF](48496673.pdf) ファイルをご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
