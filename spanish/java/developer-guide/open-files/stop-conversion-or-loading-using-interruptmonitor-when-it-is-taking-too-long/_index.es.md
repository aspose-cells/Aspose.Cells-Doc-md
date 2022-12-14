---
title: Detenga la conversión o la carga con InterruptMonitor cuando tarde demasiado
type: docs
weight: 100
url: /es/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/
---
## **Posibles escenarios de uso**

Aspose.Cells le permite detener la conversión de Workbook a varios formatos como PDF, HTML, etc. usando el[**InterrumpirMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objeto cuando está tardando demasiado. El proceso de conversión suele hacer un uso intensivo de la CPU y la memoria y suele ser útil detenerlo cuando los recursos son limitados. Puedes usar[**InterrumpirMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)tanto para detener la conversión como para dejar de cargar un libro de trabajo enorme. Por favor use[**Workbook.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#InterruptMonitor)propiedad para detener la conversión y[**LoadOptions.InterruptMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#InterruptMonitor)propiedad para cargar un libro de trabajo enorme.

## **Detenga la conversión o la carga con InterruptMonitor cuando tarde demasiado**

El siguiente código de ejemplo explica el uso de[**InterrumpirMonitor**](https://reference.aspose.com/cells/java/com.aspose.cells/InterruptMonitor)objeto. El código convierte un archivo de Excel bastante grande a PDF. Tardará varios segundos (es decir,*más de 30 segundos*) para convertirlo debido a estas líneas de código.

{{< highlight "java" >}}

//Access cell AB1000000 and add some text inside it.

Cell cell = ws.getCells().get("AB1000000");

cell.putValue("This is text.");

{{< /highlight >}}

Como ves**AB1000000**es una celda bastante más lejana en el archivo XLSX. sin embargo, el*WaitForWhileAndThenInterrupt()*El método interrumpe la conversión después de 10 segundos y el programa termina/finaliza. Utilice el siguiente código para ejecutar el código de muestra.

{{< highlight "java" >}}

new StopConversionOrLoadingUsingInterruptMonitor().testRun();

{{< /highlight >}}

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-StopConversionOrLoadingUsingInterruptMonitor-1.java" >}}
