---
title: Inserimento, eliminazione di righe e colonne
type: docs
weight: 40
url: /it/cpp/inserting-deleting-rows-and-columns/
---
## **introduzione**
Sia che si crei un nuovo foglio di lavoro da zero o che si lavori su un foglio di lavoro esistente, potrebbe essere necessario aggiungere ulteriori righe o colonne per contenere più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specificate nel foglio di lavoro. Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.
### **Gestione di righe e colonne**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) , che rappresenta un file Microsoft Excel. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce un[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}} 

Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso o verso destra e, se vengono rimosse righe o colonne, il contenuto viene spostato verso l'alto o verso sinistra.

{{% /alert %}} 
#### **Inserisci una riga**
 Inserisci una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo[InserisciRiga](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Il[InserisciRiga](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)Il metodo accetta l'indice della riga in cui verrà inserita la nuova riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **Inserimento di più righe**
 Per inserire più righe in un foglio di lavoro, chiama il metodo[InserisciRighe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Il[InserisciRighe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)metodo accetta due parametri:

- Indice di riga, l'indice della riga da cui verranno inserite le nuove righe.
- Numero di righe, il numero totale di righe che devono essere inserite.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **Eliminazione di più righe**
Per eliminare più righe da un foglio di lavoro, chiama il metodo[Elimina righe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Il[Elimina righe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)metodo accetta due parametri:

- Indice di riga, l'indice della riga da cui verranno eliminate le righe.
- Numero di righe, il numero totale di righe che devono essere eliminate.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **Inserisci una colonna**
 Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo[Inserisci colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione.[Inserisci colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)Il metodo accetta l'indice della colonna in cui verrà inserita la nuova colonna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **Elimina una colonna**
 Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il metodo[Elimina colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b) metodo del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) collezione. Il[Elimina colonna](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)Il metodo accetta l'indice della colonna da eliminare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
