---
title: Inserimento ed eliminazione di righe e colonne del file Excel
linktitle: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 70
url: /it/python-net/inserting-and-deleting-rows-and-columns/
description: Questo articolo mostra come inserire ed eliminare righe e colonne tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Aspose.Cells Python gestisce righe e colonne, inserisce righe e colonne in Python, elimina righe e colonne in Python, rimuove righe e colonne in Python.
---

## **Introduzione**

Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo dover aggiungere righe o colonne aggiuntive per ospitare più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.
Per soddisfare queste esigenze, Aspose.Cells per Python via .NET fornisce un insieme molto semplice di classi e metodi, discussi di seguito.

### **Gestire righe e colonne**

Aspose.Cells per Python via .NET fornisce una classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}}

Quando vengono aggiunte righe o colonne, i contenuti nel foglio di lavoro vengono spostati in giù o a destra, e se vengono rimosse righe o colonne, i contenuti vengono spostati in su o a sinistra.

{{% /alert %}}


## **Inserire righe e colonne**

### **Come inserire una riga**

Inserire una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) della raccolta [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Il metodo [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) richiede l'indice della riga in cui verrà inserita la nuova riga.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Come inserire più righe**

Per inserire più righe in un foglio di lavoro, chiamare il metodo [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Il metodo [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) richiede due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, il numero totale di righe da inserire.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Come inserire una riga con formattazione**

Per inserire una riga con opzioni di formattazione, utilizzare il sovraccarico [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) che richiede [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) come parametro. Impostare la proprietà [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) della classe [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) con l'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/). L'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) ha tre membri come indicato di seguito.

- UGUALE_A_QUOTA_SOPRA: Formatta la riga come la riga sopra.
- UGUALE_A_QUOTA_SOTTO: Formatta la riga come la riga sotto.
- CANCELLA: Cancella la formattazione.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Come inserire una colonna**

Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Il metodo [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) richiede l'indice della colonna in cui verrà inserita la nuova colonna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Eliminare righe e colonne**

### **Come eliminare più righe**

Per eliminare più righe da un foglio di lavoro, chiamare il metodo [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) della collezione [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Il metodo [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) richiede due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, il numero totale di righe da eliminare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Come eliminare una colonna**

Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Il metodo [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) richiede l'indice della colonna da eliminare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
