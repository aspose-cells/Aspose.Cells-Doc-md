---
title: 当没有可打印的内容时，避免在输出 PDF 中出现空白页
type: docs
weight: 30
url: /zh/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **可能的使用场景**

当 Excel 文件为空并且用户使用 Aspose.Cells 将其保存为 PDF 时，它会在输出 PDF 中呈现空白页面。有时，这种默认行为是不可取的。 Aspose.Cells 提供了[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)财产来处理这个问题。如果你将它设置为**错误的**， 然后[**细胞异常**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)只要输出的 PDF 中没有可打印的内容，就会发生。

## **当没有可打印的内容时，避免在输出 PDF 中出现空白页**

以下示例代码创建一个空工作簿，然后在设置[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)财产作为**错误的**.由于输出的 PDF 中没有要打印的内容，因此[**细胞异常**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)发生如下所示。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **例外**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
