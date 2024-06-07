---
title: 设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级
type: docs
weight: 30
url: /zh/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能的使用场景**

在设置[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)的**DefaultFont**属性时，您可能期望保存为PDF或图像会将该**DefaultFont**设置为工作簿中所有缺失的（未安装）字体的文本。

一般而言，当保存为PDF或图像时，Aspose.Cells首先尝试设置工作簿的默认字体（即[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)）。如果工作簿的默认字体仍无法正确显示/渲染文本，则Aspose.Cells将尝试使用[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中**DefaultFont**属性所述的字体进行渲染。

为满足您的期望，我们在[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中有一个名为"**CheckWorkbookDefaultFont**"的布尔属性。您可以将其设置为false以禁用尝试使用工作簿的默认字体，或者将[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中的**DefaultFont**设置优先级。

## **设置 PdfSaveOptions/ImageOrPrintOptions 的 DefaultFont 属性**

下面的示例代码打开一个Excel文件。第一个工作表的A1单元格中设置了文本"圣诞时节字体文本"。字体名称为"圣诞时节个人使用"，但未安装在该机器上。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)的**DefaultFont**属性设置为"Times New Roman"。同时，我们将**CheckWorkbookDefaultFont**布尔属性设置为"**false**"，确保A1单元格的文本使用"Times New Roman"字体，并且不使用工作簿的默认字体（在这种情况下是"Calibri"）。代码将第一个工作表渲染为PNG和TIFF图像格式。最后渲染为PDF文件格式。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** 属性的默认值为 **true**。

{{% /alert %}}

这是示例代码中使用的 [模板文件](49446914.xlsx) 的截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) 属性设置为"Times New Roman"后得到的输出 PNG 图像。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

将 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) 属性设置为"Times New Roman"后得到的输出 [TIFF](out1_imageTIFF.tiff) 图像。

将 [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) 属性设置为"Times New Roman"后得到的输出 [PDF](out1_pdf.pdf) 文件。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
