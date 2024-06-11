---
title: 在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载
type: docs
weight: 100
url: /zh/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能的使用场景**

Aspose.Cells允许你使用[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)对象在转换到PDF、HTML等各种格式时在消耗太多时间时停止转换。转换过程通常既使用CPU又使用内存，并且在资源有限时停止它通常是有用的。你可以使用[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)既停止转换又停止加载大型工作簿。请使用[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor)属性停止转换，使用[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor)属性加载大型工作簿。

## **在转换或加载花费太长时间时使用InterruptMonitor停止转换或加载**

以下示例代码解释了使用 [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) 对象的用法。该代码将大型Excel文件转换为PDF。由于这些代码行的原因，转换需要几秒钟（即*超过30秒*）。

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

正如您所见 **J1000000** 是XLSX文件中相当远的单元格。但是，**WaitForWhileAndThenInterrupt()** 方法在10秒后中断转换，程序结束/终止。请使用以下代码执行示例代码。

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
