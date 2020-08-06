---
title: Stop conversion or loading using InterruptMonitor when it is taking too long
type: docs
weight: 100
url: /java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Possible Usage Scenarios**
Aspose.Cells allows you to stop conversion of Workbook to various formats like PDF, HTML, etc. using the [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) object when it is taking too long. The conversion process is often both CPU and Memory intensive and it is often useful to halt it when resources are limited. You can use [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) both for stopping conversion as well as to stop loading huge workbook. Please use [Workbook.InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#InterruptMonitor) property for stopping conversion and [LoadOptions.InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/loadoptions#InterruptMonitor) property for loading huge workbook. 
## **Stop conversion or loading using InterruptMonitor when it is taking too long**
The following sample code explains the usage of [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) object. The code converts quite a large Excel file to PDF. It will take several seconds (i.e. *more than 30 seconds*) to get it converted because of these lines of code.

{{< highlight java >}}

 //Access cell AB1000000 and add some text inside it.

Cell cell = ws.Cells["AB1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

As you see **AB1000000** is quite a farther cell in XLSX file. However, the *WaitForWhileAndThenInterrupt()* method interrupts the conversion after 10 seconds and program ends/terminates. Please use the following code to execute the sample code.

{{< highlight java >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}
## **Sample Code**
{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
