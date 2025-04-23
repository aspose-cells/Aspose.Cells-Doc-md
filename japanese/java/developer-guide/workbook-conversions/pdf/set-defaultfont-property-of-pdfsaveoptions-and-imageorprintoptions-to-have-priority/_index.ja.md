---
title: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能な使用シナリオ**

**DefaultFont** プロパティを **[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)** および **[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** に設定する際、インストールされていないフォントを持つワークブック内のすべてのテキストにその **DefaultFont** を設定することが期待されます。

一般に、PDFや画像に保存する場合、Aspose.Cellsは最初にワークブックのデフォルトフォント（例：[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)）を設定しようとします。ワークブックのデフォルトフォントでもテキストが正しく表示/レンダリングできない場合、Aspose.Cellsは[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)の**DefaultFont**属性に記載されたフォントでレンダリングを試みます。

あなたの期待に応えるために、[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) には "**CheckWorkbookDefaultFont**" というブール型のプロパティがあります。これをfalseに設定すると、ワークブックのデフォルトフォントを試みないようにすることができます。または、**[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** の **DefaultFont** 設定が優先されるようにすることができます。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

以下のサンプルコードは、Excelファイルを開きます。 A1セル（最初のワークシートの）には、"クリスマス・タイム文字"というテキストが設定されています。フォント名は、マシンにインストールされていない"Christmas Time Personal Use"です。**DefaultFont**属性を [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) に "Times New Roman" に設定します。また、**CheckWorkbookDefaultFont** ブール型プロパティを "**false**" に設定することで、A1セルのテキストが "Times New Roman" フォントでレンダリングされ、ワークブックのデフォルトフォント（この場合は"Calibri"）を使用しないことを保証します。コードは最初のワークシートをPNGおよびTIFFイメージ形式にレンダリングし、最終的にPDFファイル形式にレンダリングします。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** 属性のデフォルト値は **true** です。

{{% /alert %}}

これは、例コードで使用される [テンプレートファイル](49446914.xlsx) のスクリーンショットです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

これは、**DefaultFont** プロパティを "Times New Roman" に設定した後の出力PNGイメージです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

"Times New Roman"を[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)プロパティに設定した後の[TIFF](out1_imageTIFF.tiff)イメージを参照してください。

"Times New Roman"を[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) プロパティに設定した後の[PDF](out1_pdf.pdf)ファイルを参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
