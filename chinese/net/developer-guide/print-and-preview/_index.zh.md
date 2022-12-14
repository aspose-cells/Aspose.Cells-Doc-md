---
title: 打印和预览工作簿
linktitle: 打印和预览
type: docs
weight: 70
url: /zh/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells 支持在没有安装Microsoft Excel的情况下打印预览Excel文件。
---
{{% alert color="primary" %}}

创建工作表后，您通常希望打印一份硬拷贝。本文介绍如何使用 Aspose.Cells 打印电子表格。

{{% /alert %}}

## **打印介绍**

Microsoft Excel 假定您要打印整个工作表区域，除非您指定一个选择。要使用 Aspose.Cells 打印，首先将 Aspose.Cells.Rendering 命名空间导入程序。它有几个有用的类，例如，[**图纸渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)和[**工作簿渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **使用 SheetRender 打印**

这[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类代表一个工作表并具有[**打印机**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)可以打印工作表的方法。以下示例代码显示了如何打印工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **使用 WorkbookRender 打印**

要打印整个工作簿，遍历工作表并打印它们，或使用[**工作簿渲染**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)班级。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells 还为[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3)和[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2)方法，因此可以在打印 Excel 电子表格时设置打印作业名称。默认情况下，所有打印作业都以名称“文档”创建。

{{% /alert %}}

## **打印预览**

可能会有数百万页的 Excel 文件需要转换为 PDF 或图像的情况。处理此类文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换此类文件之前，用户可以检查总页数，然后决定是否转换文件。本文着重于使用[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类找出总页数。

Aspose.Cells 提供打印预览功能。为此，API 提供[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类。要创建整个工作簿的打印预览，请创建[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)通过类[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)和[**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)对象到构造函数。这[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)类提供了一个[**评估页数**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount)返回生成的预览中的页数的方法。如同[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)类，[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类用于为特定工作表生成打印预览。要创建工作表的打印预览，请创建[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)通过类[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)和[**图像或打印选项**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)对象到构造函数。这[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类还提供了一个[**评估页数**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)返回生成的预览中的页数的方法。

下面的代码片段演示了两者的使用[**工作簿打印预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**单张印刷预览**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)通过使用类[示例 excel 文件](94896177.xlsx).

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

以下是执行上述代码生成的输出。

### **控制台输出**

工作簿页数：1
工作表页数：1


## **推进主题**
- [配置呈现电子表格的字体](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/)
- [将工作表转换为图像 - 删除数据周围的空白](/cells/zh/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [按页将工作表转换为图像并将工作表转换为图像](/cells/zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [使用 ImageOrPrint 选项将工作表转换为图像](/cells/zh/net/converting-worksheet-to-image-using-imageorprint-options/)
- [将工作表中的 Cells 范围导出到图像](/cells/zh/net/export-range-of-cells-in-a-worksheet-to-image/)
- [将工作表或图表导出为具有所需宽度和高度的图像](/cells/zh/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [使用 ImageOrPrintOptions 从工作表中提取图像](/cells/zh/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [生成工作表的缩略图](/cells/zh/net/generate-thumbnail-of-the-worksheet/)
- [无内容打印时输出空白页](/cells/zh/net/output-blank-page-when-there-is-nothing-to-print/)
- [页面设置和打印选项](/cells/zh/net/page-setup-and-printing-options/)
- [使用 SheetRender 和 WorkbookRender 打印页面范围](/cells/zh/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [使用 ImageOrPrintOptions 的 PageIndex 和 PageCount 属性渲染页面序列](/cells/zh/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [将工作表渲染到图形上下文](/cells/zh/net/render-worksheet-to-graphic-context/)
- [为工作簿呈现指定单个或私有字体集](/cells/zh/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [使用 Aspose.Cells 打印时指定作业或文档名称](/cells/zh/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
