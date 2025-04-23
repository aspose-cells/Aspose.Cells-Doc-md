---
title: Conversione tra nome della cella e indice riga/colonna
linktitle: Nome della Cella e Conversione Indice
type: docs
weight: 5
url: /it/java/names-and-indices/
description: Scopri come ottenere il risultato della conversione tra nome della cella e indice della riga/colonna con Aspose.Cells for Java API.
keywords: Java Convertire l indice della cella in nome, Convertire il nome della cella in indice della riga/colonna usando le api di java, Come ottenere il nome della cella da Indici di Riga e Colonna.
---

## **Come ottenere il nome della cella da Indici di Riga e Colonna**
È possibile trovare il nome di una cella dato l'indice di riga e colonna. Questo articolo spiega come fare.

Aspose.Cells fornisce il metodo [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) che permette agli sviluppatori di ottenere il nome di una cella se forniscono l’indice di riga e colonna.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il seguente esempio di codice illustra come usare [CellsHelper.cellIndexToName](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellIndexToName-int-int-) per accedere al nome di una cella dato un indice di riga e colonna conosciuti. Il codice genera il seguente output.

{{< highlight java >}}

Cell Name at [0, 0]: A1

Cell Name at [4, 0]: A5

Cell Name at [0, 4]: E1

Cell Name at [2, 2]: C3

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-IndexToName-1.java" >}}
## **Come ottenere gli indici di riga e colonna dal Nome della Cellula**
È possibile trovare un indice di riga e colonna della cella dal suo nome. Questo articolo spiega come.

Aspose.Cells fornisce il metodo [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) che consente agli sviluppatori di ottenere un indice di riga e colonna dal nome della cella.

{{% alert color="primary" %}} 

Microsoft Excel inizia a contare gli indici di riga e colonna da 1. A differenza di Microsoft Excel, Aspose.Cells inizia a contare gli indici di riga e colonna da 0.

{{% /alert %}} 

Il seguente esempio di codice illustra come usare [CellsHelper.cellNameToIndex](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#cellNameToIndex-java.lang.String-) per ottenere l'indice di riga e colonna dal nome della cella. Il codice genera il seguente output.

{{< highlight java >}}

Row Index of Cell C6: 5

Column Index of Cell C6: 2

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-NameToIndex-1.java" >}}
## **Come creare nomi di foglio sicuri**
A volte c'è la necessità di assegnare il nome del foglio in fase di esecuzione. In questo scenario, potrebbero esserci nomi di foglio che contengono alcuni caratteri aggiuntivi come <>+(?”. È necessario sostituire qualsiasi carattere non consentito come nome del foglio con un carattere preimpostato fornito dall'utente. Allo stesso modo, la lunghezza potrebbe aumentare a più di 31 caratteri che devono essere troncati. Apache POI fornisce determinate funzionalità per la creazione di nomi sicuri, pertanto una funzionalità simile è fornita da Aspose.Cells per gestire tutti questi problemi. Il codice di esempio seguente illustra questa funzionalità:



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-CreateSafeSheetName.java" >}}

**Output della console**

questo è il primo nome che viene cre

{{< highlight java >}}

` `<> + (adj.Private _ " Private"

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
