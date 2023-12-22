---
title: Raggruppamento, separazione di righe e colonne
type: docs
weight: 30
url: /it/cpp/grouping-ungrouping-rows-and-columns/
---
##  **introduzione**
In un file Excel Microsoft, puoi creare una struttura per i dati per consentirti di mostrare e nascondere i livelli di dettaglio con un solo clic del mouse.

Fai clic sui *Simboli di struttura**, 1,2,3, + e - per visualizzare rapidamente solo le righe o le colonne che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro oppure puoi utilizzare i simboli per visualizzare i dettagli in un singolo riepilogo o intestazione.
##  **Gestione del gruppo di righe e colonne**
 Aspose.Cells fornisce una lezione,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce un[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)raccolta che rappresenta tutte le celle del foglio di lavoro.

 IL[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi vengono discussi di seguito in maggiore dettaglio.
###  **Raggruppamento di righe e colonne**
 È possibile raggruppare righe o colonne chiamando il comando[Righe di gruppo](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) E[GruppoColonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) metodi del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collezione. Entrambi i metodi accettano i seguenti parametri:

- L'indice della prima riga/colonna, la prima riga o colonna del gruppo.
- L'indice dell'ultima riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno le righe/colonne dopo il raggruppamento.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **Impostazioni del gruppo**
Microsoft Excel consente di configurare le impostazioni del gruppo per la visualizzazione:

- Righe di riepilogo sotto i dettagli.
- Colonne di riepilogo a destra del dettaglio.
##  **Separazione di righe e colonne**
 Per separare eventuali righe o colonne raggruppate, chiamare il file[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione[Separarighe](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) E[Separacolonne](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)metodi. Entrambi i metodi accettano due parametri:

- L'indice della prima riga o colonna, la prima riga/colonna da separare.
- L'indice dell'ultima riga o colonna, l'ultima riga/colonna da separare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
