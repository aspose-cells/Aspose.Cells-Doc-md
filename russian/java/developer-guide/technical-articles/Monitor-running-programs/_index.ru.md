---
title: Мониторинг работающих программ
type: docs
weight: 20
url: /ru/java/Monitor-running-programs/
---

## **Как отслеживать работающую программу**

Приведенный ниже образец кода показывает, как отслеживать работу программы. Этот код может использоваться для мониторинга выполнения кода, связанного с [Книгой Excel](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/). Просто используйте класс [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/), чтобы создать объект мониторинга, используйте функцию [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-), чтобы добавить его к параметрам выполнения [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/), а затем используйте функцию [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) для установки ожидаемого времени прерывания (в миллисекундах). Если время выполнения отслеживаемого кода превышает ожидаемое время, программа будет прервана, и будет сгенерировано исключение.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
