---
title: Lettura di Cell valori in più thread contemporaneamente
linktitle: Più thread
type: docs
weight: 1100
url: /it/java/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

La necessità di leggere contemporaneamente i valori delle celle in più thread è un requisito comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

 Per leggere i valori delle celle in più di un thread contemporaneamente, imposta[**Foglio di lavoro.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) a**VERO**In caso contrario, potresti ottenere valori di cella errati. Tieni presente che alcune funzionalità come la formattazione dei valori delle celle non sono supportate per thread multipli. Quindi MultiThreadReading ti consente solo di accedere solo ai dati originali della cella. In un ambiente con più thread, se si tenta di ottenere il valore formattato della cella, ad esempio da Cell.getStringValue() per i valori numerici, è possibile che si ottengano risultati o eccezioni imprevisti.

Il seguente codice:

1. Crea una cartella di lavoro.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori stringa.
1. Quindi crea due thread che leggono simultaneamente i valori da celle casuali.
 Se i valori letti sono corretti non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

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

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
