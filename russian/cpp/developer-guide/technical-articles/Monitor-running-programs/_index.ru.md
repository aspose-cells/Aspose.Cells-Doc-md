---
title: Мониторинг работающих программ
type: docs
weight: 20
url: /ru/cpp/Monitor-running-programs/
---

## **Как отслеживать работающую программу**

Приведенный ниже образец кода показывает, как отслеживать работу программы. Этот код может быть использован для мониторинга выполнения кода, связанного с [рабочей книгой](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Просто используйте класс [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/), чтобы создать объект мониторинга, используйте функцию [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) для добавления его к параметрам выполнения [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) и затем используйте функцию [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) для задания ожидаемого времени прерывания (в миллисекундах). Если время работы контролируемого кода превысит ожидаемое время, программа будет прервана, и будет сгенерировано исключение.

## **Образец кода**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
