---
title: Lectura de valores Cell en varios subprocesos simultáneamente
linktitle: Múltiples hilos
type: docs
weight: 1100
url: /es/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aprenda a leer valores Cell en varios subprocesos simultáneamente con las API Aspose.Cells for Java.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

La necesidad de leer valores de celda en varios subprocesos simultáneamente es un requisito común. Este artículo explica cómo utilizar Aspose.Cells para este propósito.

{{% /alert %}}

##  **Cómo leer valores Cell en varios subprocesos simultáneamente con Aspose.Cells for Java**

 Para leer valores de celda en más de un hilo simultáneamente, configure[**Hoja de trabajo.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)a *verdadero**. Si no lo hace, es posible que obtenga valores de celda incorrectos. Tenga en cuenta que algunas funciones, como el formato de valores de celda, no son compatibles con subprocesos múltiples. Por lo tanto, MultiThreadReading solo le permite acceder a los datos originales de la celda. En un entorno de subprocesos múltiples, si intenta obtener el valor formateado de la celda, como por Cell.getStringValue() para valores numéricos, puede obtener un resultado inesperado o una excepción.

El siguiente código:

1. Crea un libro de trabajo.
1. Agrega una hoja de trabajo.
1. Llena la hoja de trabajo con valores de cadena.
1. Luego crea dos subprocesos que leen simultáneamente valores de celdas aleatorias.
 Si los valores leídos son correctos no pasa nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

entonces se muestra el siguiente mensaje:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
