---
title: 打印和预览工作簿
linktitle: 打印和预览
type: docs
weight: 70
url: /zh/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells支持在没有安装Microsoft Excel的情况下打印和预览Excel文件。
---

{{% alert color="primary" %}}

创建工作表后，通常需要打印硬拷贝。本文介绍如何使用Aspose.Cells打印电子表格。

{{% /alert %}}

## **打印介绍**

Microsoft Excel默认假定您要打印整个工作表区域，除非指定了选择内容。要使用Aspose.Cells打印，首先需要将Aspose.Cells.Rendering命名空间导入程序。它有几个有用的类，例如 [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) 和 [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)。

### **使用SheetRender打印**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)类表示一个工作表，具有 [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) 方法可打印工作表。下面的示例代码展示如何打印工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **使用WorkbookRender打印**

要打印整个工作簿，需要遍历各个工作表并打印，或使用 [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) 类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells还为 [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) 和 [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) 方法提供了重载，因此在打印Excel电子表格时可以设置打印作业名称。默认情况下，所有打印作业都以"Document"命名。

{{% /alert %}}

## **打印预览**

在某些情况下，需要将包含数百万页的Excel文件转换为PDF或图像。处理这些文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会发挥作用。在转换此类文件之前，用户可以检查总页数，然后决定是否转换该文件。本文重点介绍如何使用 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类查找总页数。

Aspose.Cells提供打印预览功能。为此，API 提供了 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类。要创建整个工作簿的打印预览，通过将 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 类示例化，并传递 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) 对象给构造函数。 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 类提供了 [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) 方法，返回生成预览的页数。类似于 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 类， [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类用于生成特定工作表的打印预览。要创建工作表的打印预览，通过将 [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类示例化，并传递 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) 对象给构造函数。 [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类还提供了 [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) 方法，返回生成预览的页数。

以下代码片段演示了使用 [示例Excel文件](94896177.xlsx) 的 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) 类的用法。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

执行上述代码后生成的输出如下。

### **控制台输出**

工作簿页数：1
工作表页数：1


## **高级主题**
- [配置呈现电子表格的字体](/cells/zh/net/configuring-fonts-for-rendering-spreadsheets/)
- [将工作表转换为图像 - 删除数据周围的空白](/cells/zh/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [将工作表转换为图像和按页转换工作表为图像](/cells/zh/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [使用ImageOrPrint选项将工作表转换为图像](/cells/zh/net/converting-worksheet-to-image-using-imageorprint-options/)
- [将工作表中的一系列单元格导出为图像](/cells/zh/net/export-range-of-cells-in-a-worksheet-to-image/)
- [使用所需宽度和高度将工作表或图表导出为图像](/cells/zh/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [使用ImageOrPrintOptions从工作表中提取图像](/cells/zh/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [生成工作表的缩略图](/cells/zh/net/generate-thumbnail-of-the-worksheet/)
- [当没有内容可打印时输出空白页](/cells/zh/net/output-blank-page-when-there-is-nothing-to-print/)
- [页面设置和打印选项](/cells/zh/net/page-setup-and-printing-options/)
- [使用SheetRender和WorkbookRender打印页面范围](/cells/zh/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [使用PageIndex和PageCount属性的ImageOrPrintOptions渲染页面序列](/cells/zh/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [将工作表渲染到图形上下文](/cells/zh/net/render-worksheet-to-graphic-context/)
- [为工作簿渲染指定单独或私有字体集](/cells/zh/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [使用Aspose.Cells打印时指定作业或文档名称](/cells/zh/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
