---
title: 工作簿和工作表打印预览
type: docs
weight: 130
url: /zh/java/workbook-and-worksheet-print-preview/
---
## **使用场景**

可能会有数百万页的 Excel 文件需要转换为 PDF 或图像的情况。处理此类文件将消耗大量时间和资源。在这种情况下，工作簿和工作表打印预览功能可能会很有用。在转换此类文件之前，用户可以检查总页数，然后决定是否转换文件。本文着重于使用[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类找出总页数。

## **工作簿和工作表打印预览**

Aspose.Cells 提供打印预览功能。为此，API 提供[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类。要创建整个工作簿的打印预览，请创建[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)通过类[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)和[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)对象到构造函数。这[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)类提供了一个[**评估页数**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)返回生成的预览中的页数的方法。如同[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)类，[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类用于为特定工作表生成打印预览。要创建工作表的打印预览，请创建[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)通过类[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)和[**图像或打印选项**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)对象到构造函数。这[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)类还提供了一个[**评估页数**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)返回生成的预览中的页数的方法。

下面的代码片段演示了两者的使用[**工作簿打印预览**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)和[**单张印刷预览**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)通过使用类[示例 excel 文件](Book1.xlsx).

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

以下是执行上述代码生成的输出。

### **控制台输出**

工作簿页数：1</br>
工作表页数：1
