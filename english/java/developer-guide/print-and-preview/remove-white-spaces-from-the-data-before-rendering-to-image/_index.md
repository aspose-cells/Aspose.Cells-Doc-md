---  
title: Remove White Spaces from the Data before Rendering to Image  
type: docs  
weight: 270  
url: /java/remove-white-spaces-from-the-data-before-rendering-to-image/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells API allows you to convert Microsoft Excel worksheets to images.  

{{% /alert %}}  

The [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class is capable of converting a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.  

When you use the sheet‑to‑image feature, the output image has white/blank space (i.e., a border) around it by default. You can remove this. Set the top, left, bottom, and right page‑setup margins for the source worksheet to 0 and specify [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) attributes accordingly.  

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}  
{{< app/cells/assistant language="java" >}}
