---
title: Lectura de valores Cell en múltiples subprocesos simultáneamente
linktitle: Múltiples subprocesos
type: docs
weight: 1800
url: /es/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

La necesidad de leer valores de celda en varios subprocesos simultáneamente es un requisito común. Este artículo explica cómo usar Aspose.Cells para este propósito.

{{% /alert %}}

 Para leer valores de celda en más de un subproceso simultáneamente, configure[**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) a**verdadero**. Si no lo hace, es posible que obtenga valores de celda incorrectos.

El siguiente código:

1. Crea un libro de trabajo.
1. Agrega una hoja de trabajo.
1. Llena la hoja de cálculo con valores de cadena.
1. Luego crea dos subprocesos que leen simultáneamente valores de celdas aleatorias.
 Si los valores leídos son correctos, no pasa nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

luego se muestra el siguiente mensaje:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
