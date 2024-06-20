---
title: Мониторинг работающих программ
type: docs
weight: 20
url: /ru/net/Monitor-running-programs/
---

## **Как отслеживать работающую программу**

Нижеприведенный образец кода показывает, как отслеживать запущенную программу. Этот код может использоваться для отслеживания выполнения кода, связанного с [рабочей книгой](https://reference.aspose.com/cells/net/aspose.cells/workbook/). Просто используйте класс [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) для создания объекта отслеживания, используйте функцию [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) для добавления его в параметры выполнения [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/), а затем используйте функцию [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) для установки ожидаемого времени прерывания (в миллисекундах). Если время выполнения отслеживаемого кода превышает ожидаемое время, программа будет прервана, и будет сгенерировано исключение.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
