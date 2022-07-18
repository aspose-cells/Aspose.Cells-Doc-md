---
title: Stop conversion or loading using InterruptMonitor when it is taking too long
type: docs
weight: 100
url: /net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to stop the conversion of Workbook to various formats like PDF, HTML etc. using the [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) object when it is taking too long. The conversion process is often both CPU and Memory intensive and it is often useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) both for stopping conversion as well as to stop loading huge workbook. Please use [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) property for stopping conversion and [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) property for loading huge workbook.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) object. The code converts quite a large Excel file to PDF. It will take several seconds (i.e. *more than 30 seconds*) to get it converted because of these lines of code.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

As you see **J1000000** is quite a farther cell in XLSX file. However, the **WaitForWhileAndThenInterrupt()** method interrupts the conversion after 10 seconds and program ends/terminates. Please use the following code to execute the sample code.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
