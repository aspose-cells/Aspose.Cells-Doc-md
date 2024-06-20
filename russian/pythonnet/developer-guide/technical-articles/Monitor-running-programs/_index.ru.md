---
title: Мониторинг работающих программ
type: docs
weight: 20
url: /ru/python-net/monitor-running-programs/
---

## **Как отслеживать работающую программу**

Приведенный ниже образец кода показывает, как отслеживать работающую программу. Этот код может быть использован для отслеживания выполнения кода, связанного с [рабочей книгой](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/). Просто используйте класс [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) для создания объекта отслеживания, используйте функцию [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) для добавления его в параметры выполнения [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/), а затем используйте функцию [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) для установки ожидаемого времени прерывания (в миллисекундах). Если время выполнения отслеживаемого кода превышает ожидаемое время, программа будет прервана, и будет сгенерировано исключение.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
