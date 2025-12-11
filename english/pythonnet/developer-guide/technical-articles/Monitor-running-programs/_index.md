---
title: Monitor running programs
type: docs
weight: 20
url: /python-net/monitor-running-programs/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the execution of Workbook‑related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) class to create a monitoring object, use the [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) function to add it to the [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) parameters, and then use the [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted and an exception will be thrown.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
{{< app/cells/assistant language="python-net" >}}
