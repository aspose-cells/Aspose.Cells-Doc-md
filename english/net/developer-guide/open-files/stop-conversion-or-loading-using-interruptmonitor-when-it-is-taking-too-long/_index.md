---
title: Stop conversion or loading using InterruptMonitor when it is taking too long
type: docs
weight: 100
url: /net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to stop the conversion of a Workbook to various formats, such as PDF, HTML, etc., using the [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) object when it is taking too long. The conversion process is often both CPU‑ and memory‑intensive, and it is useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) both for stopping conversion and for loading a huge workbook. Please use the [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) property for stopping conversion and the [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) property for loading a huge workbook.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of the [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) object. The code converts a fairly large Excel file to PDF. It will take several seconds (i.e., *more than 30 seconds*) to be converted because of these lines of code.

{{< highlight csharp >}}

// Access cell J1000000 and add some text to it.

Cell cell = ws.Cells["J1000000"];
cell.PutValue("This is text.");

{{< /highlight >}}

As you can see, **J1000000** is a faraway cell in the XLSX file. However, the **WaitForWhileAndThenInterrupt()** method interrupts the conversion after 10 seconds, and the program ends/terminates. Please use the following code to run the sample code.

{{< highlight csharp >}}
new StopConversionOrLoadingUsingInterruptMonitor().TestRun();
{{< /highlight >}}

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
