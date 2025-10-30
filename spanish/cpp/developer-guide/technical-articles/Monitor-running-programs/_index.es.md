---
title: Monitorizar programas en ejecución
type: docs
weight: 20
url: /es/cpp/Monitor-running-programs/
---

## **Cómo monitorizar un programa en ejecución**

El siguiente código de muestra muestra cómo monitorear un programa en ejecución. Este código se puede usar para monitorear la ejecución de código relacionado con [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Simplemente use la clase [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/) para crear un objeto de monitoreo, use la función [SetInterruptMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setinterruptmonitor/) para añadirlo a los parámetros de ejecución de [LoadOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/), y luego use la función [StartMonitor](https://reference.aspose.com/cells/cpp/aspose.cells/systemtimeinterruptmonitor/startmonitor/) para establecer el tiempo de interrupción esperado (en milisegundos). Si el tiempo de ejecución del código monitoreado excede el tiempo esperado, el programa será interrumpido y se lanzará una excepción.

## **Código de muestra**

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-TechnicalArticles-MonitorRunningPrograms.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
