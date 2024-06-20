---
title: Raggruppamento e Sgrovigliamento di Righe e Colonne
type: docs
weight: 50
url: /it/python-net/grouping-and-ungrouping-rows-and-columns/
description: Questo articolo mostra come raggruppare e sgrovigliare righe e colonne tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Come raggruppare righe e colonne in Python, Come sgrovigliare righe e colonne in Python, Gestione gruppi di righe e colonne in Python, Come impostare righe di riepilogo sotto i dettagli in Python, Come impostare colonne di riepilogo a destra dei dettagli in Python.
---

## **Introduzione**

In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Riepilogo**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono riepiloghi o intestazioni per sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un riepilogo o intestazione individuale come mostrato di seguito nella figura:

|**Raggruppamento di Righe e Colonne**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestione gruppi di righe e colonne**

Aspose.Cells per Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.

### **Come raggruppare righe e colonne**

È possibile raggruppare righe o colonne chiamando i metodi [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) e [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) della raccolta [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Entrambi i metodi prendono i seguenti parametri:

- Indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- Indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Impostazioni di raggruppamento**

Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Le colonne di riepilogo a destra del dettaglio.

Gli sviluppatori possono configurare queste impostazioni di gruppo utilizzando la proprietà [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) della classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

### **Come impostare righe di riepilogo sotto i dettagli**

È possibile controllare se le righe di riepilogo vengono visualizzate sotto i dettagli impostando la proprietà [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) della classe [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) su **true** o **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Come impostare le colonne riepilogative a destra dei dettagli**

I developer possono anche controllare la visualizzazione delle colonne riepilogative a destra dei dettagli impostando la proprietà [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) della classe [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) su **true** o **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Come annullare la raggruppamento di righe e colonne**

Per annullare il raggruppamento di qualsiasi riga o colonna raggruppata, chiamare i metodi [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) e [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) della collezione [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Entrambi i metodi richiedono due parametri:

- Indice della prima riga o colonna, la prima riga/colonna da sraggruppare.
- Indice dell'ultima riga o colonna, l'ultima riga/colonna da sraggruppare.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) ha un sovraccarico che richiede un terzo parametro booleano. Impostandolo su **true** si rimuovono tutte le informazioni raggruppate. In caso contrario, viene rimossa solo l'informazione esterna del gruppo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
