---
title: Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado
type: docs
weight: 100
url: /es/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite detener la conversión del libro a varios formatos como PDF, HTML, etc. utilizando el objeto [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) cuando está tardando demasiado. El proceso de conversión suele ser intensivo en CPU y memoria, por lo que es útil detenerlo cuando los recursos son limitados. Se puede utilizar [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor) tanto para detener la conversión como para detener la carga de un libro grande. Por favor, utiliza la propiedad [**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor) para detener la conversión y la propiedad [**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor) para cargar un libro grande.

## **Detener la conversión o carga utilizando InterruptMonitor cuando está tardando demasiado**

El siguiente código de ejemplo explica el uso del objeto [**InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor). El código convierte un archivo de Excel bastante grande a PDF. Tomará varios segundos (es decir, *más de 30 segundos*) para convertirlo debido a estas líneas de código.

{{< highlight java >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Como se ve, **AB1000000** es una celda bastante alejada en el archivo XLSX. Sin embargo, el método *WaitForWhileAndThenInterrupt()* interrumpe la conversión después de 10 segundos y el programa finaliza/termina. Por favor, utiliza el siguiente código para ejecutar el código de ejemplo.

{{< highlight java >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
{{< app/cells/assistant language="java" >}}
