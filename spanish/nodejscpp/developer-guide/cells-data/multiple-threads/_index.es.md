---
title: Lectura de valores de celda en múltiples hilos simultáneamente
linktitle: Hilos múltiples
type: docs
weight: 1800
url: /es/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Aprende cómo leer valores de celdas en múltiples hilos simultáneamente a través de la API Aspose.Cells for Node.js via C++.
keywords: Leer valores de celdas en múltiples hilos simultáneamente Node.js vía C++, Aspose.Cells C++ múltiples hilos, leer datos en múltiples hilos
---

{{% alert color="primary" %}}

Necesitar leer valores de celda en múltiples hilos simultáneamente es un requisito común. Este artículo explica cómo usar Aspose.Cells para este propósito.

{{% /alert %}}

Para leer valores de celdas en más de un hilo simultáneamente, configura [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) en **true**. Si no, podrías obtener valores incorrectos de las celdas.

El siguiente código:

1. Crea un libro de trabajo.
1. Agrega una hoja de cálculo.
1. Rellena la hoja de cálculo con valores de cadena.
1. Luego crea dos hilos que leen valores simultáneamente de celdas aleatorias.
   Si los valores leídos son correctos, no sucede nada. Si los valores leídos son incorrectos, se muestra un mensaje.

Si comentas esta línea:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

entonces se muestra el siguiente mensaje:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

De lo contrario, el programa se ejecuta sin mostrar ningún mensaje, lo que significa que todos los valores leídos de las celdas son correctos.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
