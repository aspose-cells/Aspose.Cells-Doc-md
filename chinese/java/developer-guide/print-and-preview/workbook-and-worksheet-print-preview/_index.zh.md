---
title: 工作簿和工作表打印预览
type: docs
weight: 130
url: /zh/java/workbook-and-worksheet-print-preview/
---

## **使用情景**

有时需要将具有数百万页面的Excel文件转换为PDF或图像。处理这些文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换这些文件之前，用户可以查看总页数，然后决定是否转换该文件。本文侧重于使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类来查找总页数。

## **工作簿和工作表打印预览**

Aspose.Cells提供了打印预览功能。为此，API提供了[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类。要为整个工作簿创建打印预览，通过将[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)对象传递给构造函数创建[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)类的实例。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)类提供了一个[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)方法，在生成的预览中返回页面数。与[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)类类似，[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类用于为特定工作表生成打印预览。要创建工作表的打印预览，通过将[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)和[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)对象传递给构造函数创建[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类的实例。[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类还提供一个[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)方法，在生成的预览中返回页面数。

以下代码片段演示了使用[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类的用法，使用[sample excel file](Book1.xlsx)。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

执行上述代码后生成的输出如下。

### **控制台输出**

Workbook page count: 1</br>
工作表页数：1
