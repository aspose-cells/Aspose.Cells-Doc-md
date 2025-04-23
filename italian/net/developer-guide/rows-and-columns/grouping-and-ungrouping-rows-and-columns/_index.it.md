---
title: Raggruppamento e Sgrovigliamento di Righe e Colonne
type: docs
weight: 50
url: /it/net/grouping-and-ungrouping-rows-and-columns/
---

## **Introduzione**

In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Riepilogo**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono riepiloghi o intestazioni per sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un riepilogo o intestazione individuale come mostrato di seguito nella figura:

|**Raggruppamento di Righe e Colonne**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestione gruppi di righe e colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.

### **Raggruppamento di Righe e Colonne**

È possibile raggruppare righe o colonne chiamando i metodi [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) e [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) della raccolta [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi prendono i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Impostazioni di raggruppamento**

Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Le colonne di riepilogo a destra del dettaglio.

Gli sviluppatori possono configurare queste impostazioni di gruppo utilizzando la proprietà [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) della classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

### **Riepiloghi delle Righe al di Sotto del Dettaglio**

È possibile controllare se le righe di riepilogo vengono visualizzate sotto i dettagli impostando la proprietà [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) della classe [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) su **true** o **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Colonne sommario a destra dei dettagli**

I developer possono anche controllare la visualizzazione delle colonne riepilogative a destra dei dettagli impostando la proprietà [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) della classe [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) su **true** o **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Separazione delle righe e delle colonne**

Per annullare il raggruppamento di qualsiasi riga o colonna raggruppata, chiamare i metodi [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) e [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) della collezione [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Entrambi i metodi richiedono due parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) ha un sovraccarico che richiede un terzo parametro booleano. Impostandolo su **true** si rimuovono tutte le informazioni raggruppate. In caso contrario, viene rimossa solo l'informazione esterna del gruppo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
