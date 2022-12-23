---
title: 当时间过长时使用 InterruptMonitor 停止转换或加载
type: docs
weight: 100
url: /zh/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **可能的使用场景**

Aspose.Cells 允许您停止将工作簿转换为各种格式，如 PDF、HTML 等，使用[**中断监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)反对时间太长。转换过程通常是 CPU 和内存密集型的，当资源有限时停止它通常很有用。您可以使用[**中断监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)既可以停止转换，也可以停止加载庞大的工作簿。请用[**工作簿.中断监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)停止转换的属性和[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)用于加载巨大工作簿的属性。

## **当时间过长时使用 InterruptMonitor 停止转换或加载**

下面的示例代码解释了[**中断监视器**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)目的。该代码将相当大的 Excel 文件转换为 PDF。这将需要几秒钟（即*超过 30 秒*因为这些代码行而将其转换。

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

如你所见**AB1000000**是 XLSX 文件中相当远的单元格。然而*WaitForWhileAndThenInterrupt()*方法在 10 秒后中断转换，程序结束/终止。请使用以下代码来执行示例代码。

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
