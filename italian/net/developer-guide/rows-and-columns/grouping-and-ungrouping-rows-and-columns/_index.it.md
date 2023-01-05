---
title: Raggruppamento e separazione di righe e colonne
type: docs
weight: 50
url: /it/net/grouping-and-ungrouping-rows-and-columns/
---
## **introduzione**

In un file Excel Microsoft, puoi creare una struttura per i dati per mostrare e nascondere i livelli di dettaglio con un solo clic del mouse.

 Clicca il**Simboli di contorno**, 1,2,3, + e - per visualizzare rapidamente solo le righe o le colonne che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per visualizzare i dettagli sotto un singolo riepilogo o intestazione come mostrato di seguito nella figura :

|**Raggruppamento di righe e colonne.**|
|:- |
|![cose da fare:immagine_alt_testo](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestione di gruppo di righe e colonne**

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.

### **Raggruppamento di righe e colonne**

 È possibile raggruppare righe o colonne chiamando il metodo[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) e[**Raggruppacolonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) metodi del[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collezione. Entrambi i metodi accettano i seguenti parametri:

- Indice prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna del gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Impostazioni di gruppo**

Microsoft Excel consente di configurare le impostazioni di gruppo per la visualizzazione:

- Righe di riepilogo sotto i dettagli.
- Colonne di riepilogo a destra dei dettagli.

 Gli sviluppatori possono configurare queste impostazioni di gruppo utilizzando il file[**Schema**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) proprietà del[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)classe.

### **Riepilogo righe al di sotto del dettaglio**

 È possibile controllare se le righe di riepilogo vengono visualizzate sotto i dettagli impostando il[**Schema**](https://reference.aspose.com/cells/net/aspose.cells/outline) classe'[**RiepilogoRigaSotto**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) proprietà a**VERO** o**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Colonne di riepilogo a destra del dettaglio**

 Gli sviluppatori possono anche controllare la visualizzazione delle colonne di riepilogo a destra dei dettagli impostando l'estensione[**Riepilogo Colonna Destra**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) proprietà di[**Schema**](https://reference.aspose.com/cells/net/aspose.cells/outline) classe a**VERO** o**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Separazione di righe e colonne**

 Per separare eventuali righe o colonne raggruppate, chiama il metodo[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) della collezione[**SeparaRighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) e[**Separacolonne**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)metodi. Entrambi i metodi accettano due parametri:

- Indice della prima riga o colonna, la prima riga/colonna da separare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da separare.

[**SeparaRighe**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) ha un sovraccarico che accetta un terzo parametro booleano. Impostandolo su**VERO**rimuove tutte le informazioni raggruppate. In caso contrario, vengono rimosse solo le informazioni sul gruppo esterno.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
