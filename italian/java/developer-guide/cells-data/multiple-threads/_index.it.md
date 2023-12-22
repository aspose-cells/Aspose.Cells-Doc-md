---
title: Lettura dei valori Cell in più thread contemporaneamente
linktitle: Discussioni multiple
type: docs
weight: 1100
url: /it/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Scopri come leggere i valori Cell in più thread contemporaneamente con le API Aspose.Cells for Java.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in più thread contemporaneamente è un requisito comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

##  **Come leggere i valori Cell in più thread contemporaneamente con Aspose.Cells for Java**

 Per leggere i valori delle celle in più thread contemporaneamente, impostare[**Foglio di lavoro.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)a *vero**. In caso contrario, potresti ottenere valori di cella errati. Tieni presente che alcune funzionalità come la formattazione dei valori delle celle non sono supportate per thread multipli. Pertanto MultiThreadReading ti consente di accedere solo ai dati originali della cella. In un ambiente a thread multipli se provi a ottenere il valore formattato della cella, ad esempio con Cell.getStringValue() per valori numerici, potresti ottenere risultati o eccezioni imprevisti.

Il seguente codice:

1. Crea una cartella di lavoro.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori stringa.
1. Quindi crea due thread che leggono simultaneamente valori da celle casuali.
 Se i valori letti sono corretti non succede nulla. Se i valori letti non sono corretti viene visualizzato un messaggio.

Se commenti questa riga:

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

quindi viene visualizzato il seguente messaggio:

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Altrimenti il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
