---
title: 在处理时间过长时使用InterruptMonitor停止转换或加载
type: docs
weight: 100
url: /zh/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **可能的使用场景**

Aspose.Cells允许您使用[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)对象停止将工作簿转换为PDF、HTML等各种格式的过程，当它占用时间过长时。转换过程通常既是CPU又是内存密集型的，因此在资源有限时将其停止是很有用的。您可以同时用于停止转换以及停止加载大型工作簿。请使用[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor)属性停止转换和[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor)属性加载大型工作簿。

## **在处理时间过长时使用InterruptMonitor停止转换或加载**

以下示例代码解释了[**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor)对象的用法。代码将一个非常大的Excel文件转换为PDF。由于这些代码行，转换将需要几秒钟（即*超过30秒*）才能完成。

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

正如您所看到的**J1000000**是XLSX文件中较远的单元格。然而，**WaitForWhileAndThenInterrupt()**方法会在10秒后中断转换，程序结束/终止。请使用以下代码执行示例代码。

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
