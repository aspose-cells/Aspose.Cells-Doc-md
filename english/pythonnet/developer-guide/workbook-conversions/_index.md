---
title: Convert Excel to Pdf, Image and other formats
linktitle: Workbook Conversions
type: docs
weight: 65
url: /python-net/convert-workbook-to-different-formats/
description: Convert Excel files to Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML and more by using Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel Workbook to PDF, Convert Excel Workbook to JPG in Python, Python Convert Excel Workbook to Image, Converting Excel Workbook to XPS using Python, Convert Excel to Ods, Sxc and Fods via Python, Python Convert Excel Workbook to HTML, Convert Excel Workbook to JSON in Python, Python Convert Excel Workbook to DOCX, Convert Excel Workbook to TIFF or MARKDOWN with Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET supports conversion between many formats. Technically, conversion means to load a workbook in one file format and save it into another.

{{% /alert %}}

## **Convert Excel Workbook to PDF**

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells for Python via .NET supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-PDF.py" >}}

## **Convert Excel Workbook to JPG**
Aspose.Cells for Python via .NET supports converting Excel files to JPG.  
The code example below shows how to save a workbook as JPG.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JPG.py" >}}

## **Convert Excel Workbook to Image**
Aspose.Cells for Python via .NET supports converting Excel files to images.  
The code example below shows how to save a workbook as images.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Image.py" >}}

## **Converting Excel Workbook to XPS**

The XPS document format consists of structured XML markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing documents.

The markup language for XPS is a subset of XAML which allows it to incorporate vector graphics elements in documents, using XAML to mark up the Windows Presentation Foundation (WPF) primitives. The elements used are described in terms of paths and other geometrical primitives.

An XPS file is, in fact, a Unicode ZIP archive using the Open Packaging Conventions, containing the files which make up the document. These include an XML markup file for each page, text, embedded fonts, raster images, 2D vector graphics, as well as the digital rights management information. The contents of an XPS file can be examined simply by opening it in an application that supports ZIP files.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XPS.py" >}}

## **Convert Excel to Ods, Sxc and Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells for Python via .NET supports converting Excel files to ODS, SXC, and FODS files. The code example below shows how to convert the [template](book1.xlsx) to ODS, SXC, and FODS files.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-ODS.py" >}}

## **Converting Excel Workbook to MHTML Files**

MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension.

Aspose.Cells for Python via .NET supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-MHTML.py" >}}

## **Converting Excel Workbook to HTML**

The Aspose.Cells for Python via .NET API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells for Python via .NET uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/) class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML.py" >}}

## **Setting the Image Preferences for HTML**

Aspose.Cells for Python via .NET has exposed [**image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) for the [**HtmlSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions) class, allowing developers to specify image preferences when saving spreadsheets to HTML format.

Below are details of some of the image settings that can be applied:

- [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/): Specifies the image type. Please note, all shapes, including charts, render as images in the output HTML.
- [**smoothing_mode**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/smoothing_mode/): Specifies the anti-aliasing for lines, curves & edges of filled areas.
- [**text_rendering_hint**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/text_rendering_hint/): Specifies the quality of text rendering.
- [**quality**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/quality/): Specifies the quality of the image between 0 to 100, when [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) is specified as Jpeg.
- [**vertical_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/): Gets or sets the vertical resolution of the image in dots per inch.
- [**horizontal_resolution**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/): Gets or sets the horizontal resolution of the image in dots per inch.
- [**tiff_compression**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/): Gets or sets the compression type for the images when [**ImageType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/imagetype/) is specified as Tiff.
- [**transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent/): Indicates if the background of an image should be transparent when ImageFormat is specified as Png.

The code below demonstrates how to use [**HtmlSaveOptions.image_options**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/image_options/) to specify different preferences.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-HTML-SettingImagePrefrencesforHTML-1.py" >}}

## **Convert Excel Workbook to Markdown**

The Aspose.Cells for Python via .NET API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) as the second parameter of [**Workbook.Save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.saveformat) method. You may also use [**MarkdownSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/markdownsaveoptions) class to specify additional settings for exporting worksheet to Markdown.

The following code example demonstrates exporting the active worksheet to Markdown by using the [**SaveFormat.MARKDOWN**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration member. Please see the [output Markdown file](md_sample.txt) generated by the code for reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Markdown-1.py" >}}

## **Convert Excel Workbook to JSON**

Aspose.Cells for Python via .NET supports converting a workbook to JSON (JavaScript Object Notation) file.

The following code example demonstrates exporting the active worksheet to JSON by using [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration member. Please see the code to convert the [source file](Book1.xlsx) to the [output JSON file](Book1.Json) generated by the code for reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON.py" >}}

## **Convert Excel to XML**
Aspose.Cells for Python via .NET supports converting a workbook to Excel 2003 Spreadsheet XML and plain XML data.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-XML.py" >}}

## **Convert Excel Workbook to TIFF**
Aspose.Cells for Python via .NET supports converting a workbook to a TIFF file.

The code snippet below shows how to convert Excel to TIFF:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-TIFF.py" >}}

## **Convert Excel Workbook to DOCX**

The Aspose.Cells for Python via .NET API provides support for converting spreadsheets to DOCX format. To export the workbook to DOCX, pass [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) as the second parameter of [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) method. You may also use [**DocxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/docxsaveoptions/) class to specify additional settings for exporting worksheet to DOCX.

The following code example demonstrates exporting the active worksheet to DOCX by using the [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration member. Please see the [output DOCX file](Book1.docx) generated by the code for reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-Docx-1.py" >}}

## **Convert Excel Workbook to PPTX**

The Aspose.Cells for Python via .NET API provides support for converting spreadsheets to PPTX format. To export the workbook to PPTX, pass [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) as the second parameter of [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#io.RawIOBase-aspose.cells.SaveOptions) method. You may also use [**PptxSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pptxsaveoptions) class to specify additional settings for exporting worksheet to PPTX.

The following code example demonstrates exporting the active worksheet to PPTX by using the [**SaveFormat.PPTX**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) enumeration member. Please see the [output PPTX file](Book1.pptx) generated by the code for reference.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-File-To-Pptx-1.py" >}}

## **Advanced topics**
- [Json](/cells/python-net/convert-workbook-to-json/)
- [Pdf](/cells/python-net/convert-excel-to-pdf/)
- [Convert CSV, TSV and TXT to Excel](/cells/python-net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="python-net" >}}
