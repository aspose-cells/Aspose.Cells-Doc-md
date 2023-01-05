---
title: Copiare e spostare fogli di lavoro
type: docs
weight: 20
url: /it/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

A volte, hai bisogno di un numero di fogli di lavoro con formattazione e dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare una cartella di lavoro con fogli che contengono le stesse intestazioni di colonna, intestazioni di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo.

Aspose.Cells supporta la copia e lo spostamento di fogli di lavoro all'interno o tra cartelle di lavoro. Il foglio di lavoro, completo di dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, viene copiato con il massimo grado di precisione.

{{% /alert %}}

## **Spostare o copiare fogli utilizzando Microsoft Excel**

Di seguito sono riportati i passaggi necessari per copiare e spostare i fogli di lavoro all'interno o tra le cartelle di lavoro.

1. Per spostare o copiare fogli in un'altra cartella di lavoro, apri la cartella di lavoro che riceverà i fogli.
1. Passare alla cartella di lavoro che contiene i fogli che si desidera spostare o copiare e quindi selezionare i fogli.
1.  Sul**Modificare** menu, fare clic**Sposta o copia foglio**.
1. Nella casella Per prenotare fare clic sulla cartella di lavoro per ricevere i fogli.
1.  Per spostare o copiare i fogli selezionati in una nuova cartella di lavoro, fare clic su**nuovo libro**.
1.  Nel**Prima foglio** fare clic sul foglio prima del quale si desidera inserire i fogli spostati o copiati.
1.  Per copiare i fogli invece di spostarli, seleziona il file**Crea una copia** casella di controllo.

## **Copia i fogli di lavoro all'interno di una cartella di lavoro**

 Aspose.Cells fornisce un metodo sovraccarico,[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo accetta l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine.

L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di una cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Copia fogli di lavoro tra cartelle di lavoro**

 Aspose.Cells fornisce un metodo,[**Foglio di lavoro.copia()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), utilizzato per copiare i dati e la formattazione da un foglio di lavoro di origine a un altro foglio di lavoro all'interno o tra le cartelle di lavoro. Il metodo accetta l'oggetto del foglio di lavoro di origine come parametro.

L'esempio seguente mostra come copiare un foglio di lavoro da una cartella di lavoro a un'altra cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

L'esempio seguente mostra come copiare un foglio di lavoro da una cartella di lavoro a un'altra.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Sposta i fogli di lavoro all'interno della cartella di lavoro**

 Aspose.Cells fornisce un metodo,[**Foglio di lavoro.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), utilizzato per spostare un foglio di lavoro in un'altra posizione nello stesso foglio di lavoro.

L'esempio seguente mostra come spostare un foglio di lavoro in un'altra posizione all'interno della cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
