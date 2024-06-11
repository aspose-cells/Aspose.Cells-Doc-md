---
title: 在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载
type: docs
weight: 100
url: /zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能的使用场景**

Aspose.Cells允许您在使用转换Workbook为PDF、HTML等各种格式时使用[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)对象当转换时间过长时停止转换。转换过程通常既具有CPU又具有内存密集型，当资源有限时停止转换通常是有用的。您可以使用[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)既用于停止转换又用于停止加载巨大的工作簿。请使用[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)属性停止转换，使用[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)属性加载巨大的工作簿。

## **在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载**

以下示例代码说明了 [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) 对象的用法。该代码将一个非常大的 Excel 文件转换为 PDF。由于这些代码行，它需要数秒（即 *超过 30 秒*）来完成转换。

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

如您所见，**AB1000000** 在 XLSX 文件中是相对较远的单元格。然而，*WaitForWhileAndThenInterrupt()* 方法在 10 秒后中断转换，程序结束/终止。请使用以下代码来执行示例代码。

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
