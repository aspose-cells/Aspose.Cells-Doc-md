---
title: Workbook Conversions
type: docs
weight: 65
url: /net/convert-workbook-to-different-formats/
aliases: [/net/rendering-and-printing/,/net/rendering/，/net/convert-excel-to-xps/,/net/convert-excel-to-pptx/,/net/convert-excel-to-docx/,/net/convert-excel-to-markdown/]
---

{{% alert color="primary" %}}

Aspose.Cells supports conversion between many formats. Technically, conversion means to load a workbook in one file format and save it into another.

{{% /alert %}}

## **Convert Excel to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Convert Excel to Image**
Aspose.Cells supports converting Excel files to images.
The code example below shows how to save a workbook as images.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PNG.cs" >}}

## **Converting Excel Workbook to XPS**

The XPS document format consists of structured XML markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing documents.

The markup language for XPS is a subset of XAML which allows it to incorporate vector graphics elements in documents, using XAML to mark up the Windows Presentation Foundation (WPF) primitives. The elements used are described in terms of paths and other geometrical primitives.

An XPS file is, in fact, a unicode ZIP archive using the Open Packaging Conventions, containing the files which make up the document. These include an XML markup file for each page, text, embedded fonts, raster images, 2D vector graphics, as well as the digital rights management information. The contents of an XPS file can be examined simply by opening it in an application that supports ZIP files.

From Aspose.Cells 6.0.0, Microsoft Excel to XPS conversion is supported.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Converting Excel Workbook to MHTML Files**

MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension.

Aspose.Cells supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Converting Excel Workbook to HTML**

The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the **[HtmlSaveOptions](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)** class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Setting the Image Preferences for HTML**

Starting from 8.0.2, Aspose.Cells has exposed **[ImageOptions](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** for the **[HtmlSaveOptions](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)** class, allowing developers to specify image preferences when saving spreadsheets to HTML format.

Below are details of some of the image settings that can be applied,

- **[ImageType](https://apireference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: Specifies the image type. Please note, all shapes, including charts, render as images in the output HTML.
- **[SmoothingMode](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: Specifies the anti-aliasing for lines, curves & edges of filled areas.
- **[TextRenderingHint](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint)**: Specifies the quality of text rendering.
- **[Quality](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)**: Specifies the quality of the image between 0 to 100, when **[ImageType](https://apireference.aspose.com/cells/net/aspose.cells.drawing/imagetype)** is specified as Jpeg.
- **[VerticalResolution](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: Gets or sets the vertical resolution of the image in dots per inch.
- **[HorizontalResolution](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**: Gets or sets the horizontal resolution of the image in dots per inch.
- **[TiffCompression](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)**: Gets or sets the compression type for the images when **[ImageType](https://apireference.aspose.com/cells/net/aspose.cells.drawing/imagetype)** is specified as Tiff.
- **[Transparent](https://apireference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**: Indicates if the background of an image should be transparent when ImageFormat is specified as Png.

The code below demonstrates how to use **[HtmlSaveOptions.ImageOptions](https://apireference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** to specify different preferences.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Convert Excel Workbook to Markdown**

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass **[SaveFormat.Markdown](https://apireference.aspose.com/cells/net/aspose.cells/saveformat)** as the second parameter of **[Workbook.Save](https://apireference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** method. You may also use **[MarkdownSaveOptions](https://apireference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** class to specify additional settings for exporting worksheet to Markdown.

The following code example demonstrates exporting active worksheet to Markdown by using **[SaveFormat.Markdown](https://apireference.aspose.com/cells/net/aspose.cells/saveformat)** enumeration member. Please see the [output Markdown file](md_sample.txt) generated by the code for reference.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Convert Excel Workbook to JSON**

Aspose.Cells supports converting a workbook to Json(JavaScript Object Notation) file.

The following code example demonstrates exporting active worksheet to Json by using [**SaveFormat.Json**](https://apireference.aspose.com/cells/net/aspose.cells/saveformat) enumeration member. Please see the code to convert [source file](Book1.xlsx) to the [output Json file](Book1.Json) generated by the code for reference.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Convert Excel Workbook to DOCX**

The Aspose.Cells API provides support for converting spreadsheets to DOCX format. To export the workbook to DOCX, pass [**SaveFormat.Docx**](https://apireference.aspose.com/cells/net/aspose.cells/saveformat) as the second parameter of [**Workbook.Save**](https://apireference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) method. You may also use [**DocxSaveOptions**](https://apireference.aspose.com/cells/net/aspose.cells/docxsaveoptions) class to specify additional settings for exporting worksheet to DOCX.

The following code example demonstrates exporting active worksheet to DOCX by using [**SaveFormat.Docx**](https://apireference.aspose.com/cells/net/aspose.cells/saveformat) enumeration member. Please see the [output DOCX file](Book1.docx) generated by the code for reference.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Convert Excel Workbook to PPTX**

The Aspose.Cells API provides support for converting spreadsheets to PPTX format. To export the workbook to PPTX, pass [**SaveFormat.Pptx**](https://apireference.aspose.com/cells/net/aspose.cells/saveformat) as the second parameter of [**Workbook.Save**](https://apireference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) method. You may also use [**PptxSaveOptions**](https://apireference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) class to specify additional settings for exporting worksheet to PPTX.

The following code example demonstrates exporting active worksheet to PPTX by using [**SaveFormat.Pptx**](https://apireference.aspose.com/cells/net/aspose.cells/saveformat) enumeration member. Please see the [output PPTX file](Book1.pptx) generated by the code for reference.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}
