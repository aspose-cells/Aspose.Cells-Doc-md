---
title: Convert Excel to Pdf, Image, and other formats with Golang via C++
linktitle: Workbook Conversions
type: docs
weight: 65
url: /go-cpp/convert-workbook-to-different-formats/
description: Convert Excel files to Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML, and more using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supports conversion between many formats. Technically, conversion means loading a workbook in one file format and saving it into another.

{{% /alert %}}

## **Convert Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format, and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Convert Excel Workbook to JPG**
Aspose.Cells supports converting Excel files to JPG.
The code example below shows how to save a workbook as JPG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Convert Excel Workbook to Image**
Aspose.Cells supports converting Excel files to images.
The code example below shows how to save a workbook as images.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Converting Excel Workbook to XPS**

The XPS document format consists of structured XML markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing documents.

The markup language for XPS is a subset of XAML, which allows it to incorporate vector graphics elements in documents, using XAML to mark up the Windows Presentation Foundation (WPF) primitives. The elements used are described in terms of paths and other geometrical primitives.

An XPS file is, in fact, a Unicode ZIP archive using the Open Packaging Conventions, containing the files that make up the document. These include an XML markup file for each page, text, embedded fonts, raster images, 2D vector graphics, as well as digital rights management information. The contents of an XPS file can be examined simply by opening it in an application that supports ZIP files.

From Aspose.Cells 6.0.0, Microsoft Excel to XPS conversion is supported.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Convert Excel to Ods, Sxc, and Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supports converting Excel files to Ods, Sxc, and Fods files. The code example below shows how to convert the [template](book1.xlsx) to Ods, Sxc, and Fods files.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Converting Excel Workbook to MHTML Files**

MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, etc.) into one file. It is used for emails with the .mht file extension.

Aspose.Cells supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Converting Excel Workbook to HTML**

The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Setting the Image Preferences for HTML**

Starting from 8.0.2, Aspose.Cells has exposed [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) for the [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) class, allowing developers to specify image preferences when saving spreadsheets to HTML format.

Below are details of some of the image settings that can be applied:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): Specifies the image type. Please note, all shapes, including charts, render as images in the output HTML.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): Specifies the quality of the image between 0 to 100 when [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) is specified as Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): Gets or sets the vertical resolution of the image in dots per inch.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): Gets or sets the horizontal resolution of the image in dots per inch.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): Gets or sets the compression type for the images when [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) is specified as Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): Indicates if the background of an image should be transparent when ImageFormat is specified as Png.

The code below demonstrates how to use [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) to specify different preferences.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Convert Excel Workbook to Markdown**

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. You may also use [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) class to specify additional settings for exporting the worksheet to Markdown.

The following code example demonstrates exporting the active worksheet to Markdown by using [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member. Please see the [output Markdown file](md_sample.txt) generated by the code for reference.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Convert Excel Workbook to JSON**

Aspose.Cells supports converting a workbook to JSON (JavaScript Object Notation) file.

The following code example demonstrates exporting the active worksheet to JSON by using [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member. Please see the code to convert [source file](Book1.xlsx) to the [output JSON file](Book1.Json) generated by the code for reference.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Convert Excel to XML**
Aspose.Cells supports converting a workbook to Excel 2003 Spreadsheet XML and plain XML data.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Convert Excel Workbook to TIFF**
Aspose.Cells supports converting a workbook to TIFF file.

The code snippet below shows how to convert Excel to TIFF:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Convert Excel Workbook to DOCX**

The Aspose.Cells API provides support for converting spreadsheets to DOCX format. To export the workbook to DOCX, pass [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. You may also use [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) class to specify additional settings for exporting the worksheet to DOCX.

The following code example demonstrates exporting the active worksheet to DOCX by using [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member. Please see the [output DOCX file](Book1.docx) generated by the code for reference.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Convert Excel Workbook to PPTX**

The Aspose.Cells API provides support for converting spreadsheets to PPTX format. To export the workbook to PPTX, pass [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. You may also use [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) class to specify additional settings for exporting the worksheet to PPTX.

The following code example demonstrates exporting the active worksheet to PPTX by using [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member. Please see the [output PPTX file](Book1.pptx) generated by the code for reference.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Convert Excel Workbook to EPUB**

The Aspose.Cells API provides support for converting spreadsheets to EPUB format. To export the workbook to EPUB, pass [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. You may also use [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) class to specify additional settings for exporting the worksheet to EPUB.

The following code example demonstrates exporting the active worksheet to EPUB by using [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Convert Excel Workbook to AZW3**

The Aspose.Cells API provides support for converting spreadsheets to AZW3 format. To export the workbook to AZW3, pass [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. You may also use [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) class to specify additional settings for exporting the worksheet to AZW3.

The following code example demonstrates exporting the active worksheet to AZW3 by using [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) enumeration member.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Advanced topics**
- [Convert Revision of XLSB to XLSM](/cells/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/cpp/convert-excel-to-html/)
- [Image](/cells/cpp/convert-excel-to-image/)
- [Json](/cells/cpp/convert-workbook-to-json/)
- [Convert Excel workbook to Ods, Sxc, and Fods (OpenOffice / LibreOffice calc).](/cells/cpp/convert-excel-to-ods/)
- [Pdf](/cells/cpp/convert-excel-workbook-to-pdf/)
- [Convert Excel to CSV, TSV, and Txt](/cells/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Track Document Conversion Progress](/cells/cpp/track-document-conversion-progress/)
- [Convert CSV, TSV, and TXT to Excel](/cells/cpp/convert-csv-tsv-and-txt-to-excel/)