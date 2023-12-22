---
title: Inserimento, eliminazione di righe e colonne
type: docs
weight: 40
url: /it/cpp/inserting-deleting-rows-and-columns/
---
##  **introduzione**
Sia che si crei un nuovo foglio di lavoro da zero o si lavori su un foglio di lavoro esistente, potrebbe essere necessario aggiungere righe o colonne aggiuntive per contenere più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro. Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.
###  **Gestione di righe e colonne**
 Aspose.Cells fornisce una lezione,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) , che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)raccolta che rappresenta tutte le celle del foglio di lavoro.

 IL[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection fornisce diversi metodi per la gestione di righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}} 

Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso o a destra e se righe o colonne vengono rimosse, il contenuto viene spostato verso l'alto o a sinistra.

{{% /alert %}} 
####  **Inserisci una riga**
 Inserisci una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo[InserisciRiga](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. IL[InserisciRiga](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)Il metodo prende l'indice della riga in cui verrà inserita la nuova riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **Inserimento di più righe**
 Per inserire più righe in un foglio di lavoro, chiama il comando[InserisciRighe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. IL[InserisciRighe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)il metodo accetta due parametri:

- Indice riga, l'indice della riga da cui verranno inserite le nuove righe.
- Numero di righe, il numero totale di righe che devono essere inserite.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **Eliminazione di più righe**
 Per eliminare più righe da un foglio di lavoro, chiama il file[Eliminarighe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. IL[Eliminarighe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)il metodo accetta due parametri:

- Indice riga, l'indice della riga da cui verranno eliminate le righe.
- Numero di righe, il numero totale di righe che devono essere eliminate.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **Inserisci una colonna**
 Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il comando[InserisciColonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione.[InserisciColonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)Il metodo prende l'indice della colonna in cui verrà inserita la nuova colonna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **Elimina una colonna**
 Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il file[Elimina colonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione. IL[Elimina colonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)Il metodo accetta l'indice della colonna da eliminare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
