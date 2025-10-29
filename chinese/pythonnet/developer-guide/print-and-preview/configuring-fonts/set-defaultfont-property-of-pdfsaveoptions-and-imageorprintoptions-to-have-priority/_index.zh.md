---
title: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **可能的使用场景**

在设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) 的 **DefaultFont** 属性时，您可能希望保存为 PDF 或图像时将该 DefaultFont 设置为工作簿中所有没有安装的字体的文本。

通常，在保存为PDF或图片时，Aspose.Cells for Python via .NET会首先尝试设置工作簿的默认字体（即Workbook.DefaultStyle.Font）。如果工作簿的默认字体仍无法正确显示/渲染文本，则Aspose.Cells for Python via .NET会尝试用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)中DefaultFont属性指定的字体进行渲染。

为了满足您的需求，我们在[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)中增加了一个布尔属性“**check_workbook_default_font**”。您可以将其设置为**false**，以禁用尝试使用工作簿的默认字体，或者让[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)中的**default_font**设置优先。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

以下示例代码打开一个Excel文件。第一个工作表的A1单元格中有文本“Christmas Time Font text”，字体名为“Christmas Time Personal Use”，该字体未安装在机器上。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)的***default_font***属性设置为“Times New Roman”。同时将布尔属性**check_workbook_default_font**设置为“false”，确保A1单元格的文本用“Times New Roman”字体渲染，不使用工作簿的默认字体（即“Calibri”）。代码将第一个工作表导出为PNG和TIFF图像格式，最后导出为PDF文件。

{{% alert color="primary" %}}

***CheckWorkbookDefaultFont***属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446913.xlsx)的屏幕截图。

![todo:image_alt_text](1.png)

将[**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font)属性设置为"Times New Roman"后的输出PNG图像。

![todo:image_alt_text](2.png)

查看在将 [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) 属性设置为 "Times New Roman" 后的输出 [TIFF](48496672.tiff) 图像。

查看在将 [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) 属性设置为 "Times New Roman" 后的输出 [PDF](48496673.pdf) 文件。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
