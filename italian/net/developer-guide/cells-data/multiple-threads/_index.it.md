---
title: Lettura dei valori Cell in più thread contemporaneamente
linktitle: Discussioni multiple
type: docs
weight: 1800
url: /it/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Scopri come leggere i valori Cell in più thread contemporaneamente tramite Aspose.Cells for .NET API.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in più thread contemporaneamente è un requisito comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

 Per leggere i valori delle celle in più thread contemporaneamente, impostare[**Foglio di lavoro.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)a *vero**. In caso contrario, potresti ottenere valori di cella errati.

Il seguente codice:

1. Crea una cartella di lavoro.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori stringa.
1. Quindi crea due thread che leggono simultaneamente valori da celle casuali.
 Se i valori letti sono corretti non succede nulla. Se i valori letti non sono corretti viene visualizzato un messaggio.

Se commenti questa riga:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

quindi viene visualizzato il seguente messaggio:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Altrimenti il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
