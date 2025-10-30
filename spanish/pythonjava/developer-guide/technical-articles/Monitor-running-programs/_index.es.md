---
title: Monitorizar programas en ejecución
type: docs
weight: 10
url: /es/python-java/monitor-running-programs/
---

## **Cómo monitorizar un programa en ejecución**

El siguiente código de muestra muestra cómo monitorear un programa en ejecución. Este código se puede utilizar para monitorear la ejecución de código relacionado con [Workbook](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Simplemente use la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/SystemTimeInterruptMonitor) para crear un objeto de monitoreo, use la función [setInterruptMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/loadoptions#InterruptMonitor) para agregarlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions), y luego utilice la función [startMonitor](https://reference.aspose.com/cells/python-java/asposecells.api/systemtimeinterruptmonitor#startMonitor(int)) para establecer el tiempo de interrupción esperado (en milisegundos). Si el tiempo de ejecución del código monitoreado supera el tiempo esperado, el programa se interrumpirá y se generará una excepción.

## **Código de muestra**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-python-java-TechnicalArticles-MonitorRunningPrograms.py" >}}
