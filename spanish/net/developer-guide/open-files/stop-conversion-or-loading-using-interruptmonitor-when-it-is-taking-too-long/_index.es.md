---
title: Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado
type: docs
weight: 100
url: /es/net/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Escenarios de uso posibles**

Aspose.Cells permite detener la conversión de libros de trabajo a varios formatos como PDF, HTML, etc. utilizando el objeto [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) cuando lleva demasiado tiempo. El proceso de conversión a menudo es intensivo en CPU y memoria, y a menudo es útil detenerlo cuando los recursos son limitados. Puede utilizar [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor) tanto para detener la conversión como para detener la carga de un libro de trabajo extenso. Utilice la propiedad [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/interruptmonitor) para detener la conversión y la propiedad [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/interruptmonitor) para cargar un libro de trabajo extenso.

## **Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado**

El siguiente código de muestra explica el uso del objeto [**InterruptMonitor**](https://reference.aspose.com/cells/net/aspose.cells/interruptmonitor). El código convierte un archivo de Excel bastante grande a PDF. Tomará varios segundos (es decir, *más de 30 segundos*) en convertirse debido a estas líneas de código.

{{< highlight csharp >}}

//Access cell J1000000 and add some text inside it.

Cell cell = ws.Cells["J1000000"];

cell.PutValue("This is text.");

{{< /highlight >}}

Como puede ver, **J1000000** es una celda bastante lejana en el archivo XLSX. Sin embargo, el método **WaitForWhileAndThenInterrupt()** interrumpe la conversión después de 10 segundos y el programa termina. Utilice el siguiente código para ejecutar el código de muestra.

{{< highlight csharp >}}

 new StopConversionOrLoadingUsingInterruptMonitor().TestRun();

{{< /highlight >}}

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-StopConversionOrLoadingUsingInterruptMonitor.cs" >}}
{{< app/cells/assistant language="csharp" >}}
