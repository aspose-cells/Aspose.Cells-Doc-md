---
title: 监视运行程序
type: docs
weight: 20
url: /zh/python-net/monitor-running-programs/
---

## **如何监视运行中的程序**

以下示例代码显示了如何监视运行中的程序。此代码可用于监视与[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)有关的代码运行。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) 类创建一个监视对象，使用[setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) 函数将其添加到[LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/) 运行参数，然后使用[startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) 函数设置预期的中断时间（以毫秒为单位）。如果受监视代码的运行时间超过预期时间，程序将被中断并引发异常。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
