---
title: Stop conversion or loading using InterruptMonitor when it is taking too long with Golang via C++
linktitle: Stop conversion or loading using InterruptMonitor
type: docs
weight: 100
url: /go-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
description: Learn how to stop conversion or loading of large Excel files using InterruptMonitor in Aspose.Cells with Golang via C++.
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to stop the conversion of a Workbook to various formats like PDF, HTML, etc., using the [**InterruptMonitor**](https://reference.aspose.com/cells/go-cpp/interruptmonitor/) object when it is taking too long. The conversion process is often both CPU‑ and memory‑intensive, and it is useful to halt it when resources are limited. You can use [**InterruptMonitor**](https://reference.aspose.com/cells/go-cpp/interruptmonitor/) both for stopping conversion as well as for stopping the loading of huge workbooks. Please use the [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/go-cpp/workbook/getinterruptmonitor/) property for stopping conversion and the [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/go-cpp/loadoptions/getinterruptmonitor/) property for loading huge workbooks.

## **Stop conversion or loading using InterruptMonitor when it is taking too long**

The following sample code explains the usage of the [**InterruptMonitor**](https://reference.aspose.com/cells/go-cpp/interruptmonitor/) object. The code converts a quite large Excel file to PDF. It will take several seconds (i.e., *more than 30 seconds*) to get it converted because of these lines of code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-StopConversionOrLoadingUsingInterruptmonitorWhenItIsTakingTooLong.go" >}}

As you see, **J1000000** is quite a far cell in the XLSX file. However, the **WaitForWhileAndThenInterrupt()** method interrupts the conversion after 10 seconds, and the program ends/terminates. Please use the following code to execute the sample code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-StopConversionOrLoadingUsingInterruptmonitorWhenItIsTakingTooLong-1.go" >}}

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-StopConversionOrLoadingUsingInterruptmonitorWhenItIsTakingTooLong-2.go" >}}
{{< app/cells/assistant language="go" >}}
