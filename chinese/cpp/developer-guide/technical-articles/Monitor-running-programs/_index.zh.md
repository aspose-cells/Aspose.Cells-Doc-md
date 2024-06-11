---
title: 监视运行程序
type: docs
weight: 20
url: /zh/cpp/Monitor-running-programs/
---

## **如何监视运行中的程序**

以下示例代码显示如何监视正在运行的程序。 这段代码可用于监视有关[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)的代码运行。 只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/)类创建一个监视对象，使用[SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/)函数将其添加到[LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)运行参数中，然后使用[StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/)函数设置预期中断时间（毫秒）。 如果受监视的代码运行时间超过预期时间，程序将被中断并抛出异常。

## **示例代码**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
