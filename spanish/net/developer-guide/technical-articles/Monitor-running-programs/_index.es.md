---
title: Monitorizar programas en ejecución
type: docs
weight: 20
url: /es/net/Monitor-running-programs/
---

## **Cómo monitorizar un programa en ejecución**

El siguiente código de ejemplo muestra cómo monitorear un programa en ejecución. Este código se puede utilizar para monitorear la ejecución del código relacionado con el [Libro de trabajo](https://reference.aspose.com/cells/net/aspose.cells/workbook/). Simplemente use la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/) para crear un objeto de monitoreo, use la función [SetInterruptMonitor](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/interruptmonitor/) para agregarlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/) y luego use la función [StartMonitor](https://reference.aspose.com/cells/net/aspose.cells/systemtimeinterruptmonitor/startmonitor/) para establecer el tiempo de interrupción esperado (en milisegundos). Si el tiempo de ejecución del código monitoreado excede el tiempo esperado, el programa será interrumpido y se generará una excepción.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-TechnicalArticles-MonitorRunningPrograms.cs" >}}
{{< app/cells/assistant language="csharp" >}}
