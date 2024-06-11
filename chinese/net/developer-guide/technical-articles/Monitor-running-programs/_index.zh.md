---
title: 监视运行程序
type: docs
weight: 20
url: /zh/net/Monitor-running-programs/
---

## **如何监视运行中的程序**

以下示例代码展示了如何监视运行中的程序。该代码可用于监视与[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook/)相关的代码的运行。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/)类创建一个监视对象，使用[SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/)函数将其添加到[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/)运行参数中，然后使用[StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/)函数设置预期的中断时间（毫秒为单位）。如果被监视的代码的运行时间超过预期时间，程序将被中断并抛出异常。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
