---
title: Lectura de valores de celda en múltiples hilos simultáneamente
linktitle: Hilos múltiples
type: docs
weight: 1100
url: /es/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Aprenda a leer valores de celda en hilos múltiples simultáneamente con Aspose.Cells for Java APIs.
keywords: Leer valores de celda en hilos múltiples simultáneamente en Java, Hilos múltiples para Aspose.Cells for Java APIs.
---

{{% alert color="primary" %}}

Necesitar leer valores de celda en múltiples hilos simultáneamente es un requisito común. Este artículo explica cómo usar Aspose.Cells para este propósito.

{{% /alert %}}

## **Cómo leer valores de celda en hilos múltiples simultáneamente con Aspose.Cells for Java**

Para leer valores de celda en más de un hilo simultáneamente, configure [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) a **true**. De lo contrario, puede obtener valores de celda incorrectos. Tenga en cuenta que algunas funciones, como dar formato a los valores de las celdas, no son compatibles con múltiples hilos. Por lo tanto, la lectura en varios hilos solo le permite acceder a los datos originales de las celdas. En un entorno de varios hilos, si intenta obtener el valor formateado de la celda, como usando Cell.getStringValue() para valores numéricos, es posible que obtenga un resultado inesperado o una excepción.

El siguiente código:

1. Crea un libro de trabajo.
1. Agrega una hoja de cálculo.
1. Rellena la hoja de cálculo con valores de cadena.
1. Luego crea dos hilos que leen valores simultáneamente de celdas aleatorias.
   Si los valores leídos son correctos, no sucede nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

entonces se muestra el siguiente mensaje:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
