---
title: Monitor running programs
type: docs
weight: 20
url: /go-cpp/Monitor-running-programs/
---

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the execution of **Workbook**‑related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/go-cpp/systemtimeinterruptmonitor/) class to create a monitoring object, use the [SetInterruptMonitor](https://reference.aspose.com/cells/go-cpp/loadoptions/setinterruptmonitor/) function to add it to the [LoadOptions](https://reference.aspose.com/cells/go-cpp/loadoptions/) parameters, and then use the [StartMonitor](https://reference.aspose.com/cells/go-cpp/systemtimeinterruptmonitor/startmonitor/) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted and an exception will be thrown.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MonitorRunningPrograms.go" >}}
{{< app/cells/assistant language="go" >}}


