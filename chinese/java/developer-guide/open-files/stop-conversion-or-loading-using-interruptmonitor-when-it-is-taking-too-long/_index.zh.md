---
title: 在处理时间过长时使用InterruptMonitor停止转换或加载
type: docs
weight: 100
url: /zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能的使用场景**

Aspose.Cells允许您使用[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)对象在转换工作簿为PDF、HTML等各种格式时，当转换时间太长时中止。转换过程通常既消耗CPU又消耗内存，当资源有限时，中止转换是很有用的。您可以使用[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)既用于中止转换，也用于中止加载大型工作簿。请使用[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)属性来中止转换，使用[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)属性来加载大型工作簿。

## **在处理时间过长时使用InterruptMonitor停止转换或加载**

以下示例代码解释了[**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)对象的用法。该代码将一个相当大的Excel文件转换为PDF。由于这些代码行的原因，它将需要几秒钟（即*超过30秒*）才能进行转换。

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

正如您所看到的**AB1000000**是XLSX文件中相当远的单元格。然而，*WaitForWhileAndThenInterrupt()*方法在10秒后中断转换，程序结束/终止。请使用以下代码执行示例代码。

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
