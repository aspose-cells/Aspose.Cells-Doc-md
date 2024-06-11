---
title: 打印和预览工作簿
linktitle: 打印和预览
type: docs
weight: 70
url: /zh/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells支持在没有安装Microsoft Excel的情况下打印和预览Excel文件
---

{{% alert color="primary" %}}

创建工作表后，通常希望打印它的实体副本。本文介绍如何使用Aspose.Cells打印电子表格

{{% /alert %}}

## **打印简介**

Microsoft Excel假定您想打印整个工作表区域，除非您指定了选择区域。要使用Aspose.Cells进行打印，首先将Aspose.Cells.Rendering命名空间导入到程序中。它有几个有用的类，例如[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)和[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)

### **使用SheetRender进行打印**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类表示一个工作表，其中包含一个用于打印工作表的[**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)方法。以下示例代码显示如何打印一个工作表

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **使用WorkbookRender进行打印**

要打印整个工作簿，迭代工作表并打印它们，或使用[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells还为[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3)和[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2)方法提供了重载，因此可以在打印Excel电子表格时设置打印作业名称。默认情况下，所有打印作业都使用名称“Document”创建。

{{% /alert %}}

## **打印预览**

可能有一些情况下，需要将数百万页的Excel文件转换为PDF或图像。处理这些文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换这样的文件之前，用户可以检查总页数，然后决定是否转换文件。本文侧重于使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类来查找总页数。

Aspose.Cells提供打印预览功能。为此，API提供[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类。要创建整个工作簿的打印预览，通过向构造函数传递[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)对象创建[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)类的实例。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)类提供了一个[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount)方法，返回生成预览中的页数。类似于[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)类，[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类用于为特定工作表生成打印预览。要创建工作表的打印预览，通过向构造函数传递[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)对象创建[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类的实例。[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类还提供一个[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)方法，返回生成预览的页数。

以下代码片段演示了通过使用示例Excel文件（94896177.xlsx）使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)类。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

执行上述示例代码生成的输出如下。

### **控制台输出**

工作簿页数：1
工作表页数: 1


## **高级主题**
- [为呈现电子表的字体进行配置](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/)
- [将工作表转换为图像-去除数据周围的空白](/cells/zh/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [将工作表转为图像以及按页面转为图像](/cells/zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [使用ImageOrPrint Options将工作表转换为图像](/cells/zh/net/converting-worksheet-to-image-using-imageorprint-options/)
- [导出工作表中的单元格范围为图像](/cells/zh/net/export-range-of-cells-in-a-worksheet-to-image/)
- [使用所需的宽度和高度将工作表或图表导出为图像](/cells/zh/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [使用ImageOrPrintOptions从工作表中提取图像](/cells/zh/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [生成工作表的缩略图](/cells/zh/net/generate-thumbnail-of-the-worksheet/)
- [当没有要打印的内容时输出空白页](/cells/zh/net/output-blank-page-when-there-is-nothing-to-print/)
- [页面设置和打印选项](/cells/zh/net/page-setup-and-printing-options/)
- [使用SheetRender和WorkbookRender打印一系列页面](/cells/zh/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [使用ImageOrPrintOptions的PageIndex和PageCount属性呈现页面序列](/cells/zh/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [将工作表渲染到图形上下文](/cells/zh/net/render-worksheet-to-graphic-context/)
- [指定工作簿渲染的个体或私有字体集](/cells/zh/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [在使用 Aspose.Cells 打印时指定作业或文档名称](/cells/zh/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
