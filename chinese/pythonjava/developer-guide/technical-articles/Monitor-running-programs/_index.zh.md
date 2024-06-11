---
title: 监视运行程序
type: docs
weight: 20
url: /zh/python-java/monitor-running-programs/
---

## **如何监视运行中的程序**

以下示例代码展示了如何监视运行中的程序。该代码可用于监视与[Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)相关的代码的运行。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor)类创建一个监视对象，使用[setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor)函数将其添加到[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)运行参数中，然后使用[startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int))函数设置预期的中断时间（毫秒为单位）。如果被监视的代码的运行时间超过预期时间，程序将被中断并抛出异常。

## **示例代码**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
