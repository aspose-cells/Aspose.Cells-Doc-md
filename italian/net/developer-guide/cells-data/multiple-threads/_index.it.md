---
title: Lettura di valori di celle in thread multipli contemporaneamente
linktitle: Thread multipli
type: docs
weight: 1800
url: /it/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Scopri come leggere i valori di celle in Thread Multipli contemporaneamente tramite l API Aspose.Cells for .NET.
keywords: Leggi i valori di celle in thread multipli contemporaneamente, Aspose.Cells C# Thread Multipli, Leggi dati in thread multipli
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

Per leggere i valori delle celle in più di un thread contemporaneamente, impostare [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) su **true**. In caso contrario, si potrebbero ottenere valori di celle errati.

Il seguente codice:

1. Crea un workbook.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori di stringa.
1. Quindi crea due thread che leggono contemporaneamente valori da celle casuali.
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

allora viene visualizzato il seguente messaggio:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
