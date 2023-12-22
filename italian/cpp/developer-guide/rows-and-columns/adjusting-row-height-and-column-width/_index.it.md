---
title: Regolazione dell'altezza della riga e della larghezza della colonna
type: docs
weight: 10
url: /it/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

Quando lavori con fogli di calcolo e aggiungi dati a righe o colonne, potrebbe essere necessario modificare l'altezza delle righe o la larghezza delle colonne. A volte, applicare la formattazione su righe o colonne significa che l'altezza o la larghezza corrente devono essere modificate per mostrare i dati. Normalmente, gli utenti regolano l'altezza delle righe e la larghezza delle colonne in un ambiente WYSIWYG utilizzando Microsoft Excel. Ma con Aspose.Cells gli sviluppatori possono eseguire queste operazioni in fase di runtime.

{{% /alert %}} 
##  **Lavorare con le righe**
###  **Regolazione dell'altezza della fila**
 Aspose.Cells fornisce una lezione,[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file Excel Microsoft. IL[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la classe contiene a[Raccolta di fogli di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) classe. IL[Foglio di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) la classe fornisce a[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) raccolta che rappresenta tutte le celle del foglio di lavoro. IL[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection fornisce diversi metodi per gestire righe o colonne in un foglio di lavoro. Alcuni di questi sono discussi di seguito in maggiore dettaglio.
####  **Impostazione dell'altezza di una riga**
 È possibile impostare l'altezza di una singola riga chiamando il metodo[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione[Imposta altezza riga](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) metodo. IL[Imposta altezza riga](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)Il metodo accetta i seguenti parametri come segue:

- *Indice riga**, l'indice della riga di cui stai modificando l'altezza.
- *Altezza riga**, l'altezza della riga da applicare alla riga.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Impostazione dell'altezza di tutte le righe in un foglio di lavoro**
 Se gli sviluppatori devono impostare la stessa altezza di riga per tutte le righe nel foglio di lavoro, possono farlo utilizzando il file[Imposta altezza standard](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) metodo del[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collezione.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Lavorare con le colonne**
###  **Impostazione della larghezza di una colonna**
 Imposta la larghezza di una colonna chiamando il metodo[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione[Imposta larghezza colonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) metodo. IL[Imposta larghezza colonna](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)Il metodo accetta i seguenti parametri:

- *Indice colonna**, l'indice della colonna di cui stai modificando la larghezza.
- *Larghezza colonna**, la larghezza della colonna desiderata.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Impostazione della larghezza di tutte le colonne in un foglio di lavoro**
 Per impostare la stessa larghezza di colonna per tutte le colonne del foglio di lavoro, utilizzare il comando[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collezione[Imposta larghezza standard](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)metodo.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
