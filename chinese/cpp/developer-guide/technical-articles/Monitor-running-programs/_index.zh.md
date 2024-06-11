---
title: 监控运行中的程序
type: docs
weight: 20
url: /zh/cpp/Monitor-running-programs/
---

## **如何监控运行中的程序**

以下示例代码显示了如何监控运行中的程序。此代码可用于监控与[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)相关的代码运行。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/)类创建一个监控对象，使用[SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/)函数将其添加到[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)运行参数，并使用[StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/)函数设置预期的中断时间（毫秒）。如果监控代码的运行时间超过预期时间，程序将被中断，并引发异常。

## **示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
