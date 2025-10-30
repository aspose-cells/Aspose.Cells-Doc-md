---
title: Inserimento, Eliminazione di Righe e Colonne
type: docs
weight: 40
url: /it/cpp/inserting-deleting-rows-and-columns/
---

## **Introduzione**
Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo avere bisogno di aggiungere righe o colonne aggiuntive per ospitare più dati. In modo inverso, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro. Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.
### **Gestione di Righe e Colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione di [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) che rappresenta tutte le celle nel foglio di lavoro.

La collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}} 

Quando vengono aggiunte righe o colonne, i contenuti nel foglio di lavoro vengono spostati in giù o a destra, e se vengono rimosse righe o colonne, i contenuti vengono spostati in su o a sinistra.

{{% /alert %}} 
#### **Inserire una Riga**
Inserire una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) richiede l'indice della riga dove verrà inserita la nuova riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Inserimento di Più Righe**
Per inserire più righe in un foglio di lavoro, chiamare il metodo [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) richiede due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, il numero totale di righe da inserire.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Eliminazione di Più Righe**
Per eliminare più righe da un foglio di lavoro, chiamare il metodo [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) richiede due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, il numero totale di righe da eliminare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Inserire una colonna**
Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) richiede l'indice della colonna dove verrà inserita la nuova colonna.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Eliminare una colonna**
Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Il metodo [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) richiede l'indice della colonna da eliminare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
