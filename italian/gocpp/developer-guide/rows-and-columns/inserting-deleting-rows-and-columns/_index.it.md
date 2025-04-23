---
title: Inserimento, Eliminazione di Righe e Colonne
type: docs
weight: 40
url: /it/go-cpp/inserting-deleting-rows-and-columns/
---

## **Introduzione**

Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo avere bisogno di aggiungere righe o colonne aggiuntive per ospitare più dati. In modo inverso, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro. Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.

### **Gestione di Righe e Colonne**

Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una collezione [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) fornisce una collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) che rappresenta tutte le celle del foglio.

La collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}}

Quando vengono aggiunte righe o colonne, i contenuti nel foglio di lavoro vengono spostati in giù o a destra, e se vengono rimosse righe o colonne, i contenuti vengono spostati in su o a sinistra.

{{% /alert %}}

Inserisci una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) prende come parametro l'indice della riga in cui si vuole inserire la nuova riga.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Inserimento di Più Righe**

Per inserire più righe in un foglio di lavoro, chiamare il metodo [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) prende due parametri:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Eliminazione di Più Righe**

Per eliminare più righe da un foglio di lavoro, chiama il metodo [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) prende due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, il numero totale di righe da eliminare.

#### **Inserire una colonna**

Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) prende l'indice della colonna dove verrà inserita la nuova colonna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il metodo [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) della collezione [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Il metodo [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) prende l'indice della colonna da eliminare.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
