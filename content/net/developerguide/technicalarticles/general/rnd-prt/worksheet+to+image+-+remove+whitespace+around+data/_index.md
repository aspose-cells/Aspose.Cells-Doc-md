---
title : "Worksheet to Image - Remove Whitespace around Data" 
description : "" 
weight : 20359 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/worksheet+to+image+-+remove+whitespace+around+data/
---

# Aspose.Cells for .NET : Worksheet to Image - Remove Whitespace around Data


Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.

## Remove Whitespace around Data

The [Aspose.Cells.Rendering.SheetRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.

When you use the sheet-to-image feature, the output image has whitespace, that is, a border, around it by default. You can remove this by setting the top, left, bottom and right page setup margins for the source worksheet to 0 and specify [Aspose.Cells.Rendering.ImageOrPrintOptions](https://apireference.aspose.com/net/cells/aspose.cells.rendering/imageorprintoptions) attributes accordingly.

Below example code removes the whitespace around the data in the output image.

