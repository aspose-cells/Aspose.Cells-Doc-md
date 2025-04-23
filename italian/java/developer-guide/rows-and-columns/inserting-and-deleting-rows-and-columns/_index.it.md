---
title: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 60
url: /it/java/inserting-and-deleting-rows-and-columns/
description: Scopri come Inserire e Cancellare Righe e Colonne tramite l API Aspose.Cells for Java.
keywords: Come Inserire e Cancellare Righe e Colonne in Java, Inserire Righe e Colonne usando Java, Java Cancella righe e colonne, Inserire righe o colonne con Java, Cancella righe o colonne via Java.
---

## **Introduzione**
Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo dover aggiungere righe o colonne aggiuntive per ospitare più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.

Per soddisfare queste esigenze, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.
## **Gestione delle righe/colonne**
Aspose.Cells fornisce una classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}} 

Quando vengono aggiunte righe o colonne, il contenuto nel foglio di lavoro viene spostato verso il basso o verso destra, ma se vengono rimosse righe o colonne, il contenuto viene spostato verso l'alto o verso sinistra.

{{% /alert %}} 
## **Come inserire una riga**
Inserire una riga in qualsiasi posizione chiamando il metodo [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) accetta come primo argomento l’indice della riga in cui inserire la nuova riga, e come secondo argomento il numero di righe da inserire.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Come inserire più righe**
Per inserire più righe nel foglio di lavoro, chiamare il metodo [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) richiede due parametri:

- Indice di riga: l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe: il numero totale di righe che devono essere inserite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Come inserire una riga con formattazione**
Per inserire una riga con opzioni di formattazione, usare l’overload [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) che accetta come parametro [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions). Impostare la proprietà [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) della classe [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) con l’enumerazione [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). L’enumerazione [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) ha tre membri come elencato di seguito.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Formatta la riga come quella sopra.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): Formatta la riga come quella sotto.
- [PULISCI](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Cancella la formattazione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Come Eliminare una Riga**
Per eliminare una riga in qualsiasi posizione, chiamare il metodo [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) richiede due parametri:

- Indice di riga: l'indice della riga da cui verranno eliminate le righe.
- Numero di righe: il numero totale di righe che devono essere eliminate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Come eliminare più righe**
Per eliminare più righe da un foglio di lavoro, chiamare il metodo [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) richiede due parametri:

- Indice di riga: l'indice della riga da cui verranno eliminate le righe.
- Numero di righe: il numero totale di righe che devono essere eliminate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Come Inserire una o Più Colonne**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) richiede due parametri:

- Indice della colonna, l'indice della colonna da cui verrà inserita la colonna
- Numero di colonne, il numero totale di colonne che devono essere inserite

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Come eliminare una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) della collezione [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Il metodo [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) richiede i seguenti parametri:

- Indice della colonna: l'indice della colonna da cui verrà eliminata la colonna.
- Numero di colonne: il numero totale di colonne che devono essere eliminate.
- Aggiorna Riferimenti: parametro booleano per indicare se aggiornare i riferimenti in altri fogli di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
