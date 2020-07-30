---
title : "Convert Workbook to Different Formats" 
description : "" 
weight : 12065 
toc : false
type: docs
url: /net/developerguide/ld-sv-cvt-mng/convert+workbook+to+different+formats/
---

# Aspose.Cells for .NET : Convert Workbook to Different Formats


Aspose.Cells supports conversion between many formats. Technically, conversion means to load a workbook in one file format and save it into another.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Excel Workbook to XPS](#converting-excel-workbook-to-xps)
*   2 [Converting Excel Workbook to MHTML Files](#converting-excel-workbook-to-mhtml-files)
*   3 [Converting Excel Workbook to HTML](#converting-excel-workbook-to-html)
*   4 [Setting the Image Preferences for HTML](#setting-the-image-preferences-for-html)
*   5 [Convert Excel Workbook to Markdown](#convert-excel-workbook-to-markdown)
{{< /panel >}}
 

## Converting Excel Workbook to XPS

The XPS document format consists of structured XML markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing and printing documents.

The markup language for XPS is a subset of XAML which allows it to incorporate vector graphics elements in documents, using XAML to mark up the Windows Presentation Foundation (WPF) primitives. The elements used are described in terms of paths and other geometrical primitives.

An XPS file is, in fact, a Unicoded ZIP archive using the Open Packaging Conventions, containing the files which make up the document. These include an XML markup file for each page, text, embedded fonts, raster images, 2D vector graphics, as well as the digital rights management information. The contents of an XPS file can be examined simply by opening it in an application which supports ZIP files.

From Aspose.Cells 6.0.0, Microsoft Excel to XPS conversion is supported.

## Converting Excel Workbook to MHTML Files

MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio and so on) into one file. They are used for emails with the .mht file extension.

Aspose.Cells supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file.

## Converting Excel Workbook to HTML

The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [HtmlSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions) class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file.

## Setting the Image Preferences for HTML

Starting from 8.0.2, Aspose.Cells has exposed [ImageOptions](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/imageoptions) for the [HtmlSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions) class, allowing developers to specify image preferences when saving spreadsheets to HTML format.

Below are details of some of the image settings that can be applied,

*   [ImageType](https://apireference.aspose.com/net/cells/aspose.cells.drawing/imagetype): Specifies the image type. Please note, all shapes, including charts, render as images in the output HTML.
*   [SmoothingMode](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Specifies the anti-aliasing for lines, curves & edges of filled areas.
*   [TextRenderingHint](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Specifies the quality of text rendering.
*   [Quality](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/quality): Specifies the quality of the image between 0 to 100, when [ImageType](https://apireference.aspose.com/net/cells/aspose.cells.drawing/imagetype) is specified as Jpeg.
*   [VerticalResolution](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Gets or sets the vertical resolution of the image in dots per inch.
*   [HorizontalResolution](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Gets or sets the horizontal resolution of the image in dots per inch.
*   [TiffCompression](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Gets or sets the compression type for the images when [ImageType](https://apireference.aspose.com/net/cells/aspose.cells.drawing/imagetype) is specified as Tiff.
*   [Transparent](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions/properties/transparent): Indicates if the background of an image should be transparent when `ImageFormat` is specified as Png.

The code below demonstrates how to use [HtmlSaveOptions.ImageOptions](https://apireference.aspose.com/net/cells/aspose.cells/htmlsaveoptions/properties/imageoptions) to specify different preferences.

## Convert Excel Workbook to Markdown

The Aspose.Cells API provides support for exporting spreadsheets to Markdown format. To export the active worksheet to Markdown, pass [SaveFormat.Markdown](https://apireference.aspose.com/net/cells/aspose.cells/saveformat) as the second parameter of [Workbook.Save](https://apireference.aspose.com/net/cells/aspose.cells.workbook/save/methods/3) method. You may also use [MarkdownSaveOptions](https://apireference.aspose.com/net/cells/aspose.cells/markdownsaveoptions) class to specify additional settings for exporting worksheet to Markdown.

The following code example demonstrates exporting active worksheet to Markdown by using [SaveFormat.Markdown](https://apireference.aspose.com/net/cells/aspose.cells/saveformat) enumeration member. Please see the [output Markdown file](https://docs2.aspose.com/cells/net/attachments/5013525/89620482.md) generated by the code for reference.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Book1.md](https://docs2.aspose.com/cells/net/attachments/5013525/89620482.md) (application/octet-stream)  

