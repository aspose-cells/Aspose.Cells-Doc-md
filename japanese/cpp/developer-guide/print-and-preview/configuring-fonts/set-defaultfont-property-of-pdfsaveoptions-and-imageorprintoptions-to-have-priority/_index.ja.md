---
title: PdfSaveOptionsとImageOrPrintOptionsのDefaultFontプロパティをC++で優先的に設定する方法
linktitle: PdfSaveOptionsおよびImageOrPrintOptionsのDefaultFontプロパティを設定し、優先度を持たせます。
type: docs
weight: 30
url: /ja/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aspose.CellsをC++で使用して文書保存時のフォント設定の優先順位を学びます。
---

## **可能な使用シナリオ**

[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) および [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) の **DefaultFont** プロパティを設定する際には、フォントが見つからない（インストールされていない）場合に、ワークブック全体のテキストにそのDefaultFontを設定すると期待されるかもしれません。

一般に、PDFまたは画像に保存する場合、Aspose.CellsはまずWorkbookのデフォルトフォント（つまりWorkbook.DefaultStyle.Font）を設定しようとします。Workbookのデフォルトフォントが適切に表示/レンダリングできない場合、Aspose.Cellsは[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)内のDefaultFont属性に記載されているフォントでレンダリングしようとします。

あなたの期待に応えるために、[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)には"**CheckWorkbookDefaultFont**"というブール型のプロパティがあり、これを**false**に設定すればWorkbookのデフォルトフォントを試みる動作を無効にできます。また、[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)の**DefaultFont**設定に優先順位を付けることも可能です。

## **PdfSaveOptions/ImageOrPrintOptionsのDefaultFontプロパティを設定します**

次のサンプルコードはExcelファイルを開きます。最初のシートのセルA1には"Christmas Time Font text"というテキストが設定されており、フォント名は"Christmas Time Personal Use"ですが、これはインストールされていません。[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)の**DefaultFont**属性を"Times New Roman"に設定し、**CheckWorkbookDefaultFont**ブール型プロパティを**"false"**に設定することで、A1セルのテキストを"Times New Roman"フォントでレンダリングし、Workbookのデフォルトフォント（"Calibri"）を使用しないようにします。このコードは最初のシートをPNGとTIFF画像フォーマットにレンダリングし、最後にPDFに出力します。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性のデフォルト値は**true**です。

{{% /alert %}}

これは、例コードで使用されている [テンプレートファイル](49446913.xlsx)のスクリーンショットです。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)プロパティを"Times New Roman"に設定した後の出力PNG画像例です。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)プロパティを"Times New Roman"に設定した後の出力[TIF](48496672.tiff)画像を確認してください。

{0}プロパティを"Times New Roman""に設定した後の出力[PFD](48496673.pdf)を確認してください。

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
