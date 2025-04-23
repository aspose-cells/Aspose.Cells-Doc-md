---
title: Lettura di valori di celle in thread multipli contemporaneamente
linktitle: Thread multipli
type: docs
weight: 1800
url: /it/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Impara come leggere i valori delle celle in più thread contemporaneamente attraverso l API Aspose.Cells for Node.js via C++.
keywords: Leggi i valori delle celle in più thread contemporaneamente Node.js via C++, Aspose.Cells C++ Multithread, Leggi dati in più thread
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

Per leggere i valori delle celle in più di un thread contemporaneamente, imposta [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) su **true**. Se non lo fai, potresti ottenere valori di cella sbagliati.

Il seguente codice:

1. Crea un workbook.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori di stringa.
1. Quindi crea due thread che leggono contemporaneamente valori da celle casuali.
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

allora viene visualizzato il seguente messaggio:

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
