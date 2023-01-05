---
title: 将 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性设置为优先
type: docs
weight: 30
url: /zh/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **可能的使用场景**

同时设置**默认字体**的财产[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)和[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)，您可能希望保存到 PDF 或图像会设置**默认字体**工作簿中所有缺少（未安装）字体的文本。

一般在保存到PDF或者图片时，Aspose.Cells会先尝试设置Workbook的默认字体（即，[**工作簿.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ).如果工作簿的默认字体仍然无法正确显示/呈现文本，则 Aspose.Cells 将尝试使用提到的字体呈现**默认字体**属性在[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

为了满足您的期望，我们有一个名为“**检查工作簿默认字体**“ 在[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).您可以将其设置为 false 以禁用尝试工作簿的默认字体或让**默认字体**置入[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)有优先权。

## **设置 PdfSaveOptions/ImageOrPrintOptions 的 DefaultFont 属性**

以下示例代码打开一个 Excel 文件。 A1 单元格（在第一个工作表中）的文本设置为“Christmas Time Font text”。字体名称是计算机上未安装的“Christmas Time Personal Use”。我们设置**默认字体**的属性[**Pdf保存选项**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)到“时代新罗马”。我们还设置**检查工作簿默认字体**布尔属性为“**错误的**“这确保 A1 单元格的文本以“Times New Roman”字体呈现，并且不应使用工作簿的默认字体（在本例中为“Calibri”）。代码将第一个工作表呈现为 PNG 和 TIFF 图像格式。它最终呈现为 PDF 文件格式。

{{% alert color="primary" %}}

默认值***检查工作簿默认字体***属性是**真的**.

{{% /alert %}}

这是截图[模板文件](49446914.xlsx)在示例代码中使用。

![待办事项：图片_替代_文本](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

这是设置后的输出 PNG 图像[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性为“Times New Roman”。

![待办事项：图片_替代_文本](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

查看输出[TIFF](out1_imageTIFF.tiff)设置后的图像[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)属性为“Times New Roman”。

查看输出[PDF](out1_pdf.pdf)设置后的文件[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)属性为“Times New Roman”。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
