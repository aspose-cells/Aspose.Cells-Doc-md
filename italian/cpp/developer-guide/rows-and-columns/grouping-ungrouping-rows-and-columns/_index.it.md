---
title: Raggruppamento, separazione di righe e colonne
type: docs
weight: 30
url: /it/cpp/grouping-ungrouping-rows-and-columns/
---
## **introduzione**
In un file Excel Microsoft, puoi creare una struttura per i dati per mostrare e nascondere i livelli di dettaglio con un solo clic del mouse.

 Clicca il**Simboli di contorno**, 1,2,3, + e - per visualizzare rapidamente solo le righe o le colonne che forniscono riepiloghi o intestazioni per le sezioni in un foglio di lavoro oppure è possibile utilizzare i simboli per visualizzare i dettagli sotto un singolo riepilogo o intestazione.
## **Gestione di gruppo di righe e colonne**
 Aspose.Cells offre un corso,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) che rappresenta un file Excel Microsoft. Il[Cartella di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la classe contiene un[Fogli di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) raccolta che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) classe. Il[Foglio di lavoro](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) la classe fornisce un[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)raccolta che rappresenta tutte le celle del foglio di lavoro.

 Il[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro, alcuni di questi sono discussi di seguito in modo più dettagliato.
### **Raggruppamento di righe e colonne**
 È possibile raggruppare righe o colonne chiamando il metodo[GroupRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332) e[Raggruppacolonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8) metodi del[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collezione. Entrambi i metodi accettano i seguenti parametri:

- Il primo indice di riga/colonna, la prima riga o colonna nel gruppo.
- L'ultimo indice di riga/colonna, l'ultima riga o colonna nel gruppo.
- È nascosto, un parametro booleano che specifica se nascondere o meno righe/colonne dopo il raggruppamento.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **Impostazioni di gruppo**
Microsoft Excel consente di configurare le impostazioni di gruppo per la visualizzazione:

- Righe di riepilogo sotto i dettagli.
- Colonne di riepilogo a destra dei dettagli.
## **Separazione di righe e colonne**
 Per separare eventuali righe o colonne raggruppate, chiama il metodo[ICelle](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) della collezione[SeparaRighe](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1) e[Separacolonne](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)metodi. Entrambi i metodi accettano due parametri:

- L'indice della prima riga o colonna, la prima riga/colonna da separare.
- L'ultimo indice di riga o colonna, l'ultima riga/colonna da separare.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
