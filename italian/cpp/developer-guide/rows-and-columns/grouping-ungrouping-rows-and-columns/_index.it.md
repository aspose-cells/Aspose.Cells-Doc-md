---
title: Raggruppamento, Sblocco righe e colonne
type: docs
weight: 30
url: /it/cpp/grouping-ungrouping-rows-and-columns/
---

## **Introduzione**
In un file Microsoft Excel, è possibile creare un'outline per i dati che consente di mostrare e nascondere livelli di dettaglio con un singolo clic del mouse.

Fare clic sui **Simboli di Outline**, 1,2,3, + e - per visualizzare rapidamente solo le righe o colonne che forniscono sommari o intestazioni per le sezioni in un foglio di lavoro, oppure è possibile utilizzare i simboli per vedere i dettagli sotto un sommario o un'intestazione individuale.
## **Gestione raggruppata di righe e colonne**
Aspose.Cells fornisce una classe, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta di [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) che rappresenta tutte le celle nel foglio di lavoro.

La raccolta di [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, di cui alcuni sono discussi di seguito in maggiore dettaglio.
### **Raggruppamento di righe e colonne**
È possibile raggruppare le righe o colonne chiamando i metodi [GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) e [GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) della raccolta [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Entrambi i metodi richiedono i seguenti parametri:

- L'indice della prima riga/colonna, la prima riga o colonna nel gruppo.
- L'indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **Impostazioni di raggruppamento**
Microsoft Excel consente di configurare le impostazioni di raggruppamento per la visualizzazione:

- Le righe di riassunto sotto il dettaglio.
- Le colonne di riepilogo a destra del dettaglio.
## **Sganciare Righe e Colonne**
Per disraggruppare qualsiasi riga o colonna raggruppata, chiamare i metodi [UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) e [UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) della collezione [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Entrambi i metodi richiedono due parametri:

- L'indice della prima riga o colonna, la prima riga/colonna da disraggruppare.
- L'indice dell'ultima riga o colonna, l'ultima riga/colonna da disraggruppare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
