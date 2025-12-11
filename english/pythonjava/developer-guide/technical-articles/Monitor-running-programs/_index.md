---
title: Monitor running programs
type: docs
weight: 10
url: /python-java/monitor-running-programs/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the execution of Workbook‑related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) class to create a monitoring object, use the [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) function to add it to the [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) running parameters, and then use the [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted, and an exception will be thrown.

## **Sample Code**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
