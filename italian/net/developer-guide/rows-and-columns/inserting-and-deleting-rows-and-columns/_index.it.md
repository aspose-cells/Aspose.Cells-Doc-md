---
title: Inserimento ed eliminazione di righe e colonne del file Excel
linktitle: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 70
url: /it/net/inserting-and-deleting-rows-and-columns/
description: Questo articolo mostra come inserire ed eliminare righe e colonne tramite l API Aspose.Cells for .NET.
keywords: Aspose.Cells C# gestisce righe e colonne, inserisce righe e colonne, elimina righe e colonne
---

## **Introduzione**

Che si stia creando un nuovo foglio di lavoro da zero o si stia lavorando su un foglio di lavoro esistente, potremmo dover aggiungere righe o colonne aggiuntive per ospitare più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.
Per soddisfare queste esigenze, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.

### **Gestire righe e colonne**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di calcolo in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fornisce diversi metodi per gestire righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}}

Quando vengono aggiunte righe o colonne, i contenuti nel foglio di lavoro vengono spostati in giù o a destra, e se vengono rimosse righe o colonne, i contenuti vengono spostati in su o a sinistra.

{{% /alert %}}


## **Inserire righe e colonne**

### **Come inserire una riga**

Inserire una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) richiede l'indice della riga in cui verrà inserita la nuova riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Come inserire più righe**

Per inserire più righe in un foglio di lavoro, chiamare il metodo [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) richiede due parametri:

- Indice di riga, l'indice della riga da cui saranno inserite le nuove righe.
- Numero di righe, il numero totale di righe da inserire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Come inserire una riga con formattazione**

Per inserire una riga con opzioni di formattazione, utilizzare il sovraccarico [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) che richiede [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) come parametro. Impostare la proprietà [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) della classe [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) con l'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype). L'enumerazione [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) ha tre membri come indicato di seguito.

- Uguale a sopra: Formatta la riga come la riga precedente.
- UgualeAlSotto: Formatta la riga come la riga sottostante.
- Cancella: Cancella la formattazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Come inserire una colonna**

Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il metodo [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) richiede l'indice della colonna in cui verrà inserita la nuova colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Eliminare righe e colonne**

### **Come eliminare più righe**

Per eliminare più righe da un foglio di lavoro, chiamare il metodo [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) richiede due parametri:

- Indice riga, l'indice della riga da cui partiranno le eliminazioni.
- Numero di righe, il numero totale di righe da eliminare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Come eliminare una colonna**

Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiamare il metodo [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Il metodo [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) richiede l'indice della colonna da eliminare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
