---
title: 设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级
type: docs
weight: 30
url: /zh/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能的使用场景**

在设置 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 和 **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** 的 **DefaultFont** 属性时，您可能希望保存为 PDF 或图像将默认字体设置为工作簿中具有缺失 (未安装) 字体的所有文本。

通常，在保存为 PDF 或图像时，Aspose.Cells 首先尝试设置工作簿的默认字体（即，Workbook.DefaultStyle.Font）。如果工作簿的默认字体仍无法正确显示/呈现文本，那么 Aspose.Cells 将尝试使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** 中针对 DefaultFont 属性的字体进行渲染。

为了符合您的期望，我们在 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** 中有一个名为 "**CheckWorkbookDefaultFont**" 的布尔属性。您可以将其设置为 **false** 以禁用尝试工作簿的默认字体，或者让 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** 中的 **DefaultFont** 设置具有优先级。

## **设置 PdfSaveOptions/ImageOrPrintOptions 的 DefaultFont 属性**

以下示例代码打开一个Excel文件。第一个工作表中的 A1 单元格的文本设置为 "圣诞节字体文本"。字体名称为 "Christmas Time Personal Use"，但未安装在该计算机上。我们将 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**/**[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)** 的 ***DefaultFont*** 属性设置为 "Times New Roman"。我们还将 **CheckWorkbookDefaultFont** 布尔属性设置为 **"false"**，确保 A1 单元格的文本以 "Times New Roman" 字体呈现，并且不使用工作簿的默认字体（在本例中为 "Calibri"）。该代码将第一个工作表渲染为 PNG 和 TIFF 图像格式。最后将渲染为 PDF 文件格式。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont*** 属性的默认值为 **true**。

{{% /alert %}}

这是示例代码中使用的 [模板文件](49446913.xlsx) 的屏幕截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

在将 **[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)** 属性设置为 "Times New Roman" 后的输出 PNG 图像。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

查看将 **[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/defaultfont/)** 属性设置为 "Times New Roman" 后的输出 [TIFF](48496672.tiff) 图像。

查看将 **[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** 属性设置为 "Times New Roman" 后的输出 [PDF](48496673.pdf) 文件。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.cs" >}}
