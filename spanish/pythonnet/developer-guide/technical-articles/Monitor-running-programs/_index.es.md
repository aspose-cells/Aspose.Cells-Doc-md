---
title: Monitorizar programas en ejecución
type: docs
weight: 20
url: /es/python-net/monitor-running-programs/
---

## **Cómo monitorizar un programa en ejecución**

El siguiente código de muestra muestra cómo monitorizar un programa en ejecución. Este código puede ser utilizado para monitorizar la ejecución de código relacionado con un [Libro de Trabajo](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/). Simplemente utiliza la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/) para crear un objeto de monitoreo, utiliza la función [setInterruptMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/interrupt_monitor/) para añadirlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/), y luego utiliza la función [startMonitor](https://reference.aspose.com/cells/python-net/aspose.cells/systemtimeinterruptmonitor/start_monitor/#int) para establecer el tiempo de interrupción esperado (en milisegundos). Si el tiempo de ejecución del código monitorizado excede el tiempo esperado, el programa se interrumpirá y se lanzará una excepción.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-python-net-TechnicalArticles-MonitorRunningPrograms.py" >}}
