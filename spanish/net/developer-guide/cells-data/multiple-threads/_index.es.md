---
title: Lectura de valores de celda en múltiples hilos simultáneamente
linktitle: Hilos múltiples
type: docs
weight: 1800
url: /es/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aprende cómo leer valores de celda en múltiples hilos simultáneamente a través de la API Aspose.Cells for .NET.
keywords: Leer valores de celda en múltiples hilos simultáneamente, Aspose.Cells C# Múltiples Hilos, Leer datos en Múltiples Hilos
---

{{% alert color="primary" %}}

Necesitar leer valores de celda en múltiples hilos simultáneamente es un requisito común. Este artículo explica cómo usar Aspose.Cells para este propósito.

{{% /alert %}}

Para leer valores de celda en más de un hilo simultáneamente, establece [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) a **verdadero**. Si no lo haces, podrías obtener valores de celda incorrectos.

El siguiente código:

1. Crea un libro de trabajo.
1. Agrega una hoja de cálculo.
1. Rellena la hoja de cálculo con valores de cadena.
1. Luego crea dos hilos que leen valores simultáneamente de celdas aleatorias.
   Si los valores leídos son correctos, no sucede nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

entonces se muestra el siguiente mensaje:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
