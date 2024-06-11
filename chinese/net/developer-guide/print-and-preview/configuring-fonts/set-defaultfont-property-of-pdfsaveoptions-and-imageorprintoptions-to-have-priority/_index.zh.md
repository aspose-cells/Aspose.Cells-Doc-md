---
title: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能的使用场景**

在将电子表格另存为PDF或图像时设置[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)和[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)的**DefaultFont**属性时，您可能希望将默认字体设置为所有具有丢失（未安装）字体的工作簿中的文本。

一般来说，当保存为PDF或图像时，Aspose.Cells首先尝试设置工作簿的默认字体（即，Workbook.DefaultStyle.Font）。如果工作簿的默认字体仍无法正确显示/呈现文本，则Aspose.Cells将尝试使用[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)中DefaultFont属性中指定的字体进行渲染。

为满足您的期望，我们在[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)中增加了一个名为"**CheckWorkbookDefaultFont**"的布尔属性。您可以将其设置为**false**以禁用尝试工作簿的默认字体，或者让[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)/[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)中的**DefaultFont**设置具有优先级。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

以下示例代码打开一个Excel文件。第一个工作表中的A1单元格的文本设置为"Christmas Time Font text"。字体名称为"Christmas Time Personal Use"，该字体未安装在设备上。我们将**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**的***DefaultFont***属性设置为"Times New Roman"。我们还将**CheckWorkbookDefaultFont**布尔属性设置为**"false"**，以确保A1单元格的文本使用"Times New Roman"字体渲染，而不使用工作簿的默认字体（在本例中为"Calibri"）。该代码将第一个工作表渲染为PNG和TIFF图像格式。最终渲染为PDF文件格式。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont***属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446913.xlsx)的屏幕截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

这是将**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**属性设置为"Times New Roman"后的输出PNG图像。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

查看将**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)**属性设置为"Times New Roman"后的输出[TIFF](48496672.tiff)图像。

查看将**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)**属性设置为"Times New Roman"后的输出 [PDF](48496673.pdf) 文件。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
