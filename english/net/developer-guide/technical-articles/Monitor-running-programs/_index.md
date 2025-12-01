---
title: Monitor running programs
type: docs
weight: 20
url: /net/Monitor-running-programs/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **How to monitor a running program**

The following sample code shows how to monitor a running program. This code can be used to monitor the running of [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/) related code. Simply use the [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) class to create a monitoring object, use the [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) function to add it to the [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/) running parameters, and then use the [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) function to set the expected interruption time (in milliseconds). If the running time of the monitored code exceeds the expected time, the program will be interrupted and an exception will be thrown.

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
{{< app/cells/assistant language="csharp" >}}
