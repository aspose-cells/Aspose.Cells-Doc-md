---
title: 监控运行中的程序
type: docs
weight: 20
url: /zh/java/Monitor-running-programs/
---

## **如何监控运行中的程序**

以下示例代码显示了如何监控运行中的程序。此代码可用于监控与[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/)相关的代码运行。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/)类创建一个监控对象，使用[SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-)函数将其添加到[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/)运行参数中，然后使用[StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-)函数设置预期中断时间（以毫秒为单位）。如果受监视代码的运行时间超过预期时间，程序将被中断并抛出异常。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
