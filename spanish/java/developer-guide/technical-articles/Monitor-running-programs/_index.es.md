---
title: Monitorizar programas en ejecución
type: docs
weight: 20
url: /es/java/Monitor-running-programs/
---

## **Cómo monitorizar un programa en ejecución**

El siguiente código de ejemplo muestra cómo monitorear un programa en ejecución. Este código puede utilizarse para monitorear la ejecución del código relacionado con [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook/). Simplemente utilice la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/) para crear un objeto de monitoreo, utilice la función [SetInterruptMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/#setInterruptMonitor-com.aspose.cells.AbstractInterruptMonitor-) para agregarlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions/), y luego utilice la función [StartMonitor](https://reference.aspose.com/cells/java/com.aspose.cells/systemtimeinterruptmonitor/#startMonitor-int-) para establecer el tiempo de interrupción esperado (en milisegundos). Si el tiempo de ejecución del código monitoreado excede el tiempo esperado, el programa se interrumpirá y se generará una excepción.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-TechnicalArticles-MonitorRunningPrograms.java" >}}
{{< app/cells/assistant language="java" >}}
