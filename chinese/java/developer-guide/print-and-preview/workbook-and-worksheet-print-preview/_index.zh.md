---
title: 工作簿和工作表打印预览
type: docs
weight: 130
url: /zh/java/workbook-and-worksheet-print-preview/
---

## **使用场景**

可能存在需要将拥有数百万页的 Excel 文件转换为 PDF 或图像的情况。处理这样的文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会被证明是有用的。在转换此类文件之前，用户可以检查总页数，然后决定是否要转换该文件。本文重点介绍如何使用 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类来查找总页数。

## **工作簿和工作表打印预览**

Aspose.Cells 提供了打印预览功能。作业队列提供了 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类。要创建整个工作簿的打印预览，通过将 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) 对象传递到构造函数中来创建 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 类的实例。 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 类提供了一个 [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) 方法，该方法返回生成的预览中的页数。类似于 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 类， [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类用于生成特定工作表的打印预览。要创建工作表的打印预览，通过将 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) 对象传递到构造函数中来创建 [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类的实例。 [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类还提供了一个 [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) 方法，该方法返回生成的预览中的页数。

以下代码片段展示了如何使用 [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) 和 [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) 类，使用 [示例 excel 文件](Book1.xlsx)。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

执行上述示例代码生成的输出如下。

### **控制台输出**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
