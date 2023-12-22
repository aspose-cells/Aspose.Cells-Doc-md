---
title: Inserimento ed eliminazione di righe e colonne di file Excel
linktitle: Inserimento ed eliminazione di righe e colonne
type: docs
weight: 70
url: /it/net/inserting-and-deleting-rows-and-columns/
description: Questo articolo mostra come inserire ed eliminare righe e colonne tramite Aspose.Cells for .NET API.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **introduzione**

Sia che si crei un nuovo foglio di lavoro da zero o si lavori su un foglio di lavoro esistente, potrebbe essere necessario aggiungere righe o colonne aggiuntive per contenere più dati. Al contrario, potremmo anche dover eliminare righe o colonne da posizioni specifiche nel foglio di lavoro.
Per soddisfare questi requisiti, Aspose.Cells fornisce un insieme molto semplice di classi e metodi, discussi di seguito.

###  **Gestisci righe e colonne**

Aspose.Cells fornisce una lezione[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , che rappresenta un file Excel Microsoft. IL[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene a[**Fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)raccolta che consente l'accesso a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. IL[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 IL[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection fornisce diversi metodi per la gestione di righe e colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito.

{{% alert color="primary" %}}

Quando vengono aggiunte righe o colonne, il contenuto del foglio di lavoro viene spostato verso il basso o a destra e se righe o colonne vengono rimosse, il contenuto viene spostato verso l'alto o a sinistra.

{{% /alert %}}


##  **Inserisci righe e colonne**

###  **Come inserire una riga**

 Inserisci una riga nel foglio di lavoro in qualsiasi posizione chiamando il metodo[**InserisciRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. IL[**InserisciRiga**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)Il metodo prende l'indice della riga in cui verrà inserita la nuova riga.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **Come inserire più righe**

 Per inserire più righe in un foglio di lavoro, chiama il comando[**InserisciRighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. IL[**InserisciRighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)il metodo accetta due parametri:

- Indice riga, l'indice della riga da cui verranno inserite le nuove righe.
- Numero di righe, il numero totale di righe che devono essere inserite.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **Come inserire una riga con formattazione**

Per inserire una riga con opzioni di formattazione, utilizzare il file[**InserisciRighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)sovraccarico che richiede[**InserisciOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) come parametro. Impostare il[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) proprietà di[**InserisciOpzioni**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) lezione con[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) Enumerazione. IL[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)L'enumerazione ha tre membri come elencato di seguito.

- SameAsAbove: formatta la riga come la riga precedente.
- SameAsBelow: formatta la riga come la riga sottostante.
- Cancella: cancella la formattazione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **Come inserire una colonna**

 Gli sviluppatori possono anche inserire una colonna nel foglio di lavoro in qualsiasi posizione chiamando il comando[**InserisciColonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collezione. IL[**InserisciColonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)Il metodo prende l'indice della colonna in cui verrà inserita la nuova colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **Elimina righe e colonne**

###  **Come eliminare più righe**

 Per eliminare più righe da un foglio di lavoro, chiama il file[**Eliminarighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. IL[**Eliminarighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)il metodo accetta due parametri:

- Indice riga, l'indice della riga da cui verranno eliminate le righe.
- Numero di righe, il numero totale di righe che devono essere eliminate.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **Come eliminare una colonna**

 Per eliminare una colonna dal foglio di lavoro in qualsiasi posizione, chiama il file[**Elimina colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) metodo del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collezione. IL[**Elimina colonna**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)Il metodo accetta l'indice della colonna da eliminare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
