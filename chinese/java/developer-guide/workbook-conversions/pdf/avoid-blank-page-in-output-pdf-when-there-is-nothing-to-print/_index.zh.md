---
title: 在输出PDF中避免空白页当没有内容需要打印时
type: docs
weight: 30
url: /zh/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **可能的使用场景**

当Excel文件为空且用户使用Aspose.Cells将其保存为PDF时，在输出PDF中会呈现一张空白页。有时，这种默认行为是不希望的。Aspose.Cells提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)属性来处理这个问题。如果将其设置为**false**，那么[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)将在输出PDF中没有东西需要打印时发生。

## **在输出PDF中避免空白页当没有内容需要打印时**

以下示例代码创建一个空的工作簿，然后在将[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)属性设置为**false**后将其保存为输出PDF。因为在输出PDF中没有要打印的内容，所以[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)如下所示。

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
