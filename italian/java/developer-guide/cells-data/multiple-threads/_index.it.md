---
title: Lettura di valori di celle in thread multipli contemporaneamente
linktitle: Thread multipli
type: docs
weight: 1100
url: /it/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Scopri come leggere i valori della cella in più thread contemporaneamente con le API Aspose.Cells for Java.
keywords: Legge i valori della cella Java in thread multipli contemporaneamente, thread multipli per Aspose.Cells for Java API.
---

{{% alert color="primary" %}}

La necessità di leggere i valori delle celle in thread multipli contemporaneamente è una richiesta comune. Questo articolo spiega come utilizzare Aspose.Cells per questo scopo.

{{% /alert %}}

## **Come leggere i valori della cella in più thread contemporaneamente con Aspose.Cells for Java**

Per leggere i valori delle celle in più di un thread contemporaneamente, impostare [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) su **true**. Se non lo si fa, potrebbero essere ottenuti valori errati delle celle. Si noti che alcune funzionalità come la formattazione dei valori delle celle non sono supportate per i thread multipli. Quindi, la lettura multithread abilita solo l'accesso ai dati originali delle celle. In un ambiente multi-thread se si cerca di ottenere il valore formattato della cella, ad esempio tramite Cell.getStringValue() per i valori numerici, potrebbe essere ottenuto un risultato inaspettato o un'eccezione.

Il seguente codice:

1. Crea un workbook.
1. Aggiunge un foglio di lavoro.
1. Popola il foglio di lavoro con valori di stringa.
1. Quindi crea due thread che leggono contemporaneamente valori da celle casuali.
   Se i valori letti sono corretti, non succede nulla. Se i valori letti non sono corretti, viene visualizzato un messaggio.

Se si commenta questa riga:

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

allora viene visualizzato il seguente messaggio:

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

In caso contrario, il programma viene eseguito senza mostrare alcun messaggio, il che significa che tutti i valori letti dalle celle sono corretti.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
{{< app/cells/assistant language="java" >}}
