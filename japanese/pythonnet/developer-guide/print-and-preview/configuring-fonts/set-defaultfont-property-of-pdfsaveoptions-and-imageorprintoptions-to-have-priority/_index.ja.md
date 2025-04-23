---
title: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能な使用シナリオ**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) および [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) の **DefaultFont** プロパティを設定する際には、フォントが見つからない（インストールされていない）場合に、ワークブック全体のテキストにそのDefaultFontを設定すると期待されるかもしれません。

一般的に、PDFや画像への保存時に、Aspose.Cells for Python via .NETはまずWorkbookのデフォルトフォント（つまり、Workbook.DefaultStyle.Font）を設定しようとします。もしWorkbookのデフォルトフォントが適切に表示・レンダリングできない場合、Aspose.Cells for Python via .NETは、 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)内のDefaultFont属性に記載されたフォントを使ってレンダリングを試みます。

ご期待に応えるため、[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)に"**check_workbook_default_font**"というBoolean型のプロパティを用意しています。これを**false**に設定すると、Workbookのデフォルトフォントの使用を無効にし、または、[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)の**default_font**設定を優先させることができます。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

以下のサンプルコードはExcelファイルを開きます。最初のワークシートのA1セルには"Christmas Time Font text"というテキストが設定されています。このフォント名は"Christmas Time Personal Use"ですが、これはインストールされていません。[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)の***default_font***属性を"Times New Roman"に設定し、**check_workbook_default_font**のBooleanプロパティを**"false"**に設定しています。これにより、A1セルのテキストは"Times New Roman"フォントでレンダリングされ、ワークブックのデフォルトフォント（この場合"Calibri"）は使用されません。コードは最初のワークシートをPNGとTIFF画像形式にレンダリングし、最終的にPDFファイルに出力します。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** 属性のデフォルト値は **true** です。

{{% /alert %}}

これは、例コードで使用されている [テンプレートファイル](49446913.xlsx)のスクリーンショットです。

![todo:image_alt_text](1.png)

これは、**DefaultFont** プロパティを "Times New Roman" に設定した後の出力PNGイメージです。

![todo:image_alt_text](2.png)

"Times New Roman" に[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) プロパティを設定した後の出力 [TIFF](48496672.tiff) 画像をご覧ください。

"Times New Roman" に[**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) プロパティを設定した後の出力 [PDF](48496673.pdf) ファイルをご覧ください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

