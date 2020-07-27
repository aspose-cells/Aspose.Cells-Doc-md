+++
title = "Stop conversion or loading using InterruptMonitor when it is taking too long" 
description = "" 
weight = 12109 
+++

Aspose.Cells for Java : Stop conversion or loading using InterruptMonitor when it is taking too long  

# Aspose.Cells for Java : Stop conversion or loading using InterruptMonitor when it is taking too long


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#StopconversionorloadingusingInterruptMonitorwhenitistakingtoolong-PossibleUsageScenarios)
*   2 [Stop conversion or loading using InterruptMonitor when it is taking too long](#StopconversionorloadingusingInterruptMonitorwhenitistakingtoolong-StopconversionorloadingusingInterruptMonitorwhenitistakingtoolong)
*   3 [Sample Code](#StopconversionorloadingusingInterruptMonitorwhenitistakingtoolong-SampleCode)
{{< /panel >}}
 

## Possible Usage Scenarios

Aspose.Cells allows you to stop conversion of Workbook to various formats like PDF, HTML, etc. using the [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) object when it is taking too long. The conversion process is often both CPU and Memory intensive and it is often useful to halt it when resources are limited. You can use [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) both for stopping conversion as well as to stop loading huge workbook. Please use [Workbook.InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/workbook#InterruptMonitor) property for stopping conversion and [LoadOptions.InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/loadoptions#InterruptMonitor) property for loading huge workbook. 

## Stop conversion or loading using InterruptMonitor when it is taking too long

The following sample code explains the usage of [InterruptMonitor](https://apireference.aspose.com/java/cells/com.aspose.cells/InterruptMonitor) object. The code converts quite a large Excel file to PDF. It will take several seconds (i.e. *more than 30 seconds*) to get it converted because of these lines of code.

{{< code lang="cs" >}}
//Access cell AB1000000 and add some text inside it.
Cell cell = ws.Cells["AB1000000"];
cell.PutValue("This is text.");
{{< /code >}}

As you see **AB1000000** is quite a farther cell in XLSX file. However, the *WaitForWhileAndThenInterrupt()* method interrupts the conversion after 10 seconds and program ends/terminates. Please use the following code to execute the sample code.

{{< code lang="cs" >}}
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
{{< /code >}}

## Sample Code

