---  
title: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority with Golang via C++  
linktitle: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority  
type: docs  
weight: 30  
url: /go-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/  
description: Learn to prioritize font settings when saving documents with Aspose.Cells in C++.  
---  

## **Possible Usage Scenarios**  

While setting the **DefaultFont** property of [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), you might expect that saving to PDF or image would set that DefaultFont for all the text in a workbook that has a missing (not installed) font.  

Generally, when saving to PDF or image, Aspose.Cells will first try to set the Workbook's default font (i.e., Workbook.DefaultStyle.Font). If the workbook's default font still cannot show/render text properly, then Aspose.Cells will try to render with the font specified by the DefaultFont attribute in [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/).  

To address your expectation, we have a Boolean property named **CheckWorkbookDefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/). You can set it to **false** to disable trying the workbook's default font, or let the **DefaultFont** setting in [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/) have priority.  

## **Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions**  

The following sample code opens an Excel file. The A1 cell (in the first worksheet) contains the text **"Christmas Time Font text"**. The font name is **"Christmas Time Personal Use"**, which is not installed on the machine. We set the **DefaultFont** attribute of [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/) to **"Times New Roman"**. We also set the **CheckWorkbookDefaultFont** Boolean property to **false**, which ensures that the text of the A1 cell is rendered with **"Times New Roman"** and does not use the workbook's default font (**"Calibri"** in this case). The code renders the first worksheet to PNG and TIFF image formats and finally renders it to a PDF file format.  

{{% alert color="primary" %}}  

The default value of the **CheckWorkbookDefaultFont** attribute is **true**.  

{{% /alert %}}  

This is the screenshot of the [template file](49446913.xlsx) used in the example code.  

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)  

This is the output PNG image after setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getdefaultfont/) property to **"Times New Roman"**.  

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)  

See the output [TIFF](48496672.tiff) image after setting the [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getdefaultfont/) property to **"Times New Roman"**.  

See the output [PDF](48496673.pdf) file after setting the **PdfSaveOptions** property to **"Times New Roman"**.  

## **Sample Code**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultfontPropertyOfPdfsaveoptionsAndImageorprintoptionsToHavePriority.go" >}}  
{{< app/cells/assistant language="go" >}}
