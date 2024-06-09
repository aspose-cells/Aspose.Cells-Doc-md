---
title: Monitor running programs
type: docs
weight: 20
url: /cpp/Monitor-running-programs/
---

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the running of [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) class to create a monitoring object, use the [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) function to add it to the [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) running parameters, and then use the [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted and an exception will be thrown.

## **Sample Code**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
