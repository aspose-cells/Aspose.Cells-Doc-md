---
title: 避免输出PDF中的空白页在没有内容打印时
type: docs
weight: 30
url: /zh/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能的使用场景**

当Excel文件为空且用户将其保存为PDF使用Aspose.Cells时，在输出PDF中会呈现空白页。有时，这种默认行为是不希望的。Aspose.Cells提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)属性来处理此问题。如果将其设置为false，则在输出PDF中没有打印内容时将会发生[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)

## **当没有需要打印的内容时，避免在输出PDF中出现空白页**

以下示例代码创建一个空工作簿，然后在将[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)属性设置为false后将其保存为输出PDF。由于输出PDF中没有打印内容，将会发生如下[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **异常**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
