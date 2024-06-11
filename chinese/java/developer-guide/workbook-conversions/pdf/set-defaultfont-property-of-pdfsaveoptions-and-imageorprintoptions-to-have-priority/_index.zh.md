---
title: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能的使用场景**

在设置**DefaultFont**属性时，您可能期望将其设置为工作簿中具有缺失（未安装）字体的所有文本的[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)。

通常，在保存为PDF或图像时，Aspose.Cells首先会尝试设置工作簿的默认字体（即[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font)）。如果工作簿的默认字体仍然无法正确显示/呈现文本，那么Aspose.Cells将尝试使用[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中**DefaultFont**属性所提到的字体进行呈现。

为了符合您的期望，我们在[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中有一个名为"**CheckWorkbookDefaultFont**"的布尔属性。您可以将其设置为false以禁用尝试工作簿的默认字体，或者让[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)中的**DefaultFont**设置具有优先级。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

下面的示例代码打开一个Excel文件。第一个工作表中的A1单元格的文本设置为"Christmas Time Font text"。字体名称为"Christmas Time Personal Use"，在该计算机上未安装。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)的**DefaultFont**属性设置为"Times New Roman"。我们还将**CheckWorkbookDefaultFont**布尔属性设置为"**false**"，以确保A1单元格的文本使用"Times New Roman"字体呈现，而不使用工作簿的默认字体（在此情况下为"Calibri"）。 该代码将第一个工作表呈现为PNG和TIFF图像格式。最后将其呈现为PDF文件格式。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont***属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446914.xlsx)的截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为"Times New Roman"后的输出PNG图像。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

将[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性设置为"Times New Roman"后的输出[TIFF](out1_imageTIFF.tiff)图像。

将[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)属性设置为"Times New Roman"后的输出[PDF](out1_pdf.pdf)文件。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
