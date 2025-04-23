---
title: 打印和预览工作簿
linktitle: 打印和预览
type: docs
weight: 70
url: /zh/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells for Python via .NET 支持无需安装微软 Excel 即可打印和预览 Excel 文件。
---

{{% alert color="primary" %}}

创建工作表后，通常需要打印其硬拷贝。本文介绍如何用 Aspose.Cells for Python via .NET 打印电子表格。

{{% /alert %}}

## **打印简介**

微软 Excel 默认会打印整张工作表，除非你指定某部分。使用 Aspose.Cells for Python via .NET 打印前，需导入 aspose.cells.rendering 命名空间，它包含几个实用类，如 [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) 和 [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)。

### **使用SheetRender进行打印**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)类表示一个工作表，其中包含一个用于打印工作表的[**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/)方法。以下示例代码显示如何打印一个工作表

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **使用WorkbookRender进行打印**

要打印整个工作簿，迭代工作表并打印它们，或使用[**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender)类。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET 也提供 [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) 和 [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings) 方法的重载，以在打印电子表格时设置打印任务名称。默认所有打印任务名为“Document”。

{{% /alert %}}

## **打印预览**

可能有一些情况下，需要将数百万页的Excel文件转换为PDF或图像。处理这些文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换这样的文件之前，用户可以检查总页数，然后决定是否转换文件。本文侧重于使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)类来查找总页数。

Aspose.Cells for Python via .NET 提供打印预览功能。API 提供 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) 类，实现整个工作簿的打印预览，创建 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) 类实例，传入 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) 对象。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) 类提供 [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/) 方法，返回预览页数。类似 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) 类，后者用于特定工作表的打印预览，通过传入 [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) 创建 [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) 类实例。

以下代码片段演示了通过使用示例Excel文件（94896177.xlsx）使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)类。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

执行上述示例代码生成的输出如下。

### **控制台输出**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

