---
title: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 60
url: /it/java/inserting-and-deleting-rows-and-columns/
description: Scopri come inserire ed eliminare righe e colonne tramite le API Aspose.Cells for Java.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **introduzione**
Sia che si crei un nuovo foglio di lavoro da zero o si lavori su un foglio di lavoro esistente, potrebbe essere necessario aggiungere righe o colonne aggiuntive per contenere più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.

Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.
##  **Come gestire righe/colonne**
 Aspose.Cells fornisce a[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene a[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 IL[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection fornisce diversi metodi per la gestione di righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}} 

Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso o verso destra, ma se righe o colonne vengono rimosse, il contenuto viene spostato verso l'alto o verso sinistra.

{{% /alert %}} 
##  **Come inserire una riga**
 Inserisci una riga in qualsiasi posizione chiamando il metodo[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. IL[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))prende l'indice della riga in cui verrà inserita la nuova riga come primo argomento e il numero di righe da inserire come secondo argomento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Come inserire più righe**
 Per inserire più righe nel foglio di lavoro, chiamare il comando[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. IL[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) metodo accetta due parametri:

- Indice riga: l'indice della riga da cui verranno inserite le nuove righe.
- Numero di righe: il numero totale di righe che devono essere inserite.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Come inserire una riga con formattazione**
Per inserire una riga con opzioni di formattazione, utilizzare il file[insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)sovraccarico che richiede[InserisciOpzioni](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)come parametro. Impostare il[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)proprietà di[InserisciOpzioni](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)lezione con[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Enumerazione. IL[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)L'enumerazione ha tre membri come elencato di seguito.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): formatta la riga come la riga precedente.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): formatta la riga come la riga seguente.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): cancella la formattazione.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Come eliminare una riga**
 Per eliminare una riga in qualsiasi posizione, chiama il file[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. IL[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metodo accetta due parametri:

- Indice riga: l'indice della riga da cui verranno eliminate le righe.
- Numero di righe: il numero totale di righe che devono essere eliminate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Come eliminare più righe**
 Per eliminare più righe da un foglio di lavoro, chiama il file[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. IL[deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) metodo accetta due parametri:

- Indice riga: l'indice della riga da cui verranno eliminate le righe.
- Numero di righe: il numero totale di righe che devono essere eliminate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Come inserire una o più colonne**
 Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il comando[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collezione. IL[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) metodo accetta due parametri:

- Indice colonna, l'indice della colonna da cui verrà inserita la colonna
- Numero di colonne, il numero totale di colonne che devono essere inserite

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Come eliminare una colonna**
 Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il file[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) metodo del[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collezione. IL[deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) accetta i seguenti parametri:

- Indice colonna: l'indice della colonna da cui verrà eliminata la colonna.
- Numero di colonne: il numero totale di colonne che devono essere eliminate.
- Aggiorna riferimento: parametro booleano per indicare se aggiornare i riferimenti in altri fogli di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

