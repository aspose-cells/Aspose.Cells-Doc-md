---
title: Мониторинг работающих программ
type: docs
weight: 20
url: /ru/python-java/monitor-running-programs/
---

## **Как отслеживать работающую программу**

В следующем образце кода показано, как отслеживать запущенную программу. Этот код может использоваться для мониторинга выполнения связанного с книгой кода. Просто используйте класс SystemTimeInterruptMonitor для создания объекта мониторинга, используйте функцию setInterruptMonitor для добавления его к параметрам выполнения LoadOptions, а затем используйте функцию startMonitor для установки ожидаемого времени прерывания (в миллисекундах). Если работа мониторируемого кода превышает ожидаемое время, программа будет прервана, и будет вызвано исключение.

## **Образец кода**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
